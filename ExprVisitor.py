# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx:ExprParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#secaoFuncoes.
    def visitSecaoFuncoes(self, ctx:ExprParser.SecaoFuncoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaFuncoes.
    def visitListaFuncoes(self, ctx:ExprParser.ListaFuncoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#decFuncao.
    def visitDecFuncao(self, ctx:ExprParser.DecFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tipoRetorno.
    def visitTipoRetorno(self, ctx:ExprParser.TipoRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tipoBase.
    def visitTipoBase(self, ctx:ExprParser.TipoBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dimensao.
    def visitDimensao(self, ctx:ExprParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaParametros.
    def visitListaParametros(self, ctx:ExprParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#principal.
    def visitPrincipal(self, ctx:ExprParser.PrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloco.
    def visitBloco(self, ctx:ExprParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#secaoVariaveis.
    def visitSecaoVariaveis(self, ctx:ExprParser.SecaoVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaVariaveis.
    def visitListaVariaveis(self, ctx:ExprParser.ListaVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaId.
    def visitListaId(self, ctx:ExprParser.ListaIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#secaoComandos.
    def visitSecaoComandos(self, ctx:ExprParser.SecaoComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaComandos.
    def visitListaComandos(self, ctx:ExprParser.ListaComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comando.
    def visitComando(self, ctx:ExprParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#leitura.
    def visitLeitura(self, ctx:ExprParser.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaTermoLeitura.
    def visitListaTermoLeitura(self, ctx:ExprParser.ListaTermoLeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#termoLeitura.
    def visitTermoLeitura(self, ctx:ExprParser.TermoLeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dimensao2.
    def visitDimensao2(self, ctx:ExprParser.Dimensao2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#escrita.
    def visitEscrita(self, ctx:ExprParser.EscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaTermoEscrita.
    def visitListaTermoEscrita(self, ctx:ExprParser.ListaTermoEscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#termoEscrita.
    def visitTermoEscrita(self, ctx:ExprParser.TermoEscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#selecao.
    def visitSelecao(self, ctx:ExprParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#senao.
    def visitSenao(self, ctx:ExprParser.SenaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#enquanto.
    def visitEnquanto(self, ctx:ExprParser.EnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atribuicao.
    def visitAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#complemento.
    def visitComplemento(self, ctx:ExprParser.ComplementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:ExprParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listaArgumentos.
    def visitListaArgumentos(self, ctx:ExprParser.ListaArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#retorno.
    def visitRetorno(self, ctx:ExprParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expressao.
    def visitExpressao(self, ctx:ExprParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprOu.
    def visitExprOu(self, ctx:ExprParser.ExprOuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprE.
    def visitExprE(self, ctx:ExprParser.ExprEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprRelacional.
    def visitExprRelacional(self, ctx:ExprParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#opRelacional.
    def visitOpRelacional(self, ctx:ExprParser.OpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprAditiva.
    def visitExprAditiva(self, ctx:ExprParser.ExprAditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#opAditivo.
    def visitOpAditivo(self, ctx:ExprParser.OpAditivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprMultiplicativa.
    def visitExprMultiplicativa(self, ctx:ExprParser.ExprMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#opMultiplicativo.
    def visitOpMultiplicativo(self, ctx:ExprParser.OpMultiplicativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fator.
    def visitFator(self, ctx:ExprParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constante.
    def visitConstante(self, ctx:ExprParser.ConstanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sinal.
    def visitSinal(self, ctx:ExprParser.SinalContext):
        return self.visitChildren(ctx)



del ExprParser