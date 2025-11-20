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

    # -----------------------------
    # secaoFuncoes -> listaFuncoes
    # -----------------------------
    def visitSecaoFuncoes(self, ctx:ExprParser.SecaoFuncoesContext):
        if ctx.listaFuncoes():
            self.visit(ctx.listaFuncoes())
        return None

    def visitListaFuncoes(self, ctx:ExprParser.ListaFuncoesContext):
        # regra recursiva: decFuncao (listaFuncoes decFuncao)*
        # we can rely on visitChildren
        return self.visitChildren(ctx)

    def visitDecFuncao(self, ctx:ExprParser.DecFuncaoContext):
        nome = ctx.ID().getText()
        self.ir.emit("FUNC_START", nome, None, None)

        # parâmetros (se houver)
        if ctx.parametros() and ctx.parametros().listaParametros():
            params = self.visit(ctx.parametros().listaParametros())
            for p_name, p_type in params:
                # registra parâmetro (nome, tipo)
                self.ir.emit("PARAM", p_name, p_type, None)

        # corpo da função (bloco)
        self.visit(ctx.bloco())

        # retorno implícito se necessário
        self.ir.emit("RETURN", None, None, None)
        self.ir.emit("FUNC_END", nome, None, None)
        return None

    # -----------------------------
    # principal
    # -----------------------------
    def visitPrincipal(self, ctx:ExprParser.PrincipalContext):
        self.ir.emit("FUNC_START", "principal", None, None)
        self.visit(ctx.bloco())
        self.ir.emit("RETURN", None, None, None)
        self.ir.emit("FUNC_END", "principal", None, None)
        return None

    # -----------------------------
    # blocos / variáveis
    # -----------------------------
    def visitBloco(self, ctx:ExprParser.BlocoContext):
        # CHAVE1 secaoVariaveis secaoComandos CHAVE2
        if ctx.secaoVariaveis():
            self.visit(ctx.secaoVariaveis())
        if ctx.secaoComandos():
            self.visit(ctx.secaoComandos())
        return None

    def visitSecaoVariaveis(self, ctx:ExprParser.SecaoVariaveisContext):
        if ctx.listaVariaveis():
            self.visit(ctx.listaVariaveis())
        return None

    def visitListaVariaveis(self, ctx:ExprParser.ListaVariaveisContext):
        # cada listaVariaveis tem tipo listaId PVIRG (ou recursivo)
        tipo = ctx.tipo().getText()
        ids = self.visit(ctx.listaId())
        for idname in ids:
            self.ir.emit("VAR_DECL", idname, tipo, None)
        return None

    def visitListaId(self, ctx:ExprParser.ListaIdContext):
        # listaId : ID | listaId VIRG ID
        if ctx.getChildCount() == 1:
            return [ ctx.ID().getText() ]
        else:
            # esquerda é outra listaId
            left = self.visit(ctx.listaId())
            right = ctx.ID().getText()
            return left + [ right ]

    # -----------------------------
    # secaoComandos / listaComandos / comando
    # -----------------------------
    def visitSecaoComandos(self, ctx:ExprParser.SecaoComandosContext):
        if ctx.listaComandos():
            self.visit(ctx.listaComandos())
        return None

    def visitListaComandos(self, ctx:ExprParser.ListaComandosContext):
        # recursiva: listaComandos comando | comando
        return self.visitChildren(ctx)

    def visitComando(self, ctx:ExprParser.ComandoContext):
        # comando: leitura | escrita | atribuicao | chamadaFuncao | selecao | enquanto | retorno
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

    # -----------------------------
    # leitura / escrita
    # -----------------------------
    def visitLeitura(self, ctx:ExprParser.LeituraContext):
        # SCANF PAREN1 listaTermoLeitura PAREN2 PVIRG
        # listaTermoLeitura -> terras com IDs e dimensao2
        # vamos extrair IDs via visita
        ids = self.visit(ctx.listaTermoLeitura())
        for idname in ids:
            self.ir.emit("READ", None, None, idname)
        return None

    def visitListaTermoLeitura(self, ctx:ExprParser.ListaTermoLeituraContext):
        # recursiva: listaTermoLeitura , termoLeitura | termoLeitura
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termoLeitura())
        else:
            left = self.visit(ctx.listaTermoLeitura())
            right = self.visit(ctx.termoLeitura())
            return left + right

    def visitTermoLeitura(self, ctx:ExprParser.TermoLeituraContext):
        # termoLeitura : ID dimensao2
        return [ ctx.ID().getText() ]

    def visitEscrita(self, ctx:ExprParser.EscritaContext):
        # PRINTLN PAREN1 listaTermoEscrita PAREN2 PVIRG
        terms = self.visit(ctx.listaTermoEscrita())
        for t in terms:
            if isinstance(t, str) and t.startswith('"') and t.endswith('"'):
                # string literal already
                temp = self.ir.new_temp()
                self.ir.emit("LOAD_STR", t, None, temp)
                self.ir.emit("WRITE", temp, None, None)
            else:
                # t is a temp or literal
                self.ir.emit("WRITE", t, None, None)
        return None

    def visitListaTermoEscrita(self, ctx:ExprParser.ListaTermoEscritaContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termoEscrita())
        else:
            left = self.visit(ctx.listaTermoEscrita())
            right = self.visit(ctx.termoEscrita())
            return left + right

    def visitTermoEscrita(self, ctx:ExprParser.TermoEscritaContext):
        # ID dimensao2 | constante | TEXTO
        if ctx.ID():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_VAR", ctx.ID().getText(), None, temp)
            return [temp]
        if ctx.constante():
            val = self.visit(ctx.constante())
            # visit_constante returns a temp
            return [val]
        if ctx.TEXTO():
            return [ ctx.TEXTO().getText() ]

    # -----------------------------
    # atribuicao
    # -----------------------------
    def visitAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        # ID ATRIB complemento PVIRG
        dest = ctx.ID().getText()
        val = self.visit(ctx.complemento())
        # complemento can be function call (returns temp) or expression (returns temp)
        self.ir.emit("ASSIGN", val, None, dest)
        return None

    def visitComplemento(self, ctx:ExprParser.ComplementoContext):
        if ctx.expressao():
            return self.visit(ctx.expressao())
        if ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        return None

    # -----------------------------
    # chamada de função
    # -----------------------------
    def visitChamadaFuncao(self, ctx:ExprParser.ChamadaFuncaoContext):
        # FUNC ID PAREN1 argumentos PAREN2
        nome = ctx.ID().getText()
        args = []
        if ctx.argumentos() and ctx.argumentos().listaArgumentos():
            args = self.visit(ctx.argumentos().listaArgumentos())
        # push args
        for a in args:
            self.ir.emit("ARG", a, None, None)
        temp = self.ir.new_temp()
        self.ir.emit("CALL", nome, len(args), temp)
        return temp

    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        if ctx.listaArgumentos():
            return self.visit(ctx.listaArgumentos())
        return []

    def visitListaArgumentos(self, ctx:ExprParser.ListaArgumentosContext):
        # listaArgumentos : expressao | listaArgumentos VIRG expressao
        if ctx.getChildCount() == 1:
            return [ self.visit(ctx.expressao()) ]
        else:
            left = self.visit(ctx.listaArgumentos())
            right = self.visit(ctx.expressao())
            return left + [ right ]

    # -----------------------------
    # retorno
    # -----------------------------
    def visitRetorno(self, ctx:ExprParser.RetornoContext):
        # RETURN expressao PVIRG
        val = self.visit(ctx.expressao())
        self.ir.emit("RETURN", val, None, None)
        return None

    # -----------------------------
    # selecao (if / else)
    # selecao : IF PAREN1 expressao PAREN2 bloco senao
    # senao: ELSE bloco | /* vazio */
    # -----------------------------
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

    # -----------------------------
    # enquanto
    # -----------------------------
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

    # -----------------------------
    # EXPRESSÕES (seguindo sua gramática)
    # expressao -> exprOu
    # exprOu -> exprE ( OR exprE )*
    # exprE -> exprRelacional ( AND exprRelacional )*
    # exprRelacional -> exprAditiva ( opRelacional exprAditiva )?
    # exprAditiva -> exprMultiplicativa ( opAditivo exprMultiplicativa )*
    # exprMultiplicativa -> fator ( opMultiplicativo fator )*
    # fator -> sinal ID dimensao2 | sinal constante | TEXTO | NOT fator | PAREN1 expressao PAREN2
    # -----------------------------
    def visitExpressao(self, ctx:ExprParser.ExpressaoContext):
        return self.visit(ctx.exprOu())

    def visitExprOu(self, ctx:ExprParser.ExprOuContext):
        # left OR right OR ...
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprE())
        # exprOu OR exprE  (by grammar recursion)
        # evaluate left (may be recursive)
        left = self.visit(ctx.exprOu()) if ctx.exprOu() else self.visit(ctx.exprE())
        # if grammar used recursion differently, handle generically:
        # collect all exprE children and fold OR left-to-right
        # simpler: if there are multiple ORs, traverse children
        children = [c for c in ctx.getChildren()]
        # fallback: compute exprE chain
        if ctx.exprE():
            right = self.visit(ctx.exprE())
            temp = self.ir.new_temp()
            self.ir.emit("OR", left, right, temp)
            return temp
        return left

    def visitExprE(self, ctx:ExprParser.ExprEContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprRelacional())
        # exprE AND exprRelacional
        # left recursive: visit left then right
        left = self.visit(ctx.exprE()) if ctx.exprE() else self.visit(ctx.exprRelacional())
        if ctx.exprRelacional():
            right = self.visit(ctx.exprRelacional())
            temp = self.ir.new_temp()
            self.ir.emit("AND", left, right, temp)
            return temp
        return left

    def visitExprRelacional(self, ctx:ExprParser.ExprRelacionalContext):
        # exprRelacional : exprAditiva | exprAditiva opRelacional exprAditiva
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprAditiva(0))
        left = self.visit(ctx.exprAditiva(0))
        right = self.visit(ctx.exprAditiva(1))
        op = ctx.opRelacional().getText()
        temp = self.ir.new_temp()
        self.ir.emit(op, left, right, temp)
        return temp

    def visitExprAditiva(self, ctx:ExprParser.ExprAditivaContext):
        # left recursive: exprAditiva opAditivo exprMultiplicativa | exprMultiplicativa
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprMultiplicativa(0))
        # If recursive form: exprAditiva op exprMultiplicativa
        # In generated parser there can be multiple left recursion; handle iteratively:
        left = self.visit(ctx.exprAditiva(0)) if ctx.exprAditiva() else self.visit(ctx.exprMultiplicativa(0))
        # but safe approach: collect all multiplicative children and ops
        # We'll handle simple binary case:
        if ctx.exprAditiva() and ctx.exprMultiplicativa():
            left = self.visit(ctx.exprAditiva())
            right = self.visit(ctx.exprMultiplicativa())
            op = ctx.opAditivo().getText()
            temp = self.ir.new_temp()
            self.ir.emit(op, left, right, temp)
            return temp
        # fallback: try to get first multiplicativa
        if ctx.exprMultiplicativa():
            return self.visit(ctx.exprMultiplicativa(0))
        return left

    def visitExprMultiplicativa(self, ctx:ExprParser.ExprMultiplicativaContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.fator(0))
        # handle multiplicative left recursion similarly
        # attempt binary:
        if ctx.exprMultiplicativa() and ctx.fator():
            left = self.visit(ctx.exprMultiplicativa())
            right = self.visit(ctx.fator())
            op = ctx.opMultiplicativo().getText()
            temp = self.ir.new_temp()
            self.ir.emit(op, left, right, temp)
            return temp
        # fallback: first factor
        return self.visit(ctx.fator(0))

    def visitFator(self, ctx:ExprParser.FatorContext):
        # possibilities:
        # sinal ID dimensao2
        # sinal constante
        # TEXTO
        # NOT fator
        # PAREN1 expressao PAREN2
        # Note: sinal may be present (SOMA or SUB) as optional
        # Handle TEXTO
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

        # parenthesis
        if ctx.PAREN1():
            return self.visit(ctx.expressao())

        # sinal + ID dimensao2  OR sinal constante
        # if has ID
        if ctx.ID():
            temp = self.ir.new_temp()
            self.ir.emit("LOAD_VAR", ctx.ID().getText(), None, temp)
            # apply sinal if exists
            if ctx.sinal() and ctx.sinal().SOMA():
                return temp
            if ctx.sinal() and ctx.sinal().SUB():
                # unary minus: tmp2 = 0 - temp
                t2 = self.ir.new_temp()
                self.ir.emit("-", "0", temp, t2)
                return t2
            return temp

        # constante
        if ctx.constante():
            c = self.visit(ctx.constante())
            # c is a temp already (we load it in constante)
            # apply sinal if present
            if ctx.sinal() and ctx.sinal().SUB():
                t2 = self.ir.new_temp()
                self.ir.emit("-", "0", c, t2)
                return t2
            return c

        raise Exception("Fator inválido!")

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

    def visitSinal(self, ctx:ExprParser.SinalContext):
        # handled by caller (fator)
        return None

    # -----------------------------
    # default fallback
    # -----------------------------
    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            # only call visit if it is a ParseTree (has accept/visit)
            try:
                result = self.visit(child)
            except Exception:
                # ignore non-visitable children (tokens)
                pass
        return result
