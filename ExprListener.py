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


    # Enter a parse tree produced by ExprParser#forInit.
    def enterForInit(self, ctx:ExprParser.ForInitContext):
        pass

    # Exit a parse tree produced by ExprParser#forInit.
    def exitForInit(self, ctx:ExprParser.ForInitContext):
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


    # Enter a parse tree produced by ExprParser#assignExpr.
    def enterAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by ExprParser#assignExpr.
    def exitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by ExprParser#logicOr.
    def enterLogicOr(self, ctx:ExprParser.LogicOrContext):
        pass

    # Exit a parse tree produced by ExprParser#logicOr.
    def exitLogicOr(self, ctx:ExprParser.LogicOrContext):
        pass


    # Enter a parse tree produced by ExprParser#logicAnd.
    def enterLogicAnd(self, ctx:ExprParser.LogicAndContext):
        pass

    # Exit a parse tree produced by ExprParser#logicAnd.
    def exitLogicAnd(self, ctx:ExprParser.LogicAndContext):
        pass


    # Enter a parse tree produced by ExprParser#equality.
    def enterEquality(self, ctx:ExprParser.EqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#equality.
    def exitEquality(self, ctx:ExprParser.EqualityContext):
        pass


    # Enter a parse tree produced by ExprParser#relational.
    def enterRelational(self, ctx:ExprParser.RelationalContext):
        pass

    # Exit a parse tree produced by ExprParser#relational.
    def exitRelational(self, ctx:ExprParser.RelationalContext):
        pass


    # Enter a parse tree produced by ExprParser#add.
    def enterAdd(self, ctx:ExprParser.AddContext):
        pass

    # Exit a parse tree produced by ExprParser#add.
    def exitAdd(self, ctx:ExprParser.AddContext):
        pass


    # Enter a parse tree produced by ExprParser#mul.
    def enterMul(self, ctx:ExprParser.MulContext):
        pass

    # Exit a parse tree produced by ExprParser#mul.
    def exitMul(self, ctx:ExprParser.MulContext):
        pass


    # Enter a parse tree produced by ExprParser#unary.
    def enterUnary(self, ctx:ExprParser.UnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#unary.
    def exitUnary(self, ctx:ExprParser.UnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#primary.
    def enterPrimary(self, ctx:ExprParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExprParser#primary.
    def exitPrimary(self, ctx:ExprParser.PrimaryContext):
        pass



del ExprParser