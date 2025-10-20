# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx:ExprParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ExprParser#secaoFuncoes.
    def enterSecaoFuncoes(self, ctx:ExprParser.SecaoFuncoesContext):
        pass

    # Exit a parse tree produced by ExprParser#secaoFuncoes.
    def exitSecaoFuncoes(self, ctx:ExprParser.SecaoFuncoesContext):
        pass


    # Enter a parse tree produced by ExprParser#listaFuncoes.
    def enterListaFuncoes(self, ctx:ExprParser.ListaFuncoesContext):
        pass

    # Exit a parse tree produced by ExprParser#listaFuncoes.
    def exitListaFuncoes(self, ctx:ExprParser.ListaFuncoesContext):
        pass


    # Enter a parse tree produced by ExprParser#decFuncao.
    def enterDecFuncao(self, ctx:ExprParser.DecFuncaoContext):
        pass

    # Exit a parse tree produced by ExprParser#decFuncao.
    def exitDecFuncao(self, ctx:ExprParser.DecFuncaoContext):
        pass


    # Enter a parse tree produced by ExprParser#tipoRetorno.
    def enterTipoRetorno(self, ctx:ExprParser.TipoRetornoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipoRetorno.
    def exitTipoRetorno(self, ctx:ExprParser.TipoRetornoContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#tipoBase.
    def enterTipoBase(self, ctx:ExprParser.TipoBaseContext):
        pass

    # Exit a parse tree produced by ExprParser#tipoBase.
    def exitTipoBase(self, ctx:ExprParser.TipoBaseContext):
        pass


    # Enter a parse tree produced by ExprParser#dimensao.
    def enterDimensao(self, ctx:ExprParser.DimensaoContext):
        pass

    # Exit a parse tree produced by ExprParser#dimensao.
    def exitDimensao(self, ctx:ExprParser.DimensaoContext):
        pass


    # Enter a parse tree produced by ExprParser#parametros.
    def enterParametros(self, ctx:ExprParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#parametros.
    def exitParametros(self, ctx:ExprParser.ParametrosContext):
        pass


    # Enter a parse tree produced by ExprParser#listaParametros.
    def enterListaParametros(self, ctx:ExprParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#listaParametros.
    def exitListaParametros(self, ctx:ExprParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by ExprParser#principal.
    def enterPrincipal(self, ctx:ExprParser.PrincipalContext):
        pass

    # Exit a parse tree produced by ExprParser#principal.
    def exitPrincipal(self, ctx:ExprParser.PrincipalContext):
        pass


    # Enter a parse tree produced by ExprParser#bloco.
    def enterBloco(self, ctx:ExprParser.BlocoContext):
        pass

    # Exit a parse tree produced by ExprParser#bloco.
    def exitBloco(self, ctx:ExprParser.BlocoContext):
        pass


    # Enter a parse tree produced by ExprParser#secaoVariaveis.
    def enterSecaoVariaveis(self, ctx:ExprParser.SecaoVariaveisContext):
        pass

    # Exit a parse tree produced by ExprParser#secaoVariaveis.
    def exitSecaoVariaveis(self, ctx:ExprParser.SecaoVariaveisContext):
        pass


    # Enter a parse tree produced by ExprParser#listaVariaveis.
    def enterListaVariaveis(self, ctx:ExprParser.ListaVariaveisContext):
        pass

    # Exit a parse tree produced by ExprParser#listaVariaveis.
    def exitListaVariaveis(self, ctx:ExprParser.ListaVariaveisContext):
        pass


    # Enter a parse tree produced by ExprParser#listaId.
    def enterListaId(self, ctx:ExprParser.ListaIdContext):
        pass

    # Exit a parse tree produced by ExprParser#listaId.
    def exitListaId(self, ctx:ExprParser.ListaIdContext):
        pass


    # Enter a parse tree produced by ExprParser#secaoComandos.
    def enterSecaoComandos(self, ctx:ExprParser.SecaoComandosContext):
        pass

    # Exit a parse tree produced by ExprParser#secaoComandos.
    def exitSecaoComandos(self, ctx:ExprParser.SecaoComandosContext):
        pass


    # Enter a parse tree produced by ExprParser#listaComandos.
    def enterListaComandos(self, ctx:ExprParser.ListaComandosContext):
        pass

    # Exit a parse tree produced by ExprParser#listaComandos.
    def exitListaComandos(self, ctx:ExprParser.ListaComandosContext):
        pass


    # Enter a parse tree produced by ExprParser#comando.
    def enterComando(self, ctx:ExprParser.ComandoContext):
        pass

    # Exit a parse tree produced by ExprParser#comando.
    def exitComando(self, ctx:ExprParser.ComandoContext):
        pass


    # Enter a parse tree produced by ExprParser#leitura.
    def enterLeitura(self, ctx:ExprParser.LeituraContext):
        pass

    # Exit a parse tree produced by ExprParser#leitura.
    def exitLeitura(self, ctx:ExprParser.LeituraContext):
        pass


    # Enter a parse tree produced by ExprParser#listaTermoLeitura.
    def enterListaTermoLeitura(self, ctx:ExprParser.ListaTermoLeituraContext):
        pass

    # Exit a parse tree produced by ExprParser#listaTermoLeitura.
    def exitListaTermoLeitura(self, ctx:ExprParser.ListaTermoLeituraContext):
        pass


    # Enter a parse tree produced by ExprParser#termoLeitura.
    def enterTermoLeitura(self, ctx:ExprParser.TermoLeituraContext):
        pass

    # Exit a parse tree produced by ExprParser#termoLeitura.
    def exitTermoLeitura(self, ctx:ExprParser.TermoLeituraContext):
        pass


    # Enter a parse tree produced by ExprParser#dimensao2.
    def enterDimensao2(self, ctx:ExprParser.Dimensao2Context):
        pass

    # Exit a parse tree produced by ExprParser#dimensao2.
    def exitDimensao2(self, ctx:ExprParser.Dimensao2Context):
        pass


    # Enter a parse tree produced by ExprParser#escrita.
    def enterEscrita(self, ctx:ExprParser.EscritaContext):
        pass

    # Exit a parse tree produced by ExprParser#escrita.
    def exitEscrita(self, ctx:ExprParser.EscritaContext):
        pass


    # Enter a parse tree produced by ExprParser#listaTermoEscrita.
    def enterListaTermoEscrita(self, ctx:ExprParser.ListaTermoEscritaContext):
        pass

    # Exit a parse tree produced by ExprParser#listaTermoEscrita.
    def exitListaTermoEscrita(self, ctx:ExprParser.ListaTermoEscritaContext):
        pass


    # Enter a parse tree produced by ExprParser#termoEscrita.
    def enterTermoEscrita(self, ctx:ExprParser.TermoEscritaContext):
        pass

    # Exit a parse tree produced by ExprParser#termoEscrita.
    def exitTermoEscrita(self, ctx:ExprParser.TermoEscritaContext):
        pass


    # Enter a parse tree produced by ExprParser#selecao.
    def enterSelecao(self, ctx:ExprParser.SelecaoContext):
        pass

    # Exit a parse tree produced by ExprParser#selecao.
    def exitSelecao(self, ctx:ExprParser.SelecaoContext):
        pass


    # Enter a parse tree produced by ExprParser#senao.
    def enterSenao(self, ctx:ExprParser.SenaoContext):
        pass

    # Exit a parse tree produced by ExprParser#senao.
    def exitSenao(self, ctx:ExprParser.SenaoContext):
        pass


    # Enter a parse tree produced by ExprParser#enquanto.
    def enterEnquanto(self, ctx:ExprParser.EnquantoContext):
        pass

    # Exit a parse tree produced by ExprParser#enquanto.
    def exitEnquanto(self, ctx:ExprParser.EnquantoContext):
        pass


    # Enter a parse tree produced by ExprParser#atribuicao.
    def enterAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by ExprParser#atribuicao.
    def exitAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by ExprParser#complemento.
    def enterComplemento(self, ctx:ExprParser.ComplementoContext):
        pass

    # Exit a parse tree produced by ExprParser#complemento.
    def exitComplemento(self, ctx:ExprParser.ComplementoContext):
        pass


    # Enter a parse tree produced by ExprParser#chamadaFuncao.
    def enterChamadaFuncao(self, ctx:ExprParser.ChamadaFuncaoContext):
        pass

    # Exit a parse tree produced by ExprParser#chamadaFuncao.
    def exitChamadaFuncao(self, ctx:ExprParser.ChamadaFuncaoContext):
        pass


    # Enter a parse tree produced by ExprParser#argumentos.
    def enterArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentos.
    def exitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by ExprParser#listaArgumentos.
    def enterListaArgumentos(self, ctx:ExprParser.ListaArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#listaArgumentos.
    def exitListaArgumentos(self, ctx:ExprParser.ListaArgumentosContext):
        pass


    # Enter a parse tree produced by ExprParser#retorno.
    def enterRetorno(self, ctx:ExprParser.RetornoContext):
        pass

    # Exit a parse tree produced by ExprParser#retorno.
    def exitRetorno(self, ctx:ExprParser.RetornoContext):
        pass


    # Enter a parse tree produced by ExprParser#expressao.
    def enterExpressao(self, ctx:ExprParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by ExprParser#expressao.
    def exitExpressao(self, ctx:ExprParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by ExprParser#exprOu.
    def enterExprOu(self, ctx:ExprParser.ExprOuContext):
        pass

    # Exit a parse tree produced by ExprParser#exprOu.
    def exitExprOu(self, ctx:ExprParser.ExprOuContext):
        pass


    # Enter a parse tree produced by ExprParser#exprE.
    def enterExprE(self, ctx:ExprParser.ExprEContext):
        pass

    # Exit a parse tree produced by ExprParser#exprE.
    def exitExprE(self, ctx:ExprParser.ExprEContext):
        pass


    # Enter a parse tree produced by ExprParser#exprRelacional.
    def enterExprRelacional(self, ctx:ExprParser.ExprRelacionalContext):
        pass

    # Exit a parse tree produced by ExprParser#exprRelacional.
    def exitExprRelacional(self, ctx:ExprParser.ExprRelacionalContext):
        pass


    # Enter a parse tree produced by ExprParser#opRelacional.
    def enterOpRelacional(self, ctx:ExprParser.OpRelacionalContext):
        pass

    # Exit a parse tree produced by ExprParser#opRelacional.
    def exitOpRelacional(self, ctx:ExprParser.OpRelacionalContext):
        pass


    # Enter a parse tree produced by ExprParser#exprAditiva.
    def enterExprAditiva(self, ctx:ExprParser.ExprAditivaContext):
        pass

    # Exit a parse tree produced by ExprParser#exprAditiva.
    def exitExprAditiva(self, ctx:ExprParser.ExprAditivaContext):
        pass


    # Enter a parse tree produced by ExprParser#opAditivo.
    def enterOpAditivo(self, ctx:ExprParser.OpAditivoContext):
        pass

    # Exit a parse tree produced by ExprParser#opAditivo.
    def exitOpAditivo(self, ctx:ExprParser.OpAditivoContext):
        pass


    # Enter a parse tree produced by ExprParser#exprMultiplicativa.
    def enterExprMultiplicativa(self, ctx:ExprParser.ExprMultiplicativaContext):
        pass

    # Exit a parse tree produced by ExprParser#exprMultiplicativa.
    def exitExprMultiplicativa(self, ctx:ExprParser.ExprMultiplicativaContext):
        pass


    # Enter a parse tree produced by ExprParser#opMultiplicativo.
    def enterOpMultiplicativo(self, ctx:ExprParser.OpMultiplicativoContext):
        pass

    # Exit a parse tree produced by ExprParser#opMultiplicativo.
    def exitOpMultiplicativo(self, ctx:ExprParser.OpMultiplicativoContext):
        pass


    # Enter a parse tree produced by ExprParser#fator.
    def enterFator(self, ctx:ExprParser.FatorContext):
        pass

    # Exit a parse tree produced by ExprParser#fator.
    def exitFator(self, ctx:ExprParser.FatorContext):
        pass


    # Enter a parse tree produced by ExprParser#constante.
    def enterConstante(self, ctx:ExprParser.ConstanteContext):
        pass

    # Exit a parse tree produced by ExprParser#constante.
    def exitConstante(self, ctx:ExprParser.ConstanteContext):
        pass


    # Enter a parse tree produced by ExprParser#sinal.
    def enterSinal(self, ctx:ExprParser.SinalContext):
        pass

    # Exit a parse tree produced by ExprParser#sinal.
    def exitSinal(self, ctx:ExprParser.SinalContext):
        pass



del ExprParser