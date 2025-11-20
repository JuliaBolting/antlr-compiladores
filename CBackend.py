class CBackend:
    def __init__(self, ir_code):
        self.ir = ir_code        # lista de tuplas (op, a1, a2, dest)
        self.lines = []
        self.temps = set()

    # adiciona uma linha ao código
    def emit(self, line):
        self.lines.append(line)

    # --------------------------------------------------
    # Coleta variáveis temporárias (ex.: t0, t1, t2...)
    # --------------------------------------------------
    def collect_temps(self):
        for op, a1, a2, dest in self.ir:
            if dest and isinstance(dest, str) and dest.startswith("t"):
                self.temps.add(dest)
            if a1 and isinstance(a1, str) and a1.startswith("t"):
                self.temps.add(a1)
            if a2 and isinstance(a2, str) and a2.startswith("t"):
                self.temps.add(a2)

    # --------------------------------------------------
    # Traduz uma instrução IR para C
    # --------------------------------------------------
    def translate(self, op, a1, a2, dest):

        # ---------------- MOV ----------------
        if op == "MOV":
            self.emit(f"    {dest} = {a1};")
            return

        # ---------------- NOT ----------------
        if op == "NOT":
            self.emit(f"    {dest} = !{a1};")
            return

        # ---------------- ARITMÉTICOS ----------------
        if op in ["+", "-", "*", "/", "%"]:
            self.emit(f"    {dest} = {a1} {op} {a2};")
            return

        # ---------------- RELACIONAIS ----------------
        if op in ["<", "<=", ">", ">=", "==", "!="]:
            self.emit(f"    {dest} = ({a1} {op} {a2});")
            return

        # ---------------- LÓGICOS ----------------
        if op in ["&&", "||"]:
            self.emit(f"    {dest} = ({a1} {op} {a2});")
            return

        # ---------------- LABEL ----------------
        if op == "LABEL":
            self.emit(f"{dest}:;")
            return

        # ---------------- GOTO ----------------
        if op == "GOTO":
            self.emit(f"    goto {dest};")
            return

        # ---------------- IF_TRUE ----------------
        if op == "IF_TRUE":
            self.emit(f"    if ({a1}) goto {dest};")
            return

        # ---------------- RETURN ----------------
        if op == "RETURN":
            if a1 is None:
                self.emit("    return 0;")
            else:
                self.emit(f"    return {a1};")
            return

        # ----------------------------------------------------
        # Se chegou aqui, instrução não reconhecida
        # ----------------------------------------------------
        print(f"[AVISO] Instrução IR não mapeada no backend C: {op}")

    # --------------------------------------------------
    # Gera o código C final
    # --------------------------------------------------
    def generate(self):
        self.emit("#include <stdio.h>")
        self.emit("")
        self.emit("int main() {")

        # declara temporários
        self.collect_temps()
        if self.temps:
            linha = "    int " + ", ".join(sorted(self.temps)) + ";"
            self.emit(linha)

        # traduz cada instrução
        for op, a1, a2, dest in self.ir:
            self.translate(op, a1, a2, dest)

        # retorno padrão se não houver
        self.emit("    return 0;")
        self.emit("}")

        return "\n".join(self.lines)
