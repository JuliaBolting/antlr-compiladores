# Generated from Expr.g4 by ANTLR 4.13.2
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
        4,1,44,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,52,8,0,10,0,12,0,
        55,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,64,8,1,1,1,1,1,1,1,1,1,3,
        1,70,8,1,5,1,72,8,1,10,1,12,1,75,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,89,8,1,10,1,12,1,92,9,1,1,1,1,1,3,1,96,8,
        1,1,1,1,1,3,1,100,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,111,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,119,8,4,10,4,12,4,122,9,4,1,4,1,
        4,1,4,1,4,1,4,5,4,129,8,4,10,4,12,4,132,9,4,1,4,3,4,135,8,4,3,4,
        137,8,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,145,8,5,10,5,12,5,148,9,5,1,
        5,1,5,1,6,1,6,1,6,3,6,155,8,6,1,6,1,6,3,6,159,8,6,1,6,1,6,3,6,163,
        8,6,1,6,1,6,1,6,5,6,168,8,6,10,6,12,6,171,9,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,183,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,198,8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,206,
        8,9,10,9,12,9,209,9,9,3,9,211,8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,3,11,226,8,11,1,11,1,11,1,12,1,12,
        1,13,1,13,1,13,3,13,235,8,13,1,14,1,14,1,14,5,14,240,8,14,10,14,
        12,14,243,9,14,1,15,1,15,1,15,5,15,248,8,15,10,15,12,15,251,9,15,
        1,16,1,16,1,16,5,16,256,8,16,10,16,12,16,259,9,16,1,17,1,17,1,17,
        5,17,264,8,17,10,17,12,17,267,9,17,1,18,1,18,1,18,5,18,272,8,18,
        10,18,12,18,275,9,18,1,19,1,19,1,19,5,19,280,8,19,10,19,12,19,283,
        9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,292,8,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,309,8,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,0,5,1,0,1,5,1,0,17,18,1,0,19,22,1,0,23,24,1,
        0,25,27,333,0,44,1,0,0,0,2,99,1,0,0,0,4,101,1,0,0,0,6,110,1,0,0,
        0,8,112,1,0,0,0,10,138,1,0,0,0,12,151,1,0,0,0,14,182,1,0,0,0,16,
        197,1,0,0,0,18,199,1,0,0,0,20,215,1,0,0,0,22,223,1,0,0,0,24,229,
        1,0,0,0,26,231,1,0,0,0,28,236,1,0,0,0,30,244,1,0,0,0,32,252,1,0,
        0,0,34,260,1,0,0,0,36,268,1,0,0,0,38,276,1,0,0,0,40,291,1,0,0,0,
        42,308,1,0,0,0,44,45,5,5,0,0,45,46,5,11,0,0,46,47,5,33,0,0,47,48,
        5,34,0,0,48,53,5,35,0,0,49,52,3,2,1,0,50,52,3,6,3,0,51,49,1,0,0,
        0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,
        1,0,0,0,55,53,1,0,0,0,56,57,5,36,0,0,57,58,5,0,0,1,58,1,1,0,0,0,
        59,60,3,4,2,0,60,63,5,42,0,0,61,62,5,16,0,0,62,64,3,24,12,0,63,61,
        1,0,0,0,63,64,1,0,0,0,64,73,1,0,0,0,65,66,5,32,0,0,66,69,5,42,0,
        0,67,68,5,16,0,0,68,70,3,24,12,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        72,1,0,0,0,71,65,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,
        0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,31,0,0,77,100,1,0,0,0,78,79,
        3,4,2,0,79,80,5,42,0,0,80,81,5,37,0,0,81,82,5,40,0,0,82,95,5,38,
        0,0,83,84,5,16,0,0,84,85,5,35,0,0,85,90,3,24,12,0,86,87,5,32,0,0,
        87,89,3,24,12,0,88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,
        1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,93,94,5,36,0,0,94,96,1,0,0,0,
        95,83,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,31,0,0,98,100,
        1,0,0,0,99,59,1,0,0,0,99,78,1,0,0,0,100,3,1,0,0,0,101,102,7,0,0,
        0,102,5,1,0,0,0,103,111,3,8,4,0,104,111,3,10,5,0,105,111,3,12,6,
        0,106,111,3,16,8,0,107,111,3,18,9,0,108,111,3,20,10,0,109,111,3,
        22,11,0,110,103,1,0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,
        1,0,0,0,110,107,1,0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,7,1,
        0,0,0,112,113,5,6,0,0,113,114,5,33,0,0,114,115,3,24,12,0,115,116,
        5,34,0,0,116,120,5,35,0,0,117,119,3,6,3,0,118,117,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,
        1,0,0,0,123,136,5,36,0,0,124,134,5,7,0,0,125,135,3,8,4,0,126,130,
        5,35,0,0,127,129,3,6,3,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,135,
        5,36,0,0,134,125,1,0,0,0,134,126,1,0,0,0,135,137,1,0,0,0,136,124,
        1,0,0,0,136,137,1,0,0,0,137,9,1,0,0,0,138,139,5,9,0,0,139,140,5,
        33,0,0,140,141,3,24,12,0,141,142,5,34,0,0,142,146,5,35,0,0,143,145,
        3,6,3,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,
        1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,5,36,0,0,150,11,
        1,0,0,0,151,152,5,8,0,0,152,154,5,33,0,0,153,155,3,14,7,0,154,153,
        1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,158,5,31,0,0,157,159,
        3,24,12,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,162,
        5,31,0,0,161,163,3,26,13,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,
        1,0,0,0,164,165,5,34,0,0,165,169,5,35,0,0,166,168,3,6,3,0,167,166,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,
        1,0,0,0,171,169,1,0,0,0,172,173,5,36,0,0,173,13,1,0,0,0,174,175,
        3,4,2,0,175,176,5,42,0,0,176,177,5,16,0,0,177,178,3,24,12,0,178,
        183,1,0,0,0,179,180,5,42,0,0,180,181,5,16,0,0,181,183,3,24,12,0,
        182,174,1,0,0,0,182,179,1,0,0,0,183,15,1,0,0,0,184,185,5,42,0,0,
        185,186,5,16,0,0,186,187,3,24,12,0,187,188,5,31,0,0,188,198,1,0,
        0,0,189,190,5,42,0,0,190,191,5,37,0,0,191,192,3,24,12,0,192,193,
        5,38,0,0,193,194,5,16,0,0,194,195,3,24,12,0,195,196,5,31,0,0,196,
        198,1,0,0,0,197,184,1,0,0,0,197,189,1,0,0,0,198,17,1,0,0,0,199,200,
        5,12,0,0,200,210,5,33,0,0,201,211,3,24,12,0,202,207,5,41,0,0,203,
        204,5,23,0,0,204,206,3,24,12,0,205,203,1,0,0,0,206,209,1,0,0,0,207,
        205,1,0,0,0,207,208,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,
        201,1,0,0,0,210,202,1,0,0,0,211,212,1,0,0,0,212,213,5,34,0,0,213,
        214,5,31,0,0,214,19,1,0,0,0,215,216,5,13,0,0,216,217,5,33,0,0,217,
        218,5,41,0,0,218,219,5,32,0,0,219,220,3,24,12,0,220,221,5,34,0,0,
        221,222,5,31,0,0,222,21,1,0,0,0,223,225,5,10,0,0,224,226,3,24,12,
        0,225,224,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,5,31,0,
        0,228,23,1,0,0,0,229,230,3,26,13,0,230,25,1,0,0,0,231,234,3,28,14,
        0,232,233,5,16,0,0,233,235,3,26,13,0,234,232,1,0,0,0,234,235,1,0,
        0,0,235,27,1,0,0,0,236,241,3,30,15,0,237,238,5,29,0,0,238,240,3,
        30,15,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,29,1,0,0,0,243,241,1,0,0,0,244,249,3,32,16,0,245,246,
        5,28,0,0,246,248,3,32,16,0,247,245,1,0,0,0,248,251,1,0,0,0,249,247,
        1,0,0,0,249,250,1,0,0,0,250,31,1,0,0,0,251,249,1,0,0,0,252,257,3,
        34,17,0,253,254,7,1,0,0,254,256,3,34,17,0,255,253,1,0,0,0,256,259,
        1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,33,1,0,0,0,259,257,1,
        0,0,0,260,265,3,36,18,0,261,262,7,2,0,0,262,264,3,36,18,0,263,261,
        1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,35,1,
        0,0,0,267,265,1,0,0,0,268,273,3,38,19,0,269,270,7,3,0,0,270,272,
        3,38,19,0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,37,1,0,0,0,275,273,1,0,0,0,276,281,3,40,20,0,277,278,
        7,4,0,0,278,280,3,40,20,0,279,277,1,0,0,0,280,283,1,0,0,0,281,279,
        1,0,0,0,281,282,1,0,0,0,282,39,1,0,0,0,283,281,1,0,0,0,284,285,5,
        24,0,0,285,292,3,40,20,0,286,287,5,23,0,0,287,292,3,40,20,0,288,
        289,5,30,0,0,289,292,3,40,20,0,290,292,3,42,21,0,291,284,1,0,0,0,
        291,286,1,0,0,0,291,288,1,0,0,0,291,290,1,0,0,0,292,41,1,0,0,0,293,
        294,5,33,0,0,294,295,3,24,12,0,295,296,5,34,0,0,296,309,1,0,0,0,
        297,309,5,40,0,0,298,309,5,39,0,0,299,309,5,42,0,0,300,301,5,42,
        0,0,301,302,5,37,0,0,302,303,3,24,12,0,303,304,5,38,0,0,304,309,
        1,0,0,0,305,309,5,41,0,0,306,309,5,14,0,0,307,309,5,15,0,0,308,293,
        1,0,0,0,308,297,1,0,0,0,308,298,1,0,0,0,308,299,1,0,0,0,308,300,
        1,0,0,0,308,305,1,0,0,0,308,306,1,0,0,0,308,307,1,0,0,0,309,43,1,
        0,0,0,32,51,53,63,69,73,90,95,99,110,120,130,134,136,146,154,158,
        162,169,182,197,207,210,225,234,241,249,257,265,273,281,291,308
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'char'", "'boolean'", 
                     "'void'", "'if'", "'else'", "'for'", "'while'", "'return'", 
                     "'main'", "'println'", "'scanf'", "'true'", "'false'", 
                     "'='", "'=='", "'!='", "'<='", "'<'", "'>='", "'>'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
                     "'!'", "';'", "','", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "CHAR", "BOOLEAN", "VOID", 
                      "IF", "ELSE", "FOR", "WHILE", "RETURN", "MAIN", "PRINTLN", 
                      "SCANF", "TRUE", "FALSE", "ATRIB", "EQ", "NEQ", "LE", 
                      "LT", "GE", "GT", "SOMA", "SUB", "MUL", "DIV", "RESTO", 
                      "AND", "OR", "NOT", "PVIRG", "VIRG", "PAREN1", "PAREN2", 
                      "CHAVE1", "CHAVE2", "COLCH1", "COLCH2", "NUM_DEC", 
                      "NUM_INT", "TEXTO", "ID", "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_tipo = 2
    RULE_comandos = 3
    RULE_comandoIf = 4
    RULE_comandoWhile = 5
    RULE_comandoFor = 6
    RULE_forInit = 7
    RULE_comandoAtribuicao = 8
    RULE_comandoPrint = 9
    RULE_comandoScanf = 10
    RULE_comandoReturn = 11
    RULE_expressao = 12
    RULE_assignExpr = 13
    RULE_logicOr = 14
    RULE_logicAnd = 15
    RULE_equality = 16
    RULE_relational = 17
    RULE_add = 18
    RULE_mul = 19
    RULE_unary = 20
    RULE_primary = 21

    ruleNames =  [ "programa", "declaracoes", "tipo", "comandos", "comandoIf", 
                   "comandoWhile", "comandoFor", "forInit", "comandoAtribuicao", 
                   "comandoPrint", "comandoScanf", "comandoReturn", "expressao", 
                   "assignExpr", "logicOr", "logicAnd", "equality", "relational", 
                   "add", "mul", "unary", "primary" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    CHAR=3
    BOOLEAN=4
    VOID=5
    IF=6
    ELSE=7
    FOR=8
    WHILE=9
    RETURN=10
    MAIN=11
    PRINTLN=12
    SCANF=13
    TRUE=14
    FALSE=15
    ATRIB=16
    EQ=17
    NEQ=18
    LE=19
    LT=20
    GE=21
    GT=22
    SOMA=23
    SUB=24
    MUL=25
    DIV=26
    RESTO=27
    AND=28
    OR=29
    NOT=30
    PVIRG=31
    VIRG=32
    PAREN1=33
    PAREN2=34
    CHAVE1=35
    CHAVE2=36
    COLCH1=37
    COLCH2=38
    NUM_DEC=39
    NUM_INT=40
    TEXTO=41
    ID=42
    COMMENT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(ExprParser.VOID, 0)

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def CHAVE1(self):
            return self.getToken(ExprParser.CHAVE1, 0)

        def CHAVE2(self):
            return self.getToken(ExprParser.CHAVE2, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def declaracoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclaracoesContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclaracoesContext,i)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandosContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandosContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.VOID)
            self.state = 45
            self.match(ExprParser.MAIN)
            self.state = 46
            self.match(ExprParser.PAREN1)
            self.state = 47
            self.match(ExprParser.PAREN2)
            self.state = 48
            self.match(ExprParser.CHAVE1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046525310) != 0):
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5]:
                    self.state = 49
                    self.declaracoes()
                    pass
                elif token in [6, 8, 9, 10, 12, 13, 42]:
                    self.state = 50
                    self.comandos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(ExprParser.CHAVE2)
            self.state = 57
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def ATRIB(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ATRIB)
            else:
                return self.getToken(ExprParser.ATRIB, i)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VIRG)
            else:
                return self.getToken(ExprParser.VIRG, i)

        def COLCH1(self):
            return self.getToken(ExprParser.COLCH1, 0)

        def NUM_INT(self):
            return self.getToken(ExprParser.NUM_INT, 0)

        def COLCH2(self):
            return self.getToken(ExprParser.COLCH2, 0)

        def CHAVE1(self):
            return self.getToken(ExprParser.CHAVE1, 0)

        def CHAVE2(self):
            return self.getToken(ExprParser.CHAVE2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)




    def declaracoes(self):

        localctx = ExprParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.tipo()
                self.state = 60
                self.match(ExprParser.ID)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 61
                    self.match(ExprParser.ATRIB)
                    self.state = 62
                    self.expressao()


                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 65
                    self.match(ExprParser.VIRG)
                    self.state = 66
                    self.match(ExprParser.ID)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 67
                        self.match(ExprParser.ATRIB)
                        self.state = 68
                        self.expressao()


                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 76
                self.match(ExprParser.PVIRG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.tipo()
                self.state = 79
                self.match(ExprParser.ID)
                self.state = 80
                self.match(ExprParser.COLCH1)
                self.state = 81
                self.match(ExprParser.NUM_INT)
                self.state = 82
                self.match(ExprParser.COLCH2)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 83
                    self.match(ExprParser.ATRIB)
                    self.state = 84
                    self.match(ExprParser.CHAVE1)
                    self.state = 85
                    self.expressao()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==32:
                        self.state = 86
                        self.match(ExprParser.VIRG)
                        self.state = 87
                        self.expressao()
                        self.state = 92
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 93
                    self.match(ExprParser.CHAVE2)


                self.state = 97
                self.match(ExprParser.PVIRG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return ExprParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = ExprParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandoIf(self):
            return self.getTypedRuleContext(ExprParser.ComandoIfContext,0)


        def comandoWhile(self):
            return self.getTypedRuleContext(ExprParser.ComandoWhileContext,0)


        def comandoFor(self):
            return self.getTypedRuleContext(ExprParser.ComandoForContext,0)


        def comandoAtribuicao(self):
            return self.getTypedRuleContext(ExprParser.ComandoAtribuicaoContext,0)


        def comandoPrint(self):
            return self.getTypedRuleContext(ExprParser.ComandoPrintContext,0)


        def comandoScanf(self):
            return self.getTypedRuleContext(ExprParser.ComandoScanfContext,0)


        def comandoReturn(self):
            return self.getTypedRuleContext(ExprParser.ComandoReturnContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = ExprParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comandos)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.comandoIf()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.comandoWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.comandoFor()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.comandoAtribuicao()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.comandoPrint()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.comandoScanf()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                self.comandoReturn()
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


    class ComandoIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def CHAVE1(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHAVE1)
            else:
                return self.getToken(ExprParser.CHAVE1, i)

        def CHAVE2(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHAVE2)
            else:
                return self.getToken(ExprParser.CHAVE2, i)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandosContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandosContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def comandoIf(self):
            return self.getTypedRuleContext(ExprParser.ComandoIfContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comandoIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoIf" ):
                listener.enterComandoIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoIf" ):
                listener.exitComandoIf(self)




    def comandoIf(self):

        localctx = ExprParser.ComandoIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comandoIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ExprParser.IF)
            self.state = 113
            self.match(ExprParser.PAREN1)
            self.state = 114
            self.expressao()
            self.state = 115
            self.match(ExprParser.PAREN2)
            self.state = 116
            self.match(ExprParser.CHAVE1)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046525248) != 0):
                self.state = 117
                self.comandos()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(ExprParser.CHAVE2)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 124
                self.match(ExprParser.ELSE)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 125
                    self.comandoIf()
                    pass
                elif token in [35]:
                    self.state = 126
                    self.match(ExprParser.CHAVE1)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046525248) != 0):
                        self.state = 127
                        self.comandos()
                        self.state = 132
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 133
                    self.match(ExprParser.CHAVE2)
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


    class ComandoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def CHAVE1(self):
            return self.getToken(ExprParser.CHAVE1, 0)

        def CHAVE2(self):
            return self.getToken(ExprParser.CHAVE2, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandosContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandosContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_comandoWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoWhile" ):
                listener.enterComandoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoWhile" ):
                listener.exitComandoWhile(self)




    def comandoWhile(self):

        localctx = ExprParser.ComandoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comandoWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ExprParser.WHILE)
            self.state = 139
            self.match(ExprParser.PAREN1)
            self.state = 140
            self.expressao()
            self.state = 141
            self.match(ExprParser.PAREN2)
            self.state = 142
            self.match(ExprParser.CHAVE1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046525248) != 0):
                self.state = 143
                self.comandos()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(ExprParser.CHAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def PVIRG(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PVIRG)
            else:
                return self.getToken(ExprParser.PVIRG, i)

        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def CHAVE1(self):
            return self.getToken(ExprParser.CHAVE1, 0)

        def CHAVE2(self):
            return self.getToken(ExprParser.CHAVE2, 0)

        def forInit(self):
            return self.getTypedRuleContext(ExprParser.ForInitContext,0)


        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def assignExpr(self):
            return self.getTypedRuleContext(ExprParser.AssignExprContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandosContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandosContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_comandoFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoFor" ):
                listener.enterComandoFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoFor" ):
                listener.exitComandoFor(self)




    def comandoFor(self):

        localctx = ExprParser.ComandoForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comandoFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ExprParser.FOR)
            self.state = 152
            self.match(ExprParser.PAREN1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046511166) != 0):
                self.state = 153
                self.forInit()


            self.state = 156
            self.match(ExprParser.PVIRG)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8256026099712) != 0):
                self.state = 157
                self.expressao()


            self.state = 160
            self.match(ExprParser.PVIRG)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8256026099712) != 0):
                self.state = 161
                self.assignExpr()


            self.state = 164
            self.match(ExprParser.PAREN2)
            self.state = 165
            self.match(ExprParser.CHAVE1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046525248) != 0):
                self.state = 166
                self.comandos()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(ExprParser.CHAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ATRIB(self):
            return self.getToken(ExprParser.ATRIB, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)




    def forInit(self):

        localctx = ExprParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forInit)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.tipo()
                self.state = 175
                self.match(ExprParser.ID)
                self.state = 176
                self.match(ExprParser.ATRIB)
                self.state = 177
                self.expressao()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(ExprParser.ID)
                self.state = 180
                self.match(ExprParser.ATRIB)
                self.state = 181
                self.expressao()
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


    class ComandoAtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ATRIB(self):
            return self.getToken(ExprParser.ATRIB, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)


        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def COLCH1(self):
            return self.getToken(ExprParser.COLCH1, 0)

        def COLCH2(self):
            return self.getToken(ExprParser.COLCH2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comandoAtribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoAtribuicao" ):
                listener.enterComandoAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoAtribuicao" ):
                listener.exitComandoAtribuicao(self)




    def comandoAtribuicao(self):

        localctx = ExprParser.ComandoAtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comandoAtribuicao)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(ExprParser.ID)
                self.state = 185
                self.match(ExprParser.ATRIB)
                self.state = 186
                self.expressao()
                self.state = 187
                self.match(ExprParser.PVIRG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ExprParser.ID)
                self.state = 190
                self.match(ExprParser.COLCH1)
                self.state = 191
                self.expressao()
                self.state = 192
                self.match(ExprParser.COLCH2)
                self.state = 193
                self.match(ExprParser.ATRIB)
                self.state = 194
                self.expressao()
                self.state = 195
                self.match(ExprParser.PVIRG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoPrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(ExprParser.PRINTLN, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)


        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def SOMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SOMA)
            else:
                return self.getToken(ExprParser.SOMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_comandoPrint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoPrint" ):
                listener.enterComandoPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoPrint" ):
                listener.exitComandoPrint(self)




    def comandoPrint(self):

        localctx = ExprParser.ComandoPrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comandoPrint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ExprParser.PRINTLN)
            self.state = 200
            self.match(ExprParser.PAREN1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 201
                self.expressao()
                pass

            elif la_ == 2:
                self.state = 202
                self.match(ExprParser.TEXTO)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 203
                    self.match(ExprParser.SOMA)
                    self.state = 204
                    self.expressao()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 212
            self.match(ExprParser.PAREN2)
            self.state = 213
            self.match(ExprParser.PVIRG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoScanfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCANF(self):
            return self.getToken(ExprParser.SCANF, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comandoScanf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoScanf" ):
                listener.enterComandoScanf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoScanf" ):
                listener.exitComandoScanf(self)




    def comandoScanf(self):

        localctx = ExprParser.ComandoScanfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comandoScanf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ExprParser.SCANF)
            self.state = 216
            self.match(ExprParser.PAREN1)
            self.state = 217
            self.match(ExprParser.TEXTO)
            self.state = 218
            self.match(ExprParser.VIRG)
            self.state = 219
            self.expressao()
            self.state = 220
            self.match(ExprParser.PAREN2)
            self.state = 221
            self.match(ExprParser.PVIRG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comandoReturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoReturn" ):
                listener.enterComandoReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoReturn" ):
                listener.exitComandoReturn(self)




    def comandoReturn(self):

        localctx = ExprParser.ComandoReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comandoReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ExprParser.RETURN)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8256026099712) != 0):
                self.state = 224
                self.expressao()


            self.state = 227
            self.match(ExprParser.PVIRG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(ExprParser.AssignExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = ExprParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
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


        def ATRIB(self):
            return self.getToken(ExprParser.ATRIB, 0)

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
        self.enterRule(localctx, 26, self.RULE_assignExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.logicOr()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 232
                self.match(ExprParser.ATRIB)
                self.state = 233
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
        self.enterRule(localctx, 28, self.RULE_logicOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.logicAnd()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 237
                self.match(ExprParser.OR)
                self.state = 238
                self.logicAnd()
                self.state = 243
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
        self.enterRule(localctx, 30, self.RULE_logicAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.equality()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 245
                self.match(ExprParser.AND)
                self.state = 246
                self.equality()
                self.state = 251
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


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.EQ)
            else:
                return self.getToken(ExprParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEQ)
            else:
                return self.getToken(ExprParser.NEQ, i)

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
        self.enterRule(localctx, 32, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.relational()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 253
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 254
                self.relational()
                self.state = 259
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


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LT)
            else:
                return self.getToken(ExprParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LE)
            else:
                return self.getToken(ExprParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.GT)
            else:
                return self.getToken(ExprParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.GE)
            else:
                return self.getToken(ExprParser.GE, i)

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
        self.enterRule(localctx, 34, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.add()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 261
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.add()
                self.state = 267
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


        def SOMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SOMA)
            else:
                return self.getToken(ExprParser.SOMA, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SUB)
            else:
                return self.getToken(ExprParser.SUB, i)

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
        self.enterRule(localctx, 36, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.mul()
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 270
                    self.mul() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MUL)
            else:
                return self.getToken(ExprParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIV)
            else:
                return self.getToken(ExprParser.DIV, i)

        def RESTO(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RESTO)
            else:
                return self.getToken(ExprParser.RESTO, i)

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
        self.enterRule(localctx, 38, self.RULE_mul)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.unary()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 277
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.unary()
                self.state = 283
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

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def SOMA(self):
            return self.getToken(ExprParser.SOMA, 0)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

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
        self.enterRule(localctx, 40, self.RULE_unary)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(ExprParser.SUB)
                self.state = 285
                self.unary()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(ExprParser.SOMA)
                self.state = 287
                self.unary()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.match(ExprParser.NOT)
                self.state = 289
                self.unary()
                pass
            elif token in [14, 15, 33, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
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

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def NUM_INT(self):
            return self.getToken(ExprParser.NUM_INT, 0)

        def NUM_DEC(self):
            return self.getToken(ExprParser.NUM_DEC, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def COLCH1(self):
            return self.getToken(ExprParser.COLCH1, 0)

        def COLCH2(self):
            return self.getToken(ExprParser.COLCH2, 0)

        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def TRUE(self):
            return self.getToken(ExprParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ExprParser.FALSE, 0)

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
        self.enterRule(localctx, 42, self.RULE_primary)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(ExprParser.PAREN1)
                self.state = 294
                self.expressao()
                self.state = 295
                self.match(ExprParser.PAREN2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(ExprParser.NUM_INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.match(ExprParser.NUM_DEC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.match(ExprParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.match(ExprParser.ID)
                self.state = 301
                self.match(ExprParser.COLCH1)
                self.state = 302
                self.expressao()
                self.state = 303
                self.match(ExprParser.COLCH2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 305
                self.match(ExprParser.TEXTO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 306
                self.match(ExprParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 307
                self.match(ExprParser.FALSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





