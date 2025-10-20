from ExprListener import ExprListener
import re

class SymbolListener(ExprListener):
    def __init__(self):
        # Tabela de símbolos: [(id, nome, tipo, escopo, offset)]
        self.symbols = []
        self.functions = {}
        self.errors = []
        self.context = "global"
        self.current_function = None
        self.offset = 0
        self.id_counter = 0
        
    def add_symbol(self, name, tipo):
        if self.is_declared_in_scope(name, self.context):
            self.errors.append(f"Variável '{name}' já declarada em {self.context}.")
            return
        
        match = re.match(r'(\w+)\[(\d+)\]', tipo)
        if match:
            base_tipo = match.group(1)
            tamanho = int(match.group(2))
            width = self.get_width(base_tipo) * tamanho
        else:
            width = self.get_width(tipo)
        
        self.symbols.append((self.id_counter, name, tipo, self.context, self.offset))
        self.id_counter += 1
        self.offset += width

    def lookup(self, name):
        for s in reversed(self.symbols):
            if s[1] == name:
                return s
        return None

    def is_declared_in_scope(self, name, scope):
        return any(s[1] == name and s[3] == scope for s in self.symbols)

    def get_width(self, tipo):
        return {"int": 4, "float": 8, "char": 1, "boolean": 1}.get(tipo, 4)

    def infer_type(self, expr_text):
        if '"' in expr_text:
            return "char"
        if "." in expr_text:
            return "float"
        if expr_text.isdigit():
            return "int"
        if expr_text in ["true", "false"]:
            return "boolean"
        return None


    def exitListaVariaveis(self, ctx):
        tipo_ctx = ctx.tipo()
        if not tipo_ctx:
            return
        tipo = tipo_ctx.getText()
        ids = ctx.listaId().getText().split(',')
        for ident in ids:
            self.add_symbol(ident.strip(), tipo)


    def exitDecFuncao(self, ctx):
        nome = ctx.ID().getText()
        tipo_retorno = getattr(ctx, 'tipoRetorno', None)
        tipo_retorno = tipo_retorno.getText() if tipo_retorno else "void"

        if nome in self.functions:
            self.errors.append(f"Função '{nome}' já declarada.")
            return

        self.functions[nome] = {"retorno": tipo_retorno, "params": []}
        self.context = nome
        self.current_function = nome
        self.offset = 0


    def exitParametros(self, ctx):
        if getattr(ctx, 'listaParametros', None):
            params = ctx.listaParametros().getText().split(',')
            for p in params:
                tipo, nome = p.strip().split()
                self.add_symbol(nome, tipo)
                self.functions[self.current_function]["params"].append(tipo)


    def enterPrincipal(self, ctx):
        self.context = "main"
        self.current_function = "main"
        self.offset = 0


    def exitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        symbol = self.lookup(nome)

        if not symbol:
            self.errors.append(f"Variável '{nome}' usada sem declaração.")
            return

        tipo_var = symbol[2]
        expr_text = ctx.complemento().getText() if hasattr(ctx, 'complemento') else ""
        tipo_expr = self.infer_type(expr_text)

        if tipo_expr and tipo_var != tipo_expr:
            if tipo_var == "float" and tipo_expr == "int":
                pass
            else:
                self.errors.append(f"Tipo incompatível: '{nome}' é {tipo_var}, mas expressão é {tipo_expr}.")


    def exitFator(self, ctx):
        if ctx.ID():
            var = self.lookup(ctx.ID().getText())
            if var:
                ctx.tipo = var[2]
            else:
                ctx.tipo = "error"
                self.errors.append(f"Variável '{ctx.ID().getText()}' não declarada.")
        elif ctx.constante():
            self.exitConstante(ctx.constante())
        elif ctx.TEXTO():
            ctx.tipo = "char"
        elif ctx.expressao():
            ctx.tipo = getattr(ctx.expressao(), "tipo", "unknown")
        else:
            ctx.tipo = "unknown"


    def exitConstante(self, ctx):
        if ctx.NUM_INT():
            ctx.tipo = "int"
        elif ctx.NUM_DEC():
            ctx.tipo = "float"
        else:
            ctx.tipo = "unknown"


    def exitPrograma(self, ctx):
        print("\n=== TABELA DE SÍMBOLOS ===")
        print(f"{'ID':>3} | {'Nome':10} | {'Tipo':8} | {'Escopo':10} | {'Offset':>6}")
        print("-" * 45)
        for s in self.symbols:
            print(f"{s[0]:>3} | {s[1]:10} | {s[2]:8} | {s[3]:10} | {s[4]:>6}")

        print("\n=== FUNÇÕES ===")
        for f, info in self.functions.items():
            print(f"{f}({', '.join(info['params'])}) -> {info['retorno']}")

        if self.errors:
            print("\nERROS SEMÂNTICOS:")
            for e in self.errors:
                print(" -", e)
        else:
            print("\nNenhum erro semântico encontrado.")
