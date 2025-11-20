from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
from IR import IRCode

class CodeGenVisitor(ExprVisitor):

    def __init__(self, ir: IRCode = None):
        self.ir = ir if ir is not None else IRCode()


    # -----------------------------
    # programa : secaoFuncoes principal EOF
    # -----------------------------
    def visitPrograma(self, ctx:ExprParser.ProgramaContext):
        # funções (se houver)
        if ctx.secaoFuncoes():
            self.visit(ctx.secaoFuncoes())
        # principal
        self.visit(ctx.principal())
        return self.ir


    # -----------------------------------------
    # secaoFuncoes
    # secaoFuncoes
    #     : listaFuncoes
    #     | /* vazio */
    # -----------------------------------------
    def visitSecaoFuncoes(self, ctx:ExprParser.SecaoFuncoesContext):
        if ctx.listaFuncoes():
            self.visit(ctx.listaFuncoes())
        return None


    # -----------------------------------------
    # parametros
    # parametros
    #     : listaParametros
    #     | /* vazio */
    # -----------------------------------------
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        # parametros : listaParametros | vazio
        if ctx.listaParametros():
            return self.visit(ctx.listaParametros())
        return []  # sem parâmetros


    # -----------------------------------------
    # listaParametros
    # listaParametros
    #     : tipo ID
    #     | listaParametros VIRG tipo ID
    # -----------------------------------------
    def visitListaParametros(self, ctx:ExprParser.ListaParametrosContext):
        if ctx.getChildCount() == 2:
            # caso base: tipo ID
            tipo = ctx.tipo().getText()
            nome = ctx.ID().getText()
            return [(nome, tipo)]
        else:
            # caso recursivo: listaParametros VIRG tipo ID
            prev = self.visit(ctx.listaParametros())
            tipo = ctx.tipo().getText()
            nome = ctx.ID().getText()
            return prev + [(nome, tipo)]


    # -----------------------------------------
    # listaFuncoes
    # listaFuncoes
    #     : decFuncao
    #     | listaFuncoes decFuncao
    # -----------------------------------------
    def visitListaFuncoes(self, ctx:ExprParser.ListaFuncoesContext):
        # Caso base: só 1 função
        if ctx.decFuncao() and not ctx.listaFuncoes():
            self.visit(ctx.decFuncao())
        # Caso recursivo: listaFuncoes decFuncao
        else:
            if ctx.listaFuncoes():
                self.visit(ctx.listaFuncoes())
            if ctx.decFuncao():
                self.visit(ctx.decFuncao())
        return None


    # -----------------------------------------
    # decFuncao
    # decFuncao
    #     : tipoRetorno ID PAREN1 parametros PAREN2 bloco
    # -----------------------------------------
    def visitDecFuncao(self, ctx:ExprParser.DecFuncaoContext):
        nome = ctx.ID().getText()
        ret_tipo = ctx.tipoRetorno().getText()

        self.ir.emit("FUNC_START", nome, ret_tipo, None)

        # parâmetros
        params = []
        if ctx.parametros():
            params = self.visit(ctx.parametros())
        for p_name, p_type in params:
            self.ir.emit("PARAM", p_name, p_type, None)

        # corpo
        self.visit(ctx.bloco())

        # só põe return implícito se for void
        if ret_tipo == "void":
            self.ir.emit("RETURN", None, None, None)

        self.ir.emit("FUNC_END", nome, None, None)
        return None


    # -----------------------------------------
    # principal
    # principal
    #     : MAIN PAREN1 PAREN2 bloco
    # -----------------------------------------
    def visitPrincipal(self, ctx:ExprParser.PrincipalContext):
        self.ir.emit("FUNC_START", "principal", "void", None)
        self.visit(ctx.bloco())
        self.ir.emit("RETURN", None, None, None)
        self.ir.emit("FUNC_END", "principal", None, None)
        return None


    # -----------------------------------------
    # bloco
    # bloco
    #     : CHAVE1 secaoVariaveis secaoComandos CHAVE2
    # -----------------------------------------
    def visitBloco(self, ctx:ExprParser.BlocoContext):
        if ctx.secaoVariaveis():
            self.visit(ctx.secaoVariaveis())
        if ctx.secaoComandos():
            self.visit(ctx.secaoComandos())
        return None


    # -----------------------------------------
    # secaoVariaveis
    # secaoVariaveis
    #     : listaVariaveis
    #     | /* vazio */
    # -----------------------------------------
    def visitSecaoVariaveis(self, ctx:ExprParser.SecaoVariaveisContext):
        if ctx.listaVariaveis():
            self.visit(ctx.listaVariaveis())
        return None


    # -----------------------------------------
    # listaVariaveis
    # listaVariaveis
    #     : tipo listaId PVIRG
    #     | listaVariaveis tipo listaId PVIRG
    # -----------------------------------------
    def visitListaVariaveis(self, ctx:ExprParser.ListaVariaveisContext):
        # primeiro, visita as declarações anteriores (se houver)
        if ctx.listaVariaveis():
            self.visit(ctx.listaVariaveis())

        # depois, trata o "tipo listaId PVIRG" atual
        tipo = ctx.tipo().getText()
        ids = self.visit(ctx.listaId())
        for idname in ids:
            self.ir.emit("VAR_DECL", idname, tipo, None)
        return None


    # -----------------------------------------
    # listaId
    # listaId
    #     : ID
    #     | listaId VIRG ID
    # -----------------------------------------
    def visitListaId(self, ctx:ExprParser.ListaIdContext):
        if ctx.getChildCount() == 1:
            return [ ctx.ID().getText() ]
        else:
            left = self.visit(ctx.listaId())
            right = ctx.ID().getText()
            return left + [ right ]


    # -----------------------------------------
    # secaoComandos
    # secaoComandos
    #     : listaComandos
    #     | /* vazio */
    # -----------------------------------------
    def visitSecaoComandos(self, ctx:ExprParser.SecaoComandosContext):
        if ctx.listaComandos():
            self.visit(ctx.listaComandos())
        return None


    # -----------------------------------------
    # listaComandos
    # listaComandos
    #     : comando
    #     | listaComandos comando
    # -----------------------------------------
    def visitListaComandos(self, ctx:ExprParser.ListaComandosContext):
        return self.visitChildren(ctx)


    # -----------------------------------------
    # comando
    # comando
    #     : leitura
    #     | escrita
    #     | atribuicao
    #     | chamadaFuncao
    #     | selecao
    #     | enquanto
    #     | retorno
    # -----------------------------------------
    def visitComando(self, ctx:ExprParser.ComandoContext):
        if ctx.leitura():
            return self.visit(ctx.leitura())
        if ctx.escrita():
            return self.visit(ctx.escrita())
        if ctx.atribuicao():
            return self.visit(ctx.atribuicao())
        if ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        if ctx.selecao():
            return self.visit(ctx.selecao())
        if ctx.enquanto():
            return self.visit(ctx.enquanto())
        if ctx.retorno():
            return self.visit(ctx.retorno())
        return None


    # -----------------------------------------
    # leitura
    # leitura
    #     : SCANF PAREN1 listaTermoLeitura PAREN2 PVIRG
    # -----------------------------------------
    def visitLeitura(self, ctx:ExprParser.LeituraContext):
        # vamos extrair IDs via visita
        ids = self.visit(ctx.listaTermoLeitura())
        for idname in ids:
            self.ir.emit("READ", None, None, idname)
        return None


    # -----------------------------------------
    # listaTermoLeitura
    # listaTermoLeitura
    #     : termoLeitura
    #     | listaTermoLeitura VIRG termoLeitura
    # -----------------------------------------
    def visitListaTermoLeitura(self, ctx:ExprParser.ListaTermoLeituraContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termoLeitura())
        else:
            left = self.visit(ctx.listaTermoLeitura())
            right = self.visit(ctx.termoLeitura())
            return left + right


    # -----------------------------------------
    # termoLeitura
    # termoLeitura
    #     : ID dimensao2
    # -----------------------------------------
    def visitTermoLeitura(self, ctx:ExprParser.TermoLeituraContext):
        return [ ctx.ID().getText() ]


    # -----------------------------------------
    # escrita
    # escrita
    #     : PRINTLN PAREN1 listaTermoEscrita PAREN2 PVIRG
    # -----------------------------------------
    def visitEscrita(self, ctx:ExprParser.EscritaContext):
        terms = self.visit(ctx.listaTermoEscrita())
        for t in terms:
            if isinstance(t, str) and t.startswith('"') and t.endswith('"'):
                temp = self.ir.new_temp()
                self.ir.emit("LOAD_STR", t, None, temp)
                self.ir.emit("WRITE", temp, None, None)
            else:
                self.ir.emit("WRITE", t, None, None)
        return None


    # -----------------------------------------
    # listaTermoEscrita
    # listaTermoEscrita
    #     : termoEscrita
    #     | listaTermoEscrita VIRG termoEscrita
    # -----------------------------------------
    def visitListaTermoEscrita(self, ctx:ExprParser.ListaTermoEscritaContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termoEscrita())
        else:
            left = self.visit(ctx.listaTermoEscrita())
            right = self.visit(ctx.termoEscrita())
            return left + right


    # -----------------------------------------
    # termoEscrita
    # termoEscrita
    #     : ID dimensao2
    #     | constante
    #     | TEXTO
    # -----------------------------------------
    def visitTermoEscrita(self, ctx:ExprParser.TermoEscritaContext):
        if ctx.ID():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_VAR", ctx.ID().getText(), None, temp)
            return [temp]
        if ctx.constante():
            val = self.visit(ctx.constante())
            return [val]
        if ctx.TEXTO():
            return [ ctx.TEXTO().getText() ]


    # -----------------------------------------
    # atribuicao
    # atribuicao
    #     : ID ATRIB complemento PVIRG
    # -----------------------------------------
    def visitAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        dest = ctx.ID().getText()
        val = self.visit(ctx.complemento())
        self.ir.emit("ASSIGN", val, None, dest)
        return None


    # -----------------------------------------
    # complemento
    # complemento
    #     : expressao
    #     | chamadaFuncao
    # -----------------------------------------
    def visitComplemento(self, ctx:ExprParser.ComplementoContext):
        if ctx.expressao():
            return self.visit(ctx.expressao())
        if ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        return None


    # -----------------------------------------
    # chamadaFuncao
    # chamadaFuncao
    #     : FUNC ID PAREN1 argumentos PAREN2
    # -----------------------------------------
    def visitChamadaFuncao(self, ctx:ExprParser.ChamadaFuncaoContext):
        nome = ctx.ID().getText()
        args = []
        if ctx.argumentos() and ctx.argumentos().listaArgumentos():
            args = self.visit(ctx.argumentos().listaArgumentos())
        for a in args:
            self.ir.emit("ARG", a, None, None)
        temp = self.ir.new_temp()
        self.ir.emit("CALL", nome, len(args), temp)
        return temp


    # -----------------------------------------
    # argumentos
    # argumentos
    #     : listaArgumentos
    #     | /* vazio */
    # -----------------------------------------
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        if ctx.listaArgumentos():
            return self.visit(ctx.listaArgumentos())
        return []


    # -----------------------------------------
    # listaArgumentos
    # listaArgumentos
    #     : expressao
    #     | listaArgumentos VIRG expressao
    # -----------------------------------------
    def visitListaArgumentos(self, ctx:ExprParser.ListaArgumentosContext):
        if ctx.getChildCount() == 1:
            return [ self.visit(ctx.expressao()) ]
        else:
            left = self.visit(ctx.listaArgumentos())
            right = self.visit(ctx.expressao())
            return left + [ right ]


    # -----------------------------------------
    # retorno
    # retorno
    #     : RETURN expressao PVIRG
    # -----------------------------------------
    def visitRetorno(self, ctx:ExprParser.RetornoContext):
        val = self.visit(ctx.expressao())
        self.ir.emit("RETURN", val, None, None)
        return None


    # -----------------------------------------
    # retorno
    # retorno
    #     : RETURN expressao PVIRG
    # -----------------------------------------
    def visitSelecao(self, ctx:ExprParser.SelecaoContext):
        cond_temp = self.visit(ctx.expressao())

        L_false = self.ir.new_label()
        L_end = self.ir.new_label()

        # if not cond goto L_false
        self.ir.emit("IF_FALSE_GOTO", cond_temp, None, L_false)

        # então
        self.visit(ctx.bloco())

        # se tiver senao, pular pro fim
        if ctx.senao() and ctx.senao().ELSE():
            self.ir.emit("GOTO", None, None, L_end)

        # label false (inicio do else)
        self.ir.emit_label(L_false)

        if ctx.senao() and ctx.senao().bloco():
            self.visit(ctx.senao().bloco())

        # label end
        if ctx.senao() and ctx.senao().ELSE():
            self.ir.emit_label(L_end)

        return None

    # -----------------------------------------
    # enquanto
    # enquanto
    #     : WHILE PAREN1 expressao PAREN2 bloco
    # -----------------------------------------
    def visitEnquanto(self, ctx:ExprParser.EnquantoContext):
        L_start = self.ir.new_label()
        L_end = self.ir.new_label()

        self.ir.emit_label(L_start)
        cond = self.visit(ctx.expressao())
        self.ir.emit("IF_FALSE_GOTO", cond, None, L_end)

        self.visit(ctx.bloco())

        self.ir.emit("GOTO", None, None, L_start)
        self.ir.emit_label(L_end)
        return None


    # -----------------------------------------
    # expressao
    # expressao
    #     : exprOu
    # -----------------------------------------
    def visitExpressao(self, ctx:ExprParser.ExpressaoContext):
        return self.visit(ctx.exprOu())


    # -----------------------------------------
    # exprOu
    # exprOu
    #     : exprE
    #     | exprOu OR exprE
    # -----------------------------------------
    def visitExprOu(self, ctx:ExprParser.ExprOuContext):
        # Caso base: só exprE
        if ctx.exprOu() is None:
            return self.visit(ctx.exprE())

        # Caso recursivo: exprOu OR exprE
        left = self.visit(ctx.exprOu())
        right = self.visit(ctx.exprE())
        temp = self.ir.new_temp()
        self.ir.emit("||", left, right, temp)
        return temp


    # -----------------------------------------
    # exprE
    # exprE
    #     : exprRelacional
    #     | exprE AND exprRelacional
    # -----------------------------------------
    def visitExprE(self, ctx:ExprParser.ExprEContext):
        if ctx.exprE() is None:
            return self.visit(ctx.exprRelacional())

        left = self.visit(ctx.exprE())
        right = self.visit(ctx.exprRelacional())
        temp = self.ir.new_temp()
        self.ir.emit("&&", left, right, temp)
        return temp


    # -----------------------------------------
    # exprRelacional
    # exprRelacional
    #     : exprAditiva
    #     | exprAditiva opRelacional exprAditiva
    #
    # opRelacional
    #     : LT | LE | GT | GE | EQ | NEQ
    # -----------------------------------------
    def visitExprRelacional(self, ctx:ExprParser.ExprRelacionalContext):
        if ctx.opRelacional() is None:
            return self.visit(ctx.exprAditiva(0))

        left = self.visit(ctx.exprAditiva(0))
        right = self.visit(ctx.exprAditiva(1))
        op = ctx.opRelacional().getText()  # <, <=, >, >=, ==, !=
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp


    # -----------------------------------------
    # exprAditiva
    # exprAditiva
    #     : exprMultiplicativa
    #     | exprAditiva opAditivo exprMultiplicativa
    #
    # opAditivo
    #     : SOMA | SUB
    # -----------------------------------------
    def visitExprAditiva(self, ctx:ExprParser.ExprAditivaContext):
        # Caso base: só um exprMultiplicativa
        if ctx.exprAditiva() is None:
            return self.visit(ctx.exprMultiplicativa())

        # Caso recursivo: exprAditiva opAditivo exprMultiplicativa
        left = self.visit(ctx.exprAditiva())
        right = self.visit(ctx.exprMultiplicativa())
        op = ctx.opAditivo().getText()   # '+' ou '-'
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp


    # -----------------------------------------
    # exprMultiplicativa
    # exprMultiplicativa
    #     : fator
    #     | exprMultiplicativa opMultiplicativo fator
    #
    # opMultiplicativo
    #     : MUL | DIV | RESTO
    # -----------------------------------------
    def visitExprMultiplicativa(self, ctx:ExprParser.ExprMultiplicativaContext):
        # Caso base: só um fator
        if ctx.exprMultiplicativa() is None:
            return self.visit(ctx.fator())

        # Caso recursivo: exprMultiplicativa opMultiplicativo fator
        left = self.visit(ctx.exprMultiplicativa())
        right = self.visit(ctx.fator())
        op = ctx.opMultiplicativo().getText()   # '*', '/', '%'
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp


    # -----------------------------------------
    # fator
    # fator
    #     : sinal ID dimensao2
    #     | sinal constante
    #     | TEXTO
    #     | NOT fator
    #     | PAREN1 expressao PAREN2
    # -----------------------------------------
    def visitFator(self, ctx:ExprParser.FatorContext):
        if ctx.TEXTO():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_STR", ctx.TEXTO().getText(), None, temp)
            return temp

        # NOT fator
        if ctx.NOT():
            val = self.visit(ctx.fator())
            temp = self.ir.new_temp()
            self.ir.emit("NOT", val, None, temp)
            return temp

        # parenteses
        if ctx.PAREN1():
            return self.visit(ctx.expressao())

        # sinal + ID dimensao2  OR sinal constante
        if ctx.ID():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_VAR", ctx.ID().getText(), None, temp)
            if ctx.sinal() and ctx.sinal().SOMA():
                return temp
            if ctx.sinal() and ctx.sinal().SUB():
                t2 = self.ir.new_temp()
                self.ir.emit("-", "0", temp, t2)
                return t2
            return temp

        # constante
        if ctx.constante():
            c = self.visit(ctx.constante())
            if ctx.sinal() and ctx.sinal().SUB():
                t2 = self.ir.new_temp()
                self.ir.emit("-", "0", c, t2)
                return t2
            return c

        raise Exception("Fator inválido!")


    # -----------------------------------------
    # constante
    # constante
    #     : NUM_INT
    #     | NUM_DEC
    # -----------------------------------------
    def visitConstante(self, ctx:ExprParser.ConstanteContext):
        # NUM_INT | NUM_DEC
        if ctx.NUM_INT():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_INT", ctx.NUM_INT().getText(), None, temp)
            return temp
        if ctx.NUM_DEC():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_REAL", ctx.NUM_DEC().getText(), None, temp)
            return temp
        return None


    # -----------------------------------------
    # sinal
    # sinal
    #     : SOMA
    #     | SUB
    #     | /* vazio */
    # -----------------------------------------
    def visitSinal(self, ctx:ExprParser.SinalContext):
        # Não geramos IR aqui.
        # Quem interpreta o sinal (unário + ou -) é o visitFator,
        # verificando ctx.sinal().SOMA() / ctx.sinal().SUB().
        return None


    # -----------------------------------------
    # fallback padrão
    # percorre filhos genéricos de qualquer regra
    # -----------------------------------------
    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            try:
                result = self.visit(child)
            except AttributeError:
                # tokens simples não têm 'accept/visit'
                pass
        return result

