# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#declarator.
    def enterDeclarator(self, ctx:ExprParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by ExprParser#declarator.
    def exitDeclarator(self, ctx:ExprParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by ExprParser#stmt.
    def enterStmt(self, ctx:ExprParser.StmtContext):
        pass

    # Exit a parse tree produced by ExprParser#stmt.
    def exitStmt(self, ctx:ExprParser.StmtContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
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