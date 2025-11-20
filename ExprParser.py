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
        4,1,43,408,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,0,1,1,1,1,3,1,99,8,1,1,2,1,2,1,2,1,2,1,2,5,2,106,8,2,10,
        2,12,2,109,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,120,8,4,1,
        5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,132,8,7,10,7,12,7,135,
        9,7,1,8,1,8,3,8,139,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,
        150,8,9,10,9,12,9,153,9,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,3,12,167,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,179,8,13,10,13,12,13,182,9,13,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,190,8,14,10,14,12,14,193,9,14,1,15,1,15,
        3,15,197,8,15,1,16,1,16,1,16,1,16,1,16,5,16,204,8,16,10,16,12,16,
        207,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,216,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,230,8,
        19,10,19,12,19,233,9,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,5,21,244,8,21,10,21,12,21,247,9,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,261,8,23,10,23,12,23,264,
        9,23,1,24,1,24,1,24,1,24,3,24,270,8,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,3,26,282,8,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,3,29,297,8,29,1,30,1,30,
        1,30,1,30,1,30,1,30,1,31,1,31,3,31,307,8,31,1,32,1,32,1,32,1,32,
        1,32,1,32,5,32,315,8,32,10,32,12,32,318,9,32,1,33,1,33,1,33,1,33,
        1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,332,8,35,10,35,12,35,
        335,9,35,1,36,1,36,1,36,1,36,1,36,1,36,5,36,343,8,36,10,36,12,36,
        346,9,36,1,37,1,37,1,37,1,37,1,37,3,37,353,8,37,1,38,1,38,1,39,1,
        39,1,39,1,39,1,39,1,39,1,39,5,39,364,8,39,10,39,12,39,367,9,39,1,
        40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,5,41,378,8,41,10,41,12,
        41,381,9,41,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,3,43,399,8,43,1,44,1,44,1,45,1,45,1,
        45,3,45,406,8,45,1,45,0,14,4,14,18,26,28,32,38,42,46,64,70,72,78,
        82,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,0,5,1,0,1,4,1,0,16,21,1,0,22,23,1,0,24,26,1,0,38,39,398,
        0,92,1,0,0,0,2,98,1,0,0,0,4,100,1,0,0,0,6,110,1,0,0,0,8,119,1,0,
        0,0,10,121,1,0,0,0,12,124,1,0,0,0,14,126,1,0,0,0,16,138,1,0,0,0,
        18,140,1,0,0,0,20,154,1,0,0,0,22,159,1,0,0,0,24,166,1,0,0,0,26,168,
        1,0,0,0,28,183,1,0,0,0,30,196,1,0,0,0,32,198,1,0,0,0,34,215,1,0,
        0,0,36,217,1,0,0,0,38,223,1,0,0,0,40,234,1,0,0,0,42,237,1,0,0,0,
        44,248,1,0,0,0,46,254,1,0,0,0,48,269,1,0,0,0,50,271,1,0,0,0,52,281,
        1,0,0,0,54,283,1,0,0,0,56,289,1,0,0,0,58,296,1,0,0,0,60,298,1,0,
        0,0,62,306,1,0,0,0,64,308,1,0,0,0,66,319,1,0,0,0,68,323,1,0,0,0,
        70,325,1,0,0,0,72,336,1,0,0,0,74,352,1,0,0,0,76,354,1,0,0,0,78,356,
        1,0,0,0,80,368,1,0,0,0,82,370,1,0,0,0,84,382,1,0,0,0,86,398,1,0,
        0,0,88,400,1,0,0,0,90,405,1,0,0,0,92,93,3,2,1,0,93,94,3,20,10,0,
        94,95,5,0,0,1,95,1,1,0,0,0,96,99,3,4,2,0,97,99,1,0,0,0,98,96,1,0,
        0,0,98,97,1,0,0,0,99,3,1,0,0,0,100,101,6,2,-1,0,101,102,3,6,3,0,
        102,107,1,0,0,0,103,104,10,1,0,0,104,106,3,6,3,0,105,103,1,0,0,0,
        106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,5,1,0,0,0,109,
        107,1,0,0,0,110,111,3,8,4,0,111,112,5,41,0,0,112,113,5,32,0,0,113,
        114,3,16,8,0,114,115,5,33,0,0,115,116,3,22,11,0,116,7,1,0,0,0,117,
        120,3,10,5,0,118,120,5,5,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,
        9,1,0,0,0,121,122,3,12,6,0,122,123,3,14,7,0,123,11,1,0,0,0,124,125,
        7,0,0,0,125,13,1,0,0,0,126,133,6,7,-1,0,127,128,10,2,0,0,128,129,
        5,36,0,0,129,130,5,39,0,0,130,132,5,37,0,0,131,127,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,15,1,0,0,0,135,133,1,
        0,0,0,136,139,3,18,9,0,137,139,1,0,0,0,138,136,1,0,0,0,138,137,1,
        0,0,0,139,17,1,0,0,0,140,141,6,9,-1,0,141,142,3,10,5,0,142,143,5,
        41,0,0,143,151,1,0,0,0,144,145,10,1,0,0,145,146,5,31,0,0,146,147,
        3,10,5,0,147,148,5,41,0,0,148,150,1,0,0,0,149,144,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,19,1,0,0,0,153,151,1,
        0,0,0,154,155,5,11,0,0,155,156,5,32,0,0,156,157,5,33,0,0,157,158,
        3,22,11,0,158,21,1,0,0,0,159,160,5,34,0,0,160,161,3,24,12,0,161,
        162,3,30,15,0,162,163,5,35,0,0,163,23,1,0,0,0,164,167,3,26,13,0,
        165,167,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,25,1,0,0,0,168,
        169,6,13,-1,0,169,170,3,10,5,0,170,171,3,28,14,0,171,172,5,30,0,
        0,172,180,1,0,0,0,173,174,10,1,0,0,174,175,3,10,5,0,175,176,3,28,
        14,0,176,177,5,30,0,0,177,179,1,0,0,0,178,173,1,0,0,0,179,182,1,
        0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,27,1,0,0,0,182,180,1,0,
        0,0,183,184,6,14,-1,0,184,185,5,41,0,0,185,191,1,0,0,0,186,187,10,
        1,0,0,187,188,5,31,0,0,188,190,5,41,0,0,189,186,1,0,0,0,190,193,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,29,1,0,0,0,193,191,1,
        0,0,0,194,197,3,32,16,0,195,197,1,0,0,0,196,194,1,0,0,0,196,195,
        1,0,0,0,197,31,1,0,0,0,198,199,6,16,-1,0,199,200,3,34,17,0,200,205,
        1,0,0,0,201,202,10,1,0,0,202,204,3,34,17,0,203,201,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,33,1,0,0,0,207,205,1,
        0,0,0,208,216,3,36,18,0,209,216,3,44,22,0,210,216,3,56,28,0,211,
        216,3,60,30,0,212,216,3,50,25,0,213,216,3,54,27,0,214,216,3,66,33,
        0,215,208,1,0,0,0,215,209,1,0,0,0,215,210,1,0,0,0,215,211,1,0,0,
        0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,0,216,35,1,0,0,0,
        217,218,5,13,0,0,218,219,5,32,0,0,219,220,3,38,19,0,220,221,5,33,
        0,0,221,222,5,30,0,0,222,37,1,0,0,0,223,224,6,19,-1,0,224,225,3,
        40,20,0,225,231,1,0,0,0,226,227,10,1,0,0,227,228,5,31,0,0,228,230,
        3,40,20,0,229,226,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,
        1,0,0,0,232,39,1,0,0,0,233,231,1,0,0,0,234,235,5,41,0,0,235,236,
        3,42,21,0,236,41,1,0,0,0,237,245,6,21,-1,0,238,239,10,2,0,0,239,
        240,5,36,0,0,240,241,3,78,39,0,241,242,5,37,0,0,242,244,1,0,0,0,
        243,238,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,
        246,43,1,0,0,0,247,245,1,0,0,0,248,249,5,12,0,0,249,250,5,32,0,0,
        250,251,3,46,23,0,251,252,5,33,0,0,252,253,5,30,0,0,253,45,1,0,0,
        0,254,255,6,23,-1,0,255,256,3,48,24,0,256,262,1,0,0,0,257,258,10,
        1,0,0,258,259,5,31,0,0,259,261,3,48,24,0,260,257,1,0,0,0,261,264,
        1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,47,1,0,0,0,264,262,1,
        0,0,0,265,266,5,41,0,0,266,270,3,42,21,0,267,270,3,88,44,0,268,270,
        5,40,0,0,269,265,1,0,0,0,269,267,1,0,0,0,269,268,1,0,0,0,270,49,
        1,0,0,0,271,272,5,6,0,0,272,273,5,32,0,0,273,274,3,68,34,0,274,275,
        5,33,0,0,275,276,3,22,11,0,276,277,3,52,26,0,277,51,1,0,0,0,278,
        279,5,7,0,0,279,282,3,22,11,0,280,282,1,0,0,0,281,278,1,0,0,0,281,
        280,1,0,0,0,282,53,1,0,0,0,283,284,5,9,0,0,284,285,5,32,0,0,285,
        286,3,68,34,0,286,287,5,33,0,0,287,288,3,22,11,0,288,55,1,0,0,0,
        289,290,5,41,0,0,290,291,5,15,0,0,291,292,3,58,29,0,292,293,5,30,
        0,0,293,57,1,0,0,0,294,297,3,68,34,0,295,297,3,60,30,0,296,294,1,
        0,0,0,296,295,1,0,0,0,297,59,1,0,0,0,298,299,5,14,0,0,299,300,5,
        41,0,0,300,301,5,32,0,0,301,302,3,62,31,0,302,303,5,33,0,0,303,61,
        1,0,0,0,304,307,3,64,32,0,305,307,1,0,0,0,306,304,1,0,0,0,306,305,
        1,0,0,0,307,63,1,0,0,0,308,309,6,32,-1,0,309,310,3,68,34,0,310,316,
        1,0,0,0,311,312,10,1,0,0,312,313,5,31,0,0,313,315,3,68,34,0,314,
        311,1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,
        65,1,0,0,0,318,316,1,0,0,0,319,320,5,10,0,0,320,321,3,68,34,0,321,
        322,5,30,0,0,322,67,1,0,0,0,323,324,3,70,35,0,324,69,1,0,0,0,325,
        326,6,35,-1,0,326,327,3,72,36,0,327,333,1,0,0,0,328,329,10,1,0,0,
        329,330,5,28,0,0,330,332,3,72,36,0,331,328,1,0,0,0,332,335,1,0,0,
        0,333,331,1,0,0,0,333,334,1,0,0,0,334,71,1,0,0,0,335,333,1,0,0,0,
        336,337,6,36,-1,0,337,338,3,74,37,0,338,344,1,0,0,0,339,340,10,1,
        0,0,340,341,5,27,0,0,341,343,3,74,37,0,342,339,1,0,0,0,343,346,1,
        0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,73,1,0,0,0,346,344,1,0,
        0,0,347,353,3,78,39,0,348,349,3,78,39,0,349,350,3,76,38,0,350,351,
        3,78,39,0,351,353,1,0,0,0,352,347,1,0,0,0,352,348,1,0,0,0,353,75,
        1,0,0,0,354,355,7,1,0,0,355,77,1,0,0,0,356,357,6,39,-1,0,357,358,
        3,82,41,0,358,365,1,0,0,0,359,360,10,1,0,0,360,361,3,80,40,0,361,
        362,3,82,41,0,362,364,1,0,0,0,363,359,1,0,0,0,364,367,1,0,0,0,365,
        363,1,0,0,0,365,366,1,0,0,0,366,79,1,0,0,0,367,365,1,0,0,0,368,369,
        7,2,0,0,369,81,1,0,0,0,370,371,6,41,-1,0,371,372,3,86,43,0,372,379,
        1,0,0,0,373,374,10,1,0,0,374,375,3,84,42,0,375,376,3,86,43,0,376,
        378,1,0,0,0,377,373,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,
        380,1,0,0,0,380,83,1,0,0,0,381,379,1,0,0,0,382,383,7,3,0,0,383,85,
        1,0,0,0,384,385,3,90,45,0,385,386,5,41,0,0,386,387,3,42,21,0,387,
        399,1,0,0,0,388,389,3,90,45,0,389,390,3,88,44,0,390,399,1,0,0,0,
        391,399,5,40,0,0,392,393,5,29,0,0,393,399,3,86,43,0,394,395,5,32,
        0,0,395,396,3,68,34,0,396,397,5,33,0,0,397,399,1,0,0,0,398,384,1,
        0,0,0,398,388,1,0,0,0,398,391,1,0,0,0,398,392,1,0,0,0,398,394,1,
        0,0,0,399,87,1,0,0,0,400,401,7,4,0,0,401,89,1,0,0,0,402,406,5,22,
        0,0,403,406,5,23,0,0,404,406,1,0,0,0,405,402,1,0,0,0,405,403,1,0,
        0,0,405,404,1,0,0,0,406,91,1,0,0,0,27,98,107,119,133,138,151,166,
        180,191,196,205,215,231,245,262,269,281,296,306,316,333,344,352,
        365,379,398,405
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'char'", "'boolean'", 
                     "'void'", "'if'", "'else'", "'for'", "'while'", "'return'", 
                     "'main'", "'println'", "'scanf'", "'func'", "'='", 
                     "'=='", "'!='", "'<='", "'<'", "'>='", "'>'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'!'", 
                     "';'", "','", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "CHAR", "BOOLEAN", "VOID", 
                      "IF", "ELSE", "FOR", "WHILE", "RETURN", "MAIN", "PRINTLN", 
                      "SCANF", "FUNC", "ATRIB", "EQ", "NEQ", "LE", "LT", 
                      "GE", "GT", "SOMA", "SUB", "MUL", "DIV", "RESTO", 
                      "AND", "OR", "NOT", "PVIRG", "VIRG", "PAREN1", "PAREN2", 
                      "CHAVE1", "CHAVE2", "COLCH1", "COLCH2", "NUM_DEC", 
                      "NUM_INT", "TEXTO", "ID", "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_secaoFuncoes = 1
    RULE_listaFuncoes = 2
    RULE_decFuncao = 3
    RULE_tipoRetorno = 4
    RULE_tipo = 5
    RULE_tipoBase = 6
    RULE_dimensao = 7
    RULE_parametros = 8
    RULE_listaParametros = 9
    RULE_principal = 10
    RULE_bloco = 11
    RULE_secaoVariaveis = 12
    RULE_listaVariaveis = 13
    RULE_listaId = 14
    RULE_secaoComandos = 15
    RULE_listaComandos = 16
    RULE_comando = 17
    RULE_leitura = 18
    RULE_listaTermoLeitura = 19
    RULE_termoLeitura = 20
    RULE_dimensao2 = 21
    RULE_escrita = 22
    RULE_listaTermoEscrita = 23
    RULE_termoEscrita = 24
    RULE_selecao = 25
    RULE_senao = 26
    RULE_enquanto = 27
    RULE_atribuicao = 28
    RULE_complemento = 29
    RULE_chamadaFuncao = 30
    RULE_argumentos = 31
    RULE_listaArgumentos = 32
    RULE_retorno = 33
    RULE_expressao = 34
    RULE_exprOu = 35
    RULE_exprE = 36
    RULE_exprRelacional = 37
    RULE_opRelacional = 38
    RULE_exprAditiva = 39
    RULE_opAditivo = 40
    RULE_exprMultiplicativa = 41
    RULE_opMultiplicativo = 42
    RULE_fator = 43
    RULE_constante = 44
    RULE_sinal = 45

    ruleNames =  [ "programa", "secaoFuncoes", "listaFuncoes", "decFuncao", 
                   "tipoRetorno", "tipo", "tipoBase", "dimensao", "parametros", 
                   "listaParametros", "principal", "bloco", "secaoVariaveis", 
                   "listaVariaveis", "listaId", "secaoComandos", "listaComandos", 
                   "comando", "leitura", "listaTermoLeitura", "termoLeitura", 
                   "dimensao2", "escrita", "listaTermoEscrita", "termoEscrita", 
                   "selecao", "senao", "enquanto", "atribuicao", "complemento", 
                   "chamadaFuncao", "argumentos", "listaArgumentos", "retorno", 
                   "expressao", "exprOu", "exprE", "exprRelacional", "opRelacional", 
                   "exprAditiva", "opAditivo", "exprMultiplicativa", "opMultiplicativo", 
                   "fator", "constante", "sinal" ]

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
    FUNC=14
    ATRIB=15
    EQ=16
    NEQ=17
    LE=18
    LT=19
    GE=20
    GT=21
    SOMA=22
    SUB=23
    MUL=24
    DIV=25
    RESTO=26
    AND=27
    OR=28
    NOT=29
    PVIRG=30
    VIRG=31
    PAREN1=32
    PAREN2=33
    CHAVE1=34
    CHAVE2=35
    COLCH1=36
    COLCH2=37
    NUM_DEC=38
    NUM_INT=39
    TEXTO=40
    ID=41
    COMMENT=42
    WS=43

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

        def secaoFuncoes(self):
            return self.getTypedRuleContext(ExprParser.SecaoFuncoesContext,0)


        def principal(self):
            return self.getTypedRuleContext(ExprParser.PrincipalContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.secaoFuncoes()
            self.state = 93
            self.principal()
            self.state = 94
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecaoFuncoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaFuncoes(self):
            return self.getTypedRuleContext(ExprParser.ListaFuncoesContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_secaoFuncoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecaoFuncoes" ):
                listener.enterSecaoFuncoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecaoFuncoes" ):
                listener.exitSecaoFuncoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecaoFuncoes" ):
                return visitor.visitSecaoFuncoes(self)
            else:
                return visitor.visitChildren(self)




    def secaoFuncoes(self):

        localctx = ExprParser.SecaoFuncoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_secaoFuncoes)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.listaFuncoes(0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaFuncoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decFuncao(self):
            return self.getTypedRuleContext(ExprParser.DecFuncaoContext,0)


        def listaFuncoes(self):
            return self.getTypedRuleContext(ExprParser.ListaFuncoesContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listaFuncoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaFuncoes" ):
                listener.enterListaFuncoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaFuncoes" ):
                listener.exitListaFuncoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaFuncoes" ):
                return visitor.visitListaFuncoes(self)
            else:
                return visitor.visitChildren(self)



    def listaFuncoes(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaFuncoesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_listaFuncoes, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.decFuncao()
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaFuncoesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaFuncoes)
                    self.state = 103
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 104
                    self.decFuncao() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DecFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoRetorno(self):
            return self.getTypedRuleContext(ExprParser.TipoRetornoContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def parametros(self):
            return self.getTypedRuleContext(ExprParser.ParametrosContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_decFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecFuncao" ):
                listener.enterDecFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecFuncao" ):
                listener.exitDecFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecFuncao" ):
                return visitor.visitDecFuncao(self)
            else:
                return visitor.visitChildren(self)




    def decFuncao(self):

        localctx = ExprParser.DecFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decFuncao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.tipoRetorno()
            self.state = 111
            self.match(ExprParser.ID)
            self.state = 112
            self.match(ExprParser.PAREN1)
            self.state = 113
            self.parametros()
            self.state = 114
            self.match(ExprParser.PAREN2)
            self.state = 115
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def VOID(self):
            return self.getToken(ExprParser.VOID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_tipoRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoRetorno" ):
                listener.enterTipoRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoRetorno" ):
                listener.exitTipoRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoRetorno" ):
                return visitor.visitTipoRetorno(self)
            else:
                return visitor.visitChildren(self)




    def tipoRetorno(self):

        localctx = ExprParser.TipoRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipoRetorno)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.tipo()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(ExprParser.VOID)
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


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoBase(self):
            return self.getTypedRuleContext(ExprParser.TipoBaseContext,0)


        def dimensao(self):
            return self.getTypedRuleContext(ExprParser.DimensaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = ExprParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.tipoBase()
            self.state = 122
            self.dimensao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoBaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(ExprParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_tipoBase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoBase" ):
                listener.enterTipoBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoBase" ):
                listener.exitTipoBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoBase" ):
                return visitor.visitTipoBase(self)
            else:
                return visitor.visitChildren(self)




    def tipoBase(self):

        localctx = ExprParser.TipoBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoBase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
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


    class DimensaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensao(self):
            return self.getTypedRuleContext(ExprParser.DimensaoContext,0)


        def COLCH1(self):
            return self.getToken(ExprParser.COLCH1, 0)

        def NUM_INT(self):
            return self.getToken(ExprParser.NUM_INT, 0)

        def COLCH2(self):
            return self.getToken(ExprParser.COLCH2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_dimensao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao" ):
                listener.enterDimensao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao" ):
                listener.exitDimensao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensao" ):
                return visitor.visitDimensao(self)
            else:
                return visitor.visitChildren(self)



    def dimensao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.DimensaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_dimensao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.DimensaoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dimensao)
                    self.state = 127
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 128
                    self.match(ExprParser.COLCH1)
                    self.state = 129
                    self.match(ExprParser.NUM_INT)
                    self.state = 130
                    self.match(ExprParser.COLCH2) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaParametros(self):
            return self.getTypedRuleContext(ExprParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = ExprParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametros)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.listaParametros(0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def listaParametros(self):
            return self.getTypedRuleContext(ExprParser.ListaParametrosContext,0)


        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_listaParametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParametros" ):
                listener.enterListaParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParametros" ):
                listener.exitListaParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)



    def listaParametros(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaParametrosContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_listaParametros, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.tipo()
            self.state = 142
            self.match(ExprParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaParametrosContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaParametros)
                    self.state = 144
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 145
                    self.match(ExprParser.VIRG)
                    self.state = 146
                    self.tipo()
                    self.state = 147
                    self.match(ExprParser.ID) 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrincipalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_principal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrincipal" ):
                listener.enterPrincipal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrincipal" ):
                listener.exitPrincipal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrincipal" ):
                return visitor.visitPrincipal(self)
            else:
                return visitor.visitChildren(self)




    def principal(self):

        localctx = ExprParser.PrincipalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_principal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ExprParser.MAIN)
            self.state = 155
            self.match(ExprParser.PAREN1)
            self.state = 156
            self.match(ExprParser.PAREN2)
            self.state = 157
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAVE1(self):
            return self.getToken(ExprParser.CHAVE1, 0)

        def secaoVariaveis(self):
            return self.getTypedRuleContext(ExprParser.SecaoVariaveisContext,0)


        def secaoComandos(self):
            return self.getTypedRuleContext(ExprParser.SecaoComandosContext,0)


        def CHAVE2(self):
            return self.getToken(ExprParser.CHAVE2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = ExprParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bloco)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ExprParser.CHAVE1)
            self.state = 160
            self.secaoVariaveis()
            self.state = 161
            self.secaoComandos()
            self.state = 162
            self.match(ExprParser.CHAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecaoVariaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaVariaveis(self):
            return self.getTypedRuleContext(ExprParser.ListaVariaveisContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_secaoVariaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecaoVariaveis" ):
                listener.enterSecaoVariaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecaoVariaveis" ):
                listener.exitSecaoVariaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecaoVariaveis" ):
                return visitor.visitSecaoVariaveis(self)
            else:
                return visitor.visitChildren(self)




    def secaoVariaveis(self):

        localctx = ExprParser.SecaoVariaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_secaoVariaveis)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.listaVariaveis(0)
                pass
            elif token in [6, 9, 10, 12, 13, 14, 35, 41]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaVariaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def listaId(self):
            return self.getTypedRuleContext(ExprParser.ListaIdContext,0)


        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def listaVariaveis(self):
            return self.getTypedRuleContext(ExprParser.ListaVariaveisContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listaVariaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaVariaveis" ):
                listener.enterListaVariaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaVariaveis" ):
                listener.exitListaVariaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaVariaveis" ):
                return visitor.visitListaVariaveis(self)
            else:
                return visitor.visitChildren(self)



    def listaVariaveis(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaVariaveisContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_listaVariaveis, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.tipo()
            self.state = 170
            self.listaId(0)
            self.state = 171
            self.match(ExprParser.PVIRG)
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaVariaveisContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaVariaveis)
                    self.state = 173
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 174
                    self.tipo()
                    self.state = 175
                    self.listaId(0)
                    self.state = 176
                    self.match(ExprParser.PVIRG) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListaIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def listaId(self):
            return self.getTypedRuleContext(ExprParser.ListaIdContext,0)


        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_listaId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaId" ):
                listener.enterListaId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaId" ):
                listener.exitListaId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaId" ):
                return visitor.visitListaId(self)
            else:
                return visitor.visitChildren(self)



    def listaId(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaIdContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_listaId, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ExprParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaIdContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaId)
                    self.state = 186
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 187
                    self.match(ExprParser.VIRG)
                    self.state = 188
                    self.match(ExprParser.ID) 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SecaoComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaComandos(self):
            return self.getTypedRuleContext(ExprParser.ListaComandosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_secaoComandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecaoComandos" ):
                listener.enterSecaoComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecaoComandos" ):
                listener.exitSecaoComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecaoComandos" ):
                return visitor.visitSecaoComandos(self)
            else:
                return visitor.visitChildren(self)




    def secaoComandos(self):

        localctx = ExprParser.SecaoComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_secaoComandos)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 9, 10, 12, 13, 14, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.listaComandos(0)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self):
            return self.getTypedRuleContext(ExprParser.ComandoContext,0)


        def listaComandos(self):
            return self.getTypedRuleContext(ExprParser.ListaComandosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_listaComandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaComandos" ):
                listener.enterListaComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaComandos" ):
                listener.exitListaComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaComandos" ):
                return visitor.visitListaComandos(self)
            else:
                return visitor.visitChildren(self)



    def listaComandos(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaComandosContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_listaComandos, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.comando()
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaComandosContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaComandos)
                    self.state = 201
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 202
                    self.comando() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leitura(self):
            return self.getTypedRuleContext(ExprParser.LeituraContext,0)


        def escrita(self):
            return self.getTypedRuleContext(ExprParser.EscritaContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(ExprParser.AtribuicaoContext,0)


        def chamadaFuncao(self):
            return self.getTypedRuleContext(ExprParser.ChamadaFuncaoContext,0)


        def selecao(self):
            return self.getTypedRuleContext(ExprParser.SelecaoContext,0)


        def enquanto(self):
            return self.getTypedRuleContext(ExprParser.EnquantoContext,0)


        def retorno(self):
            return self.getTypedRuleContext(ExprParser.RetornoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = ExprParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comando)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.leitura()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.escrita()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.atribuicao()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.chamadaFuncao()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.selecao()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.enquanto()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.retorno()
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


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCANF(self):
            return self.getToken(ExprParser.SCANF, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def listaTermoLeitura(self):
            return self.getTypedRuleContext(ExprParser.ListaTermoLeituraContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeitura" ):
                return visitor.visitLeitura(self)
            else:
                return visitor.visitChildren(self)




    def leitura(self):

        localctx = ExprParser.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ExprParser.SCANF)
            self.state = 218
            self.match(ExprParser.PAREN1)
            self.state = 219
            self.listaTermoLeitura(0)
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


    class ListaTermoLeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termoLeitura(self):
            return self.getTypedRuleContext(ExprParser.TermoLeituraContext,0)


        def listaTermoLeitura(self):
            return self.getTypedRuleContext(ExprParser.ListaTermoLeituraContext,0)


        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_listaTermoLeitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaTermoLeitura" ):
                listener.enterListaTermoLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaTermoLeitura" ):
                listener.exitListaTermoLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaTermoLeitura" ):
                return visitor.visitListaTermoLeitura(self)
            else:
                return visitor.visitChildren(self)



    def listaTermoLeitura(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaTermoLeituraContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_listaTermoLeitura, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.termoLeitura()
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaTermoLeituraContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaTermoLeitura)
                    self.state = 226
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 227
                    self.match(ExprParser.VIRG)
                    self.state = 228
                    self.termoLeitura() 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoLeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def dimensao2(self):
            return self.getTypedRuleContext(ExprParser.Dimensao2Context,0)


        def getRuleIndex(self):
            return ExprParser.RULE_termoLeitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoLeitura" ):
                listener.enterTermoLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoLeitura" ):
                listener.exitTermoLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoLeitura" ):
                return visitor.visitTermoLeitura(self)
            else:
                return visitor.visitChildren(self)




    def termoLeitura(self):

        localctx = ExprParser.TermoLeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_termoLeitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ExprParser.ID)
            self.state = 235
            self.dimensao2(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimensao2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensao2(self):
            return self.getTypedRuleContext(ExprParser.Dimensao2Context,0)


        def COLCH1(self):
            return self.getToken(ExprParser.COLCH1, 0)

        def exprAditiva(self):
            return self.getTypedRuleContext(ExprParser.ExprAditivaContext,0)


        def COLCH2(self):
            return self.getToken(ExprParser.COLCH2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_dimensao2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao2" ):
                listener.enterDimensao2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao2" ):
                listener.exitDimensao2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensao2" ):
                return visitor.visitDimensao2(self)
            else:
                return visitor.visitChildren(self)



    def dimensao2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.Dimensao2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_dimensao2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.Dimensao2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dimensao2)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    self.match(ExprParser.COLCH1)
                    self.state = 240
                    self.exprAditiva(0)
                    self.state = 241
                    self.match(ExprParser.COLCH2) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(ExprParser.PRINTLN, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def listaTermoEscrita(self):
            return self.getTypedRuleContext(ExprParser.ListaTermoEscritaContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscrita" ):
                return visitor.visitEscrita(self)
            else:
                return visitor.visitChildren(self)




    def escrita(self):

        localctx = ExprParser.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_escrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ExprParser.PRINTLN)
            self.state = 249
            self.match(ExprParser.PAREN1)
            self.state = 250
            self.listaTermoEscrita(0)
            self.state = 251
            self.match(ExprParser.PAREN2)
            self.state = 252
            self.match(ExprParser.PVIRG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaTermoEscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termoEscrita(self):
            return self.getTypedRuleContext(ExprParser.TermoEscritaContext,0)


        def listaTermoEscrita(self):
            return self.getTypedRuleContext(ExprParser.ListaTermoEscritaContext,0)


        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_listaTermoEscrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaTermoEscrita" ):
                listener.enterListaTermoEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaTermoEscrita" ):
                listener.exitListaTermoEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaTermoEscrita" ):
                return visitor.visitListaTermoEscrita(self)
            else:
                return visitor.visitChildren(self)



    def listaTermoEscrita(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaTermoEscritaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_listaTermoEscrita, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.termoEscrita()
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaTermoEscritaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaTermoEscrita)
                    self.state = 257
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 258
                    self.match(ExprParser.VIRG)
                    self.state = 259
                    self.termoEscrita() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoEscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def dimensao2(self):
            return self.getTypedRuleContext(ExprParser.Dimensao2Context,0)


        def constante(self):
            return self.getTypedRuleContext(ExprParser.ConstanteContext,0)


        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_termoEscrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoEscrita" ):
                listener.enterTermoEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoEscrita" ):
                listener.exitTermoEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoEscrita" ):
                return visitor.visitTermoEscrita(self)
            else:
                return visitor.visitChildren(self)




    def termoEscrita(self):

        localctx = ExprParser.TermoEscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_termoEscrita)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ExprParser.ID)
                self.state = 266
                self.dimensao2(0)
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.constante()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
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


    class SelecaoContext(ParserRuleContext):
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

        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def senao(self):
            return self.getTypedRuleContext(ExprParser.SenaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_selecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelecao" ):
                listener.enterSelecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelecao" ):
                listener.exitSelecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelecao" ):
                return visitor.visitSelecao(self)
            else:
                return visitor.visitChildren(self)




    def selecao(self):

        localctx = ExprParser.SelecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_selecao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(ExprParser.IF)
            self.state = 272
            self.match(ExprParser.PAREN1)
            self.state = 273
            self.expressao()
            self.state = 274
            self.match(ExprParser.PAREN2)
            self.state = 275
            self.bloco()
            self.state = 276
            self.senao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SenaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_senao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSenao" ):
                listener.enterSenao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSenao" ):
                listener.exitSenao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSenao" ):
                return visitor.visitSenao(self)
            else:
                return visitor.visitChildren(self)




    def senao(self):

        localctx = ExprParser.SenaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_senao)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(ExprParser.ELSE)
                self.state = 279
                self.bloco()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnquantoContext(ParserRuleContext):
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

        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnquanto" ):
                listener.enterEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnquanto" ):
                listener.exitEnquanto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquanto" ):
                return visitor.visitEnquanto(self)
            else:
                return visitor.visitChildren(self)




    def enquanto(self):

        localctx = ExprParser.EnquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_enquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ExprParser.WHILE)
            self.state = 284
            self.match(ExprParser.PAREN1)
            self.state = 285
            self.expressao()
            self.state = 286
            self.match(ExprParser.PAREN2)
            self.state = 287
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ATRIB(self):
            return self.getToken(ExprParser.ATRIB, 0)

        def complemento(self):
            return self.getTypedRuleContext(ExprParser.ComplementoContext,0)


        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = ExprParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ExprParser.ID)
            self.state = 290
            self.match(ExprParser.ATRIB)
            self.state = 291
            self.complemento()
            self.state = 292
            self.match(ExprParser.PVIRG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def chamadaFuncao(self):
            return self.getTypedRuleContext(ExprParser.ChamadaFuncaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_complemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento" ):
                listener.enterComplemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento" ):
                listener.exitComplemento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplemento" ):
                return visitor.visitComplemento(self)
            else:
                return visitor.visitChildren(self)




    def complemento(self):

        localctx = ExprParser.ComplementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_complemento)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 29, 32, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expressao()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.chamadaFuncao()
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


    class ChamadaFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ExprParser.FUNC, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ExprParser.ArgumentosContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_chamadaFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaFuncao" ):
                listener.enterChamadaFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaFuncao" ):
                listener.exitChamadaFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChamadaFuncao" ):
                return visitor.visitChamadaFuncao(self)
            else:
                return visitor.visitChildren(self)




    def chamadaFuncao(self):

        localctx = ExprParser.ChamadaFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_chamadaFuncao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(ExprParser.FUNC)
            self.state = 299
            self.match(ExprParser.ID)
            self.state = 300
            self.match(ExprParser.PAREN1)
            self.state = 301
            self.argumentos()
            self.state = 302
            self.match(ExprParser.PAREN2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaArgumentos(self):
            return self.getTypedRuleContext(ExprParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = ExprParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_argumentos)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 29, 32, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.listaArgumentos(0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def listaArgumentos(self):
            return self.getTypedRuleContext(ExprParser.ListaArgumentosContext,0)


        def VIRG(self):
            return self.getToken(ExprParser.VIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_listaArgumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgumentos" ):
                listener.enterListaArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgumentos" ):
                listener.exitListaArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgumentos" ):
                return visitor.visitListaArgumentos(self)
            else:
                return visitor.visitChildren(self)



    def listaArgumentos(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ListaArgumentosContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_listaArgumentos, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expressao()
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ListaArgumentosContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listaArgumentos)
                    self.state = 311
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 312
                    self.match(ExprParser.VIRG)
                    self.state = 313
                    self.expressao() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PVIRG(self):
            return self.getToken(ExprParser.PVIRG, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = ExprParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ExprParser.RETURN)
            self.state = 320
            self.expressao()
            self.state = 321
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

        def exprOu(self):
            return self.getTypedRuleContext(ExprParser.ExprOuContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = ExprParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.exprOu(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprOuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprE(self):
            return self.getTypedRuleContext(ExprParser.ExprEContext,0)


        def exprOu(self):
            return self.getTypedRuleContext(ExprParser.ExprOuContext,0)


        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exprOu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOu" ):
                listener.enterExprOu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOu" ):
                listener.exitExprOu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOu" ):
                return visitor.visitExprOu(self)
            else:
                return visitor.visitChildren(self)



    def exprOu(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprOuContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exprOu, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.exprE(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprOuContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprOu)
                    self.state = 328
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 329
                    self.match(ExprParser.OR)
                    self.state = 330
                    self.exprE(0) 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprRelacional(self):
            return self.getTypedRuleContext(ExprParser.ExprRelacionalContext,0)


        def exprE(self):
            return self.getTypedRuleContext(ExprParser.ExprEContext,0)


        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exprE

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprE" ):
                listener.enterExprE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprE" ):
                listener.exitExprE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprE" ):
                return visitor.visitExprE(self)
            else:
                return visitor.visitChildren(self)



    def exprE(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprEContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exprE, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.exprRelacional()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprEContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprE)
                    self.state = 339
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 340
                    self.match(ExprParser.AND)
                    self.state = 341
                    self.exprRelacional() 
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprAditiva(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprAditivaContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprAditivaContext,i)


        def opRelacional(self):
            return self.getTypedRuleContext(ExprParser.OpRelacionalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exprRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacional" ):
                listener.enterExprRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacional" ):
                listener.exitExprRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacional" ):
                return visitor.visitExprRelacional(self)
            else:
                return visitor.visitChildren(self)




    def exprRelacional(self):

        localctx = ExprParser.ExprRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exprRelacional)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.exprAditiva(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.exprAditiva(0)
                self.state = 349
                self.opRelacional()
                self.state = 350
                self.exprAditiva(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ExprParser.LT, 0)

        def LE(self):
            return self.getToken(ExprParser.LE, 0)

        def GT(self):
            return self.getToken(ExprParser.GT, 0)

        def GE(self):
            return self.getToken(ExprParser.GE, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_opRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpRelacional" ):
                listener.enterOpRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpRelacional" ):
                listener.exitOpRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpRelacional" ):
                return visitor.visitOpRelacional(self)
            else:
                return visitor.visitChildren(self)




    def opRelacional(self):

        localctx = ExprParser.OpRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_opRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
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


    class ExprAditivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprMultiplicativa(self):
            return self.getTypedRuleContext(ExprParser.ExprMultiplicativaContext,0)


        def exprAditiva(self):
            return self.getTypedRuleContext(ExprParser.ExprAditivaContext,0)


        def opAditivo(self):
            return self.getTypedRuleContext(ExprParser.OpAditivoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exprAditiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAditiva" ):
                listener.enterExprAditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAditiva" ):
                listener.exitExprAditiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAditiva" ):
                return visitor.visitExprAditiva(self)
            else:
                return visitor.visitChildren(self)



    def exprAditiva(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprAditivaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exprAditiva, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.exprMultiplicativa(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprAditivaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprAditiva)
                    self.state = 359
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 360
                    self.opAditivo()
                    self.state = 361
                    self.exprMultiplicativa(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpAditivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOMA(self):
            return self.getToken(ExprParser.SOMA, 0)

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_opAditivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAditivo" ):
                listener.enterOpAditivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAditivo" ):
                listener.exitOpAditivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAditivo" ):
                return visitor.visitOpAditivo(self)
            else:
                return visitor.visitChildren(self)




    def opAditivo(self):

        localctx = ExprParser.OpAditivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_opAditivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class ExprMultiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(ExprParser.FatorContext,0)


        def exprMultiplicativa(self):
            return self.getTypedRuleContext(ExprParser.ExprMultiplicativaContext,0)


        def opMultiplicativo(self):
            return self.getTypedRuleContext(ExprParser.OpMultiplicativoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exprMultiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultiplicativa" ):
                listener.enterExprMultiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultiplicativa" ):
                listener.exitExprMultiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultiplicativa" ):
                return visitor.visitExprMultiplicativa(self)
            else:
                return visitor.visitChildren(self)



    def exprMultiplicativa(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprMultiplicativaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exprMultiplicativa, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.fator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprMultiplicativaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprMultiplicativa)
                    self.state = 373
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 374
                    self.opMultiplicativo()
                    self.state = 375
                    self.fator() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpMultiplicativoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def RESTO(self):
            return self.getToken(ExprParser.RESTO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_opMultiplicativo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMultiplicativo" ):
                listener.enterOpMultiplicativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMultiplicativo" ):
                listener.exitOpMultiplicativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMultiplicativo" ):
                return visitor.visitOpMultiplicativo(self)
            else:
                return visitor.visitChildren(self)




    def opMultiplicativo(self):

        localctx = ExprParser.OpMultiplicativoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_opMultiplicativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
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


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sinal(self):
            return self.getTypedRuleContext(ExprParser.SinalContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def dimensao2(self):
            return self.getTypedRuleContext(ExprParser.Dimensao2Context,0)


        def constante(self):
            return self.getTypedRuleContext(ExprParser.ConstanteContext,0)


        def TEXTO(self):
            return self.getToken(ExprParser.TEXTO, 0)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def fator(self):
            return self.getTypedRuleContext(ExprParser.FatorContext,0)


        def PAREN1(self):
            return self.getToken(ExprParser.PAREN1, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def PAREN2(self):
            return self.getToken(ExprParser.PAREN2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = ExprParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_fator)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.sinal()
                self.state = 385
                self.match(ExprParser.ID)
                self.state = 386
                self.dimensao2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.sinal()
                self.state = 389
                self.constante()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.match(ExprParser.TEXTO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 392
                self.match(ExprParser.NOT)
                self.state = 393
                self.fator()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 394
                self.match(ExprParser.PAREN1)
                self.state = 395
                self.expressao()
                self.state = 396
                self.match(ExprParser.PAREN2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(ExprParser.NUM_INT, 0)

        def NUM_DEC(self):
            return self.getToken(ExprParser.NUM_DEC, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_constante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstante" ):
                listener.enterConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstante" ):
                listener.exitConstante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstante" ):
                return visitor.visitConstante(self)
            else:
                return visitor.visitChildren(self)




    def constante(self):

        localctx = ExprParser.ConstanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_constante)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
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


    class SinalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOMA(self):
            return self.getToken(ExprParser.SOMA, 0)

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_sinal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinal" ):
                listener.enterSinal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinal" ):
                listener.exitSinal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinal" ):
                return visitor.visitSinal(self)
            else:
                return visitor.visitChildren(self)




    def sinal(self):

        localctx = ExprParser.SinalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_sinal)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(ExprParser.SOMA)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.match(ExprParser.SUB)
                pass
            elif token in [38, 39, 41]:
                self.enterOuterAlt(localctx, 3)

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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.listaFuncoes_sempred
        self._predicates[7] = self.dimensao_sempred
        self._predicates[9] = self.listaParametros_sempred
        self._predicates[13] = self.listaVariaveis_sempred
        self._predicates[14] = self.listaId_sempred
        self._predicates[16] = self.listaComandos_sempred
        self._predicates[19] = self.listaTermoLeitura_sempred
        self._predicates[21] = self.dimensao2_sempred
        self._predicates[23] = self.listaTermoEscrita_sempred
        self._predicates[32] = self.listaArgumentos_sempred
        self._predicates[35] = self.exprOu_sempred
        self._predicates[36] = self.exprE_sempred
        self._predicates[39] = self.exprAditiva_sempred
        self._predicates[41] = self.exprMultiplicativa_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def listaFuncoes_sempred(self, localctx:ListaFuncoesContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def dimensao_sempred(self, localctx:DimensaoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def listaParametros_sempred(self, localctx:ListaParametrosContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def listaVariaveis_sempred(self, localctx:ListaVariaveisContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def listaId_sempred(self, localctx:ListaIdContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def listaComandos_sempred(self, localctx:ListaComandosContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def listaTermoLeitura_sempred(self, localctx:ListaTermoLeituraContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def dimensao2_sempred(self, localctx:Dimensao2Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def listaTermoEscrita_sempred(self, localctx:ListaTermoEscritaContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def listaArgumentos_sempred(self, localctx:ListaArgumentosContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def exprOu_sempred(self, localctx:ExprOuContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def exprE_sempred(self, localctx:ExprEContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def exprAditiva_sempred(self, localctx:ExprAditivaContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def exprMultiplicativa_sempred(self, localctx:ExprMultiplicativaContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         




