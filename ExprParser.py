# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,1,2,3,2,54,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,3,3,3,81,8,3,1,3,3,3,84,8,
        3,1,3,1,3,3,3,88,8,3,1,3,1,3,1,3,1,3,3,3,94,8,3,1,3,1,3,3,3,98,8,
        3,1,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,3,6,115,8,6,1,7,1,7,1,7,5,7,120,8,7,10,7,12,7,123,9,7,1,
        8,1,8,1,8,5,8,128,8,8,10,8,12,8,131,9,8,1,9,1,9,1,9,5,9,136,8,9,
        10,9,12,9,139,9,9,1,10,1,10,1,10,5,10,144,8,10,10,10,12,10,147,9,
        10,1,11,1,11,1,11,5,11,152,8,11,10,11,12,11,155,9,11,1,12,1,12,1,
        12,5,12,160,8,12,10,12,12,12,163,9,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,172,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,
        14,182,8,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        0,5,1,0,11,15,1,0,1,2,1,0,3,6,1,0,25,26,1,0,27,29,199,0,34,1,0,0,
        0,2,39,1,0,0,0,4,50,1,0,0,0,6,97,1,0,0,0,8,99,1,0,0,0,10,109,1,0,
        0,0,12,111,1,0,0,0,14,116,1,0,0,0,16,124,1,0,0,0,18,132,1,0,0,0,
        20,140,1,0,0,0,22,148,1,0,0,0,24,156,1,0,0,0,26,171,1,0,0,0,28,181,
        1,0,0,0,30,33,3,2,1,0,31,33,3,6,3,0,32,30,1,0,0,0,32,31,1,0,0,0,
        33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,
        0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,40,7,0,0,0,40,45,3,4,2,0,41,
        42,5,40,0,0,42,44,3,4,2,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,1,0,
        0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,41,0,0,49,
        3,1,0,0,0,50,53,5,9,0,0,51,52,5,24,0,0,52,54,3,10,5,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,5,1,0,0,0,55,56,3,10,5,0,56,57,5,41,0,0,57,
        98,1,0,0,0,58,59,5,16,0,0,59,60,5,34,0,0,60,61,3,10,5,0,61,62,5,
        35,0,0,62,65,3,8,4,0,63,64,5,17,0,0,64,66,3,8,4,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,98,1,0,0,0,67,68,5,19,0,0,68,69,5,34,0,0,69,70,
        3,10,5,0,70,71,5,35,0,0,71,72,3,8,4,0,72,98,1,0,0,0,73,74,5,18,0,
        0,74,80,5,34,0,0,75,81,3,2,1,0,76,78,3,10,5,0,77,76,1,0,0,0,77,78,
        1,0,0,0,78,79,1,0,0,0,79,81,5,41,0,0,80,75,1,0,0,0,80,77,1,0,0,0,
        81,83,1,0,0,0,82,84,3,10,5,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,
        0,0,0,85,87,5,41,0,0,86,88,3,10,5,0,87,86,1,0,0,0,87,88,1,0,0,0,
        88,89,1,0,0,0,89,90,5,35,0,0,90,98,3,8,4,0,91,93,5,23,0,0,92,94,
        3,10,5,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,98,5,41,0,
        0,96,98,3,8,4,0,97,55,1,0,0,0,97,58,1,0,0,0,97,67,1,0,0,0,97,73,
        1,0,0,0,97,91,1,0,0,0,97,96,1,0,0,0,98,7,1,0,0,0,99,104,5,38,0,0,
        100,103,3,2,1,0,101,103,3,6,3,0,102,100,1,0,0,0,102,101,1,0,0,0,
        103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,
        106,104,1,0,0,0,107,108,5,39,0,0,108,9,1,0,0,0,109,110,3,12,6,0,
        110,11,1,0,0,0,111,114,3,14,7,0,112,113,5,24,0,0,113,115,3,12,6,
        0,114,112,1,0,0,0,114,115,1,0,0,0,115,13,1,0,0,0,116,121,3,16,8,
        0,117,118,5,31,0,0,118,120,3,16,8,0,119,117,1,0,0,0,120,123,1,0,
        0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,15,1,0,0,0,123,121,1,0,0,
        0,124,129,3,18,9,0,125,126,5,30,0,0,126,128,3,18,9,0,127,125,1,0,
        0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,17,1,0,0,
        0,131,129,1,0,0,0,132,137,3,20,10,0,133,134,7,1,0,0,134,136,3,20,
        10,0,135,133,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,
        0,0,138,19,1,0,0,0,139,137,1,0,0,0,140,145,3,22,11,0,141,142,7,2,
        0,0,142,144,3,22,11,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,
        0,0,0,145,146,1,0,0,0,146,21,1,0,0,0,147,145,1,0,0,0,148,153,3,24,
        12,0,149,150,7,3,0,0,150,152,3,24,12,0,151,149,1,0,0,0,152,155,1,
        0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,23,1,0,0,0,155,153,1,0,
        0,0,156,161,3,26,13,0,157,158,7,4,0,0,158,160,3,26,13,0,159,157,
        1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,25,1,
        0,0,0,163,161,1,0,0,0,164,165,5,32,0,0,165,172,3,26,13,0,166,167,
        5,25,0,0,167,172,3,26,13,0,168,169,5,26,0,0,169,172,3,26,13,0,170,
        172,3,28,14,0,171,164,1,0,0,0,171,166,1,0,0,0,171,168,1,0,0,0,171,
        170,1,0,0,0,172,27,1,0,0,0,173,174,5,34,0,0,174,175,3,10,5,0,175,
        176,5,35,0,0,176,182,1,0,0,0,177,182,5,8,0,0,178,182,5,7,0,0,179,
        182,5,9,0,0,180,182,5,10,0,0,181,173,1,0,0,0,181,177,1,0,0,0,181,
        178,1,0,0,0,181,179,1,0,0,0,181,180,1,0,0,0,182,29,1,0,0,0,22,32,
        34,45,53,65,77,80,83,87,93,97,102,104,114,121,129,137,145,153,161,
        171,181
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'char'", "'boolean'", "'void'", 
                     "'if'", "'else'", "'for'", "'while'", "'scanf'", "'println'", 
                     "'main'", "'return'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'&&'", "'||'", "'!'", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM_INT", 
                      "NUM_DEC", "ID", "TEXTO", "INT", "FLOAT", "CHAR", 
                      "BOOLEAN", "VOID", "IF", "ELSE", "FOR", "WHILE", "SCANF", 
                      "PRINTLN", "MAIN", "RETURN", "ASSIGN", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "AND", "OR", "NOT", "COMP", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
                      "RBRACE", "COMMA", "SEMI", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_declarator = 2
    RULE_stmt = 3
    RULE_block = 4
    RULE_expr = 5
    RULE_assignExpr = 6
    RULE_logicOr = 7
    RULE_logicAnd = 8
    RULE_equality = 9
    RULE_relational = 10
    RULE_add = 11
    RULE_mul = 12
    RULE_unary = 13
    RULE_primary = 14

    ruleNames =  [ "program", "declaration", "declarator", "stmt", "block", 
                   "expr", "assignExpr", "logicOr", "logicAnd", "equality", 
                   "relational", "add", "mul", "unary", "primary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUM_INT=7
    NUM_DEC=8
    ID=9
    TEXTO=10
    INT=11
    FLOAT=12
    CHAR=13
    BOOLEAN=14
    VOID=15
    IF=16
    ELSE=17
    FOR=18
    WHILE=19
    SCANF=20
    PRINTLN=21
    MAIN=22
    RETURN=23
    ASSIGN=24
    PLUS=25
    MINUS=26
    MULT=27
    DIV=28
    MOD=29
    AND=30
    OR=31
    NOT=32
    COMP=33
    LPAREN=34
    RPAREN=35
    LBRACK=36
    RBRACK=37
    LBRACE=38
    RBRACE=39
    COMMA=40
    SEMI=41
    COMMENT=42
    WS=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 296462712704) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 14, 15]:
                    self.state = 30
                    self.declaration()
                    pass
                elif token in [7, 8, 9, 10, 16, 18, 19, 23, 25, 26, 32, 34, 38]:
                    self.state = 31
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclaratorContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclaratorContext,i)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def BOOLEAN(self):
            return self.getToken(ExprParser.BOOLEAN, 0)

        def VOID(self):
            return self.getToken(ExprParser.VOID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 40
            self.declarator()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 41
                self.match(ExprParser.COMMA)
                self.state = 42
                self.declarator()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ExprParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)




    def declarator(self):

        localctx = ExprParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ExprParser.ID)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 51
                self.match(ExprParser.ASSIGN)
                self.state = 52
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)


        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 25, 26, 32, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.expr()
                self.state = 56
                self.match(ExprParser.SEMI)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(ExprParser.IF)
                self.state = 59
                self.match(ExprParser.LPAREN)
                self.state = 60
                self.expr()
                self.state = 61
                self.match(ExprParser.RPAREN)
                self.state = 62
                self.block()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 63
                    self.match(ExprParser.ELSE)
                    self.state = 64
                    self.block()


                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(ExprParser.WHILE)
                self.state = 68
                self.match(ExprParser.LPAREN)
                self.state = 69
                self.expr()
                self.state = 70
                self.match(ExprParser.RPAREN)
                self.state = 71
                self.block()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(ExprParser.FOR)
                self.state = 74
                self.match(ExprParser.LPAREN)
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 14, 15]:
                    self.state = 75
                    self.declaration()
                    pass
                elif token in [7, 8, 9, 10, 25, 26, 32, 34, 41]:
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21575501696) != 0):
                        self.state = 76
                        self.expr()


                    self.state = 79
                    self.match(ExprParser.SEMI)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21575501696) != 0):
                    self.state = 82
                    self.expr()


                self.state = 85
                self.match(ExprParser.SEMI)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21575501696) != 0):
                    self.state = 86
                    self.expr()


                self.state = 89
                self.match(ExprParser.RPAREN)
                self.state = 90
                self.block()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.match(ExprParser.RETURN)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21575501696) != 0):
                    self.state = 92
                    self.expr()


                self.state = 95
                self.match(ExprParser.SEMI)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExprParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprParser.RBRACE, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ExprParser.LBRACE)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 296462712704) != 0):
                self.state = 102
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 14, 15]:
                    self.state = 100
                    self.declaration()
                    pass
                elif token in [7, 8, 9, 10, 16, 18, 19, 23, 25, 26, 32, 34, 38]:
                    self.state = 101
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(ExprParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(ExprParser.AssignExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.assignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOr(self):
            return self.getTypedRuleContext(ExprParser.LogicOrContext,0)


        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def assignExpr(self):
            return self.getTypedRuleContext(ExprParser.AssignExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)




    def assignExpr(self):

        localctx = ExprParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.logicOr()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 112
                self.match(ExprParser.ASSIGN)
                self.state = 113
                self.assignExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LogicAndContext)
            else:
                return self.getTypedRuleContext(ExprParser.LogicAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.OR)
            else:
                return self.getToken(ExprParser.OR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_logicOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)




    def logicOr(self):

        localctx = ExprParser.LogicOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logicOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.logicAnd()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 117
                self.match(ExprParser.OR)
                self.state = 118
                self.logicAnd()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.EqualityContext)
            else:
                return self.getTypedRuleContext(ExprParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.AND)
            else:
                return self.getToken(ExprParser.AND, i)

        def getRuleIndex(self):
            return ExprParser.RULE_logicAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)




    def logicAnd(self):

        localctx = ExprParser.LogicAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.equality()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 125
                self.match(ExprParser.AND)
                self.state = 126
                self.equality()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.RelationalContext)
            else:
                return self.getTypedRuleContext(ExprParser.RelationalContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)




    def equality(self):

        localctx = ExprParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.relational()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 133
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 134
                self.relational()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AddContext)
            else:
                return self.getTypedRuleContext(ExprParser.AddContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)




    def relational(self):

        localctx = ExprParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.add()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0):
                self.state = 141
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.add()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MulContext)
            else:
                return self.getTypedRuleContext(ExprParser.MulContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PLUS)
            else:
                return self.getToken(ExprParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MINUS)
            else:
                return self.getToken(ExprParser.MINUS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)




    def add(self):

        localctx = ExprParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.mul()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.mul()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.UnaryContext)
            else:
                return self.getTypedRuleContext(ExprParser.UnaryContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MULT)
            else:
                return self.getToken(ExprParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIV)
            else:
                return self.getToken(ExprParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MOD)
            else:
                return self.getToken(ExprParser.MOD, i)

        def getRuleIndex(self):
            return ExprParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)




    def mul(self):

        localctx = ExprParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mul)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.unary()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 157
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.unary()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(ExprParser.PrimaryContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = ExprParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unary)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(ExprParser.NOT)
                self.state = 165
                self.unary()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(ExprParser.PLUS)
                self.state = 167
                self.unary()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(ExprParser.MINUS)
                self.state = 169
                self.unary()
                pass
            elif token in [7, 8, 9, 10, 34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def NUM_DEC(self):
            return self.getToken(ExprParser.NUM_DEC, 0)

        def NUM_INT(self):
            return self.getToken(ExprParser.NUM_INT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = ExprParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primary)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(ExprParser.LPAREN)
                self.state = 174
                self.expr()
                self.state = 175
                self.match(ExprParser.RPAREN)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(ExprParser.NUM_DEC)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(ExprParser.NUM_INT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(ExprParser.ID)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.match(ExprParser.TEXTO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





