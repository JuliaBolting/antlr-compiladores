from CompiladorVisitor import CompiladorVisitor
from CompiladorParser import CompiladorParser

class CodeGenVisitor(CompiladorVisitor):
    def __init__(self, ir):
        self.ir = ir

    # ---------------------------------------
    # PROGRAM
    # ---------------------------------------

    def visitPrograma(self, ctx):
        # Tipos e variáveis globais (se existirem)
        self.visit(ctx.declaracoesTipos())
        if ctx.secaoVariaveis():
            self.visit(ctx.secaoVariaveis())

        # Funções
        self.visit(ctx.secaoFuncoes())

        # Principal
        self.visit(ctx.principal())
        return self.ir.code

    # ---------------------------------------
    # TIPOS
    # ---------------------------------------

    def visitDeclaracoesTipos(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclaracaoTipo(self, ctx):
        return self.visitChildren(ctx)

    def visitCampoRegistro(self, ctx):
        return self.visitChildren(ctx)

    # ---------------------------------------
    # VARIÁVEIS
    # ---------------------------------------

    def visitSecaoVariaveis(self, ctx):
        for lista in ctx.listaVariaveis():
            self.visit(lista)
        return None

    def visitListaVariaveis(self, ctx):
        tipo = ctx.tipo().getText()
        for ID in ctx.ID():
            self.ir.emit("VAR_DECL", ID.getText(), tipo, None)
        return None

    # ---------------------------------------
    # FUNÇÕES
    # ---------------------------------------

    def visitSecaoFuncoes(self, ctx):
        for f in ctx.decFuncao():
            self.visit(f)
        return None

    def visitDecFuncao(self, ctx):
        nome = ctx.ID().getText()
        self.ir.emit("FUNC_START", nome, None, None)

        # parâmetros
        if ctx.parametros():
            for p in ctx.parametros().param():
                tipo = p.tipo().getText()
                nome_param = p.ID().getText()
                self.ir.emit("PARAM", nome_param, tipo, None)

        # corpo
        self.visit(ctx.bloco())

        # garante retorno automático
        self.ir.emit("RETURN", None, None, None)

        self.ir.emit("FUNC_END", nome, None, None)
        return None

    # ---------------------------------------
    # PRINCIPAL
    # ---------------------------------------

    def visitPrincipal(self, ctx):
        self.ir.emit("FUNC_START", "principal", None, None)
        self.visit(ctx.bloco())
        self.ir.emit("RETURN", None, None, None)
        self.ir.emit("FUNC_END", "principal", None, None)
        return None

    # ---------------------------------------
    # BLOCOS / COMANDOS
    # ---------------------------------------

    def visitBloco(self, ctx):
        for cmd in ctx.comando():
            self.visit(cmd)
        return None

    def visitComando(self, ctx):
        return self.visitChildren(ctx)

    # ---------------------------------------
    # ATRIBUIÇÃO
    # ---------------------------------------

    def visitAtribuicao(self, ctx):
        ID = ctx.ID().getText()
        expr_val = self.visit(ctx.expr())
        self.ir.emit("ASSIGN", expr_val, None, ID)
        return None

    # ---------------------------------------
    # LEITURA / ESCRITA
    # ---------------------------------------

    def visitLeitura(self, ctx):
        ID = ctx.ID().getText()
        self.ir.emit("READ", None, None, ID)
        return None

    def visitEscrita(self, ctx):
        val = self.visit(ctx.expr())
        self.ir.emit("WRITE", val, None, None)
        return None

    # ---------------------------------------
    # IF / ELSE
    # ---------------------------------------

    def visitSelecao(self, ctx):
        cond_val = self.visit(ctx.expr())

        L_false = self.ir.new_label()
        L_end = self.ir.new_label()

        self.ir.emit("IF_FALSE_GOTO", cond_val, None, L_false)

        for c in ctx.comando():
            self.visit(c)

        if ctx.SENAO():
            self.ir.emit("GOTO", None, None, L_end)

        self.ir.emit_label(L_false)

        if ctx.SENAO():
            for c in ctx.elseBloc.comando():
                self.visit(c)
            self.ir.emit_label(L_end)

        return None

    # ---------------------------------------
    # ENQUANTO (WHILE)
    # ---------------------------------------

    def visitEnquanto(self, ctx):
        L_start = self.ir.new_label()
        L_end = self.ir.new_label()

        self.ir.emit_label(L_start)

        cond = self.visit(ctx.expr())
        self.ir.emit("IF_FALSE_GOTO", cond, None, L_end)

        for c in ctx.comando():
            self.visit(c)

        self.ir.emit("GOTO", None, None, L_start)
        self.ir.emit_label(L_end)

        return None

    # ---------------------------------------
    # RETURN
    # ---------------------------------------

    def visitRetorno(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.ir.emit("RETURN", val, None, None)
        else:
            self.ir.emit("RETURN", None, None, None)
        return None

    # ---------------------------------------
    # CHAMADA DE FUNÇÃO
    # ---------------------------------------

    def visitChamadaFuncao(self, ctx):
        nome = ctx.ID().getText()

        args = []
        if ctx.listaArgumentos():
            for e in ctx.listaArgumentos().expr():
                args.append(self.visit(e))

        for a in args:
            self.ir.emit("ARG", a, None, None)

        temp = self.ir.new_temp()
        self.ir.emit("CALL", nome, len(args), temp)
        return temp

    # ---------------------------------------
    # EXPRESSÕES
    # ---------------------------------------

    # Soma/Subtração
    def visitExprAddSub(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.termo())
        op = ctx.op.text
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp

    # Termo sozinho
    def visitExprTermo(self, ctx):
        return self.visit(ctx.termo())

    # Multiplicação/Divisão
    def visitTermoMulDiv(self, ctx):
        left = self.visit(ctx.termo())
        right = self.visit(ctx.fator())
        op = ctx.op.text
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp

    # Fator sozinho
    def visitTermoFator(self, ctx):
        return self.visit(ctx.fator())

    # ---------------------------------------
    # FATORES (LITERALS / ID / PARÊNTESES)
    # ---------------------------------------

    def visitFator(self, ctx):
        if ctx.NUM_INT():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_INT", ctx.NUM_INT().getText(), None, temp)
            return temp

        if ctx.NUM_REAL():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_REAL", ctx.NUM_REAL().getText(), None, temp)
            return temp

        if ctx.ID():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_VAR", ctx.ID().getText(), None, temp)
            return temp

        if ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())

        if ctx.expr():
            return self.visit(ctx.expr())

        raise Exception("Fator inválido!")

    # ---------------------------------------
    # DEFAULT
    # ---------------------------------------

    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            result = self.visit(node.getChild(i))
        return result
