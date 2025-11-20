class CBackend:

        # ir_code: lista de tuplas (op, a1, a2, dest),
        # produzida pelas VISITS da CodeGenVisitor:
        #
        # - visitDecFuncao / visitPrincipal: FUNC_START, FUNC_END, PARAM
        # - visitListaVariaveis: VAR_DECL
        # - visitLeitura / visitListaTermoLeitura / visitTermoLeitura: READ
        # - visitEscrita / visitListaTermoEscrita / visitTermoEscrita: LOAD_STR, LOAD_VAR, WRITE
        # - visitAtribuicao / visitComplemento / visitas de expressão: ASSIGN, LOAD_VAR, +, -, *, /, %, RELACIONAIS, LÓGICOS
        # - visitConstante: LOAD_INT, LOAD_REAL
        # - visitSelecao / visitEnquanto: IF_FALSE_GOTO, LABEL, GOTO
        # - visitChamadaFuncao / visitArgumentos / visitListaArgumentos: ARG, CALL
        #


    def __init__(self, ir_code):
        self.ir = ir_code
        self.lines = []
        self.temps = set()
        self.string_temps = set()
        # novo: nome_func -> [(tipo, nome), ...]
        self.func_params = {}
        # Pré-passo só olhando IR de funções/parâmetros
        self._scan_functions()


    # --------------------------------------------------
    # Pré-passo: descobre parâmetros de cada função
    # Gramática relacionada:
    #   decFuncao
    #       : tipoRetorno ID PAREN1 parametros PAREN2 bloco
    #   parametros
    #       : listaParametros
    #       | /* vazio */
    #   listaParametros
    #       : tipo ID
    #       | listaParametros VIRG tipo ID
    # Visit correspondente: visitDecFuncao, visitParametros, visitListaParametros
    # --------------------------------------------------
    def _scan_functions(self):
        current_func = None
        for op, a1, a2, dest in self.ir:
            if op == "FUNC_START":
                current_func = a1
                self.func_params[current_func] = []
            elif op == "FUNC_END":
                current_func = None
            elif op == "PARAM" and current_func is not None:
                nome = a1
                tipo = a2 or "int"
                if tipo == "boolean":
                    tipo = "int"
                self.func_params[current_func].append((tipo, nome))


    # adiciona uma linha ao código
    def emit(self, line):
        self.lines.append(line)


    # --------------------------------------------------
    # Coleta variáveis temporárias (t0, t1, t2, ...)
    # Essas temps são criadas pela CodeGenVisitor em:
    #   - new_temp() chamado em:
    #       * expressões (exprAditiva, exprMultiplicativa, exprRelacional,
    #         exprE, exprOu, NOT, fator com ID/constante, etc.)
    #       * LOAD_STR / LOAD_VAR / LOAD_INT / LOAD_REAL
    # --------------------------------------------------
    def collect_temps(self):
        for op, a1, a2, dest in self.ir:
            if dest and isinstance(dest, str) and dest.startswith("t"):
                self.temps.add(dest)
            if a1 and isinstance(a1, str) and a1.startswith("t"):
                self.temps.add(a1)
            if a2 and isinstance(a2, str) and a2.startswith("t"):
                self.temps.add(a2)

            # marca temporários de string
            if op == "LOAD_STR" and dest:
                self.string_temps.add(dest)


    # --------------------------------------------------
    # Traduz uma instrução IR (op, a1, a2, dest) para C
    # Cada "op" abaixo está ligado a algum pedaço da gramática via o Visitor.
    # --------------------------------------------------
    def translate(self, op, a1, a2, dest):

        if op == "PARAM":
            # PARAM: vem de visitDecFuncao / visitParametros / visitListaParametros.
            # Ele já foi consumido no pré-passo (_scan_functions), então aqui
            # não geramos nada.
            return


        # ---------------- MOV ----------------
        # (poderia vir de otimizações ou reescritas internas – não está
        #  diretamente ligado a uma regra da gramática, é bem "IR genérico")
        if op == "MOV":
            self.emit(f"    {dest} = {a1};")
            return


        # ---------------- NOT ----------------
        # vem de:
        #   fator : NOT fator
        # visitFator gera "NOT" no IR.
        if op == "NOT":
            self.emit(f"    {dest} = !{a1};")
            return


        # ---------------- ARITMÉTICOS ----------------
        # vêm principalmente de:
        #   exprAditiva       → '+', '-'
        #   exprMultiplicativa→ '*', '/', '%'
        # visitExprAditiva / visitExprMultiplicativa:
        #   self.ir.emit(op, left, right, temp)        
        if op in ["+", "-", "*", "/", "%"]:
            self.emit(f"    {dest} = {a1} {op} {a2};")
            return


        # ---------------- RELACIONAIS ----------------
        # vêm de:
        #   exprRelacional
        # visitExprRelacional:
        #   self.ir.emit(op, left, right, temp)
        if op in ["<", "<=", ">", ">=", "==", "!="]:
            self.emit(f"    {dest} = ({a1} {op} {a2});")
            return


        # ---------------- LÓGICOS ----------------
        # vêm de:
        #   exprE   (AND → '&&')
        #   exprOu  (OR  → '||')
        # visitExprE / visitExprOu:
        #   self.ir.emit("&&"/"||", left, right, temp)
        if op in ["&&", "||"]:
            self.emit(f"    {dest} = ({a1} {op} {a2});")
            return


        # ---------------- LABEL ----------------
        # vem de:
        #   visitSelecao / visitEnquanto
        #   via ir.emit_label(Lx)
        if op == "LABEL":
            self.emit(f"{a1}:;")
            return


        # ---------------- GOTO ----------------
        # vem de:
        #   visitSelecao:
        #       GOTO ..., L_end
        #   visitEnquanto:
        #       GOTO ..., L_start
        if op == "GOTO":
            self.emit(f"    goto {dest};")
            return


        # ---------------- IF_TRUE (não usado) ----------------
        # exemplo típico: if (cond) goto label;
        if op == "IF_TRUE":
            self.emit(f"    if ({a1}) goto {dest};")
            return


        # ---------------- RETURN ----------------
        # vem de:
        #   visitRetorno (RETURN expressao PVIRG)
        #   visitDecFuncao (return implícito se void)
        #   visitPrincipal (RETURN None no fim de main)-
        if op == "RETURN":
            if a1 is None:
                self.emit("    return;")
            else:
                self.emit(f"    return {a1};")
            return


        # ---------------- FUNC_START ----------------
        # vem de:
        #   visitDecFuncao:
        #       self.ir.emit("FUNC_START", nome, ret_tipo, None)
        #   visitPrincipal:
        #       self.ir.emit("FUNC_START", "principal", "void", None)
        #
        # Aqui transformamos:
        #   - "principal" → int main(...)
        #   - retornais "boolean" → int-
        if op == "FUNC_START":
            nome = a1 or "func"
            ret_tipo = a2 or "void"
            if ret_tipo == "boolean":
                ret_tipo = "int"
            if nome == "principal":
                nome_c = "main"
                ret_tipo = "int"
            else:
                nome_c = nome

            # pega a lista de parâmetros dessa função
            params = self.func_params.get(nome, [])

            # monta "tipo nome" pra cada um
            params_c = ", ".join(f"{tipo} {nomep}" for tipo, nomep in params)
            self.emit(f"{ret_tipo} {nome_c}({params_c}) {{")
            return


        # ---------------- FUNC_END ----------------
        # vem de:
        #   visitDecFuncao
        #   visitPrincipal
        if op == "FUNC_END":
            self.emit("}")
            self.emit("")  # linha em branco
            return


        # ---------------- VAR_DECL ----------------
        # vem de:
        #   listaVariaveis
        #       : tipo listaId PVIRG
        #       | listaVariaveis tipo listaId PVIRG
        # visitListaVariaveis → self.ir.emit("VAR_DECL", idname, tipo, None)--
        if op == "VAR_DECL":
            tipo = a2 or "int"
            if tipo == "boolean":
                tipo = "int"
            nome = a1
            self.emit(f"    {tipo} {nome};")
            return


        # ---------------- LOAD_STR ----------------
        # vem de:
        #   visitEscrita quando TEXTO
        #   visitFator quando TEXTO
        if op == "LOAD_STR":
            self.emit(f"    const char* {dest} = {a1};")
            return


        # ---------------- LOAD_VAR ----------------
        # vem de:
        #   visitFator quando ID
        #   visitTermoEscrita quando ID
        #   visitAtribuicao/complemento/expressões em geral
        if op == "LOAD_VAR":
            self.emit(f"    {dest} = {a1}; // copiar variavel")
            return


        # ---------------- READ ----------------
        # vem de:
        #   leitura
        #   : SCANF PAREN1 listaTermoLeitura PAREN2 PVIRG
        # visitLeitura/visitTermoLeitura:
        #   self.ir.emit("READ", None, None, idname)
        if op == "READ":
            self.emit(f"    scanf(\"%d\", &{dest});")
            return
        

        # ---------------- ASSIGN ----------------
        # vem de:
        #   atribuicao
        #   : ID ATRIB complemento PVIRG
        # visitAtribuicao:
        #   self.ir.emit("ASSIGN", valor_temp, None, dest)
        if op == "ASSIGN":
            self.emit(f"    {dest} = {a1};")
            return


        # ---------------- LOAD_INT / LOAD_REAL ----------------
        # vêm de:
        #   constante
        #   : NUM_INT
        #   | NUM_DEC
        # visitConstante:
        #   self.ir.emit("LOAD_INT", NUM_INT, None, temp)
        #   self.ir.emit("LOAD_REAL", NUM_DEC, None, temp)
        if op == "LOAD_INT":
            self.emit(f"    {dest} = {a1};")
            return

        if op == "LOAD_REAL":
            self.emit(f"    {dest} = {a1};")
            return


        # ---------------- IF_FALSE_GOTO ----------------
        # vem de:
        #   visitSelecao (if / else)
        #   visitEnquanto (while)
        #   usando: self.ir.emit("IF_FALSE_GOTO", cond_temp, None, Lx)
        if op == "IF_FALSE_GOTO":
            self.emit(f"    if (!({a1})) goto {dest};")
            return


        # ---------------- ARG ----------------
        # vem de:
        #   visitChamadaFuncao / visitListaArgumentos:
        #       self.ir.emit("ARG", temp_arg, None, None)
        # Usamos um buffer pending_args até o CALL.
        if op == "ARG":
            # acumula argumentos para o próximo CALL
            if not hasattr(self, "pending_args"):
                self.pending_args = []
            self.pending_args.append(a1)
            return


        # ---------------- CALL ----------------
        # vem de:
        #   visitChamadaFuncao:
        #       self.ir.emit("CALL", nome, len(args), temp_dest)
        if op == "CALL":
            nome = a1
            nargs = a2 or 0
            args = []
            if hasattr(self, "pending_args"):
                # pega os últimos nargs argumentos
                args = self.pending_args[-nargs:]
                self.pending_args = self.pending_args[:-nargs]
            call_expr = f"{nome}({', '.join(args)})"
            if dest:
                self.emit(f"    {dest} = {call_expr};")
            else:
                self.emit(f"    {call_expr};")
            return


        # ---------------- WRITE ----------------
        # vem de:
        #   escrita
        #   : PRINTLN PAREN1 listaTermoEscrita PAREN2 PVIRG
        # visitEscrita:
        #   - strings → LOAD_STR + WRITE(temp_de_string)
        #   - outros  → WRITE(temp_ou_variável)
        #
        # Aqui escolhemos %s ou %d com base em string_temps
        if op == "WRITE":
            valor = a1
            if valor in self.string_temps:
                self.emit(f"    printf(\"%s\\n\", {valor});")
            else:
                self.emit(f"    printf(\"%d\\n\", {valor});")
            return


        # Se chegou aqui, instrução não reconhecida
        print(f"[AVISO] Instrução IR não mapeada no backend C: {op}")


    # --------------------------------------------------
    # Gera o código C final
    # --------------------------------------------------
    def generate(self):
        # Cabeçalho padrão
        self.emit("#include <stdio.h>")
        self.emit("")

        # Declara todos os temporários como int.
        # Esses temporários vêm das expressões da gramática
        # (expressao, exprOu, exprE, exprRelacional, exprAditiva, exprMultiplicativa, fator, constante, etc.)
        self.collect_temps()
        if self.temps:
            linha = "int " + ", ".join(sorted(self.temps)) + ";"
            self.emit(linha)
            self.emit("")

        # Traduz cada instrução IR (na ordem em que foi emitida pelo Visitor)
        for op, a1, a2, dest in self.ir:
            self.translate(op, a1, a2, dest)

        # Junta tudo em uma string
        return "\n".join(self.lines)

