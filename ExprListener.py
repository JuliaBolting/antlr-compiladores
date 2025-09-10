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


    # Enter a parse tree produced by ExprParser#declaracoes.
    def enterDeclaracoes(self, ctx:ExprParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracoes.
    def exitDeclaracoes(self, ctx:ExprParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#comandos.
    def enterComandos(self, ctx:ExprParser.ComandosContext):
        pass

    # Exit a parse tree produced by ExprParser#comandos.
    def exitComandos(self, ctx:ExprParser.ComandosContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoIf.
    def enterComandoIf(self, ctx:ExprParser.ComandoIfContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoIf.
    def exitComandoIf(self, ctx:ExprParser.ComandoIfContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoWhile.
    def enterComandoWhile(self, ctx:ExprParser.ComandoWhileContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoWhile.
    def exitComandoWhile(self, ctx:ExprParser.ComandoWhileContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoFor.
    def enterComandoFor(self, ctx:ExprParser.ComandoForContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoFor.
    def exitComandoFor(self, ctx:ExprParser.ComandoForContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracaoFor.
    def enterDeclaracaoFor(self, ctx:ExprParser.DeclaracaoForContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracaoFor.
    def exitDeclaracaoFor(self, ctx:ExprParser.DeclaracaoForContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoAtribuicao.
    def enterComandoAtribuicao(self, ctx:ExprParser.ComandoAtribuicaoContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoAtribuicao.
    def exitComandoAtribuicao(self, ctx:ExprParser.ComandoAtribuicaoContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoPrint.
    def enterComandoPrint(self, ctx:ExprParser.ComandoPrintContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoPrint.
    def exitComandoPrint(self, ctx:ExprParser.ComandoPrintContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoScanf.
    def enterComandoScanf(self, ctx:ExprParser.ComandoScanfContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoScanf.
    def exitComandoScanf(self, ctx:ExprParser.ComandoScanfContext):
        pass


    # Enter a parse tree produced by ExprParser#comandoReturn.
    def enterComandoReturn(self, ctx:ExprParser.ComandoReturnContext):
        pass

    # Exit a parse tree produced by ExprParser#comandoReturn.
    def exitComandoReturn(self, ctx:ExprParser.ComandoReturnContext):
        pass


    # Enter a parse tree produced by ExprParser#expressao.
    def enterExpressao(self, ctx:ExprParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by ExprParser#expressao.
    def exitExpressao(self, ctx:ExprParser.ExpressaoContext):
        pass



del ExprParser