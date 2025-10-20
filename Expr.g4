grammar Expr;

// -------------------- Parser Rules --------------------

programa
    : secaoFuncoes principal EOF
    ;

secaoFuncoes
    : listaFuncoes
    | /* vazio */
    ;

listaFuncoes
    : decFuncao
    | listaFuncoes decFuncao
    ;

decFuncao
    : tipoRetorno ID PAREN1 parametros PAREN2 bloco
    ;

tipoRetorno
    : tipo
    | VOID
    ;

tipo
    : tipoBase dimensao
    ;

tipoBase
    : CHAR
    | FLOAT
    | INT
    | BOOLEAN
    ;

dimensao
    : dimensao COLCH1 NUM_INT COLCH2
    | /* vazio */
    ;

parametros
    : listaParametros
    | /* vazio */
    ;

listaParametros
    : tipo ID
    | listaParametros VIRG tipo ID
    ;

principal
    : MAIN PAREN1 PAREN2 bloco
    ;

bloco
    : CHAVE1 secaoVariaveis secaoComandos CHAVE2
    ;

secaoVariaveis
    : listaVariaveis
    | /* vazio */
    ;

listaVariaveis
    : tipo listaId PVIRG
    | listaVariaveis tipo listaId PVIRG
    ;

listaId
    : ID
    | listaId VIRG ID
    ;

secaoComandos
    : listaComandos
    | /* vazio */
    ;

listaComandos
    : comando
    | listaComandos comando
    ;

comando
    : leitura
    | escrita
    | atribuicao
    | chamadaFuncao
    | selecao
    | enquanto
    | retorno
    ;

leitura
    : SCANF PAREN1 listaTermoLeitura PAREN2 PVIRG
    ;

listaTermoLeitura
    : termoLeitura
    | listaTermoLeitura VIRG termoLeitura
    ;

termoLeitura
    : ID dimensao2
    ;

dimensao2
    : dimensao2 COLCH1 exprAditiva COLCH2
    | /* vazio */
    ;

escrita
    : PRINTLN PAREN1 listaTermoEscrita PAREN2 PVIRG
    ;

listaTermoEscrita
    : termoEscrita
    | listaTermoEscrita VIRG termoEscrita
    ;

termoEscrita
    : ID dimensao2
    | constante
    | TEXTO
    ;

selecao
    : IF PAREN1 expressao PAREN2 bloco senao
    ;

senao
    : ELSE bloco
    | /* vazio */
    ;

enquanto
    : WHILE PAREN1 expressao PAREN2 bloco
    ;

atribuicao
    : ID ATRIB complemento PVIRG
    ;

complemento
    : expressao
    | chamadaFuncao
    ;

chamadaFuncao
    : FUNC ID PAREN1 argumentos PAREN2
    ;

argumentos
    : listaArgumentos
    | /* vazio */
    ;

listaArgumentos
    : expressao
    | listaArgumentos VIRG expressao
    ;

retorno
    : RETURN expressao PVIRG
    ;

// -------------------- Expressões --------------------

expressao
    : exprOu
    ;

exprOu
    : exprE
    | exprOu OR exprE
    ;

exprE
    : exprRelacional
    | exprE AND exprRelacional
    ;

exprRelacional
    : exprAditiva
    | exprAditiva opRelacional exprAditiva
    ;

opRelacional
    : LT | LE | GT | GE | EQ | NEQ
    ;

exprAditiva
    : exprMultiplicativa
    | exprAditiva opAditivo exprMultiplicativa
    ;

opAditivo
    : SOMA | SUB
    ;

exprMultiplicativa
    : fator
    | exprMultiplicativa opMultiplicativo fator
    ;

opMultiplicativo
    : MUL | DIV | RESTO
    ;

fator
    : sinal ID dimensao2
    | sinal constante
    | TEXTO
    | NOT fator
    | PAREN1 expressao PAREN2
    ;

constante
    : NUM_INT
    | NUM_DEC
    ;

sinal
    : SOMA
    | SUB
    | /* vazio */
    ;

// -------------------- Lexer Rules --------------------

// Palavras-chave
INT       : 'int' ;
FLOAT     : 'float' ;
CHAR      : 'char' ;
BOOLEAN   : 'boolean' ;
VOID      : 'void' ;
IF        : 'if' ;
ELSE      : 'else' ;
FOR       : 'for' ;
WHILE     : 'while' ;
RETURN    : 'return' ;
MAIN      : 'main' ;
PRINTLN   : 'println' ;
SCANF     : 'scanf' ;
FUNC      : 'func' ;

// Operadores
ATRIB     : '=' ;
EQ        : '==' ;
NEQ       : '!=' ;
LE        : '<=' ;
LT        : '<' ;
GE        : '>=' ;
GT        : '>' ;
SOMA      : '+' ;
SUB       : '-' ;
MUL       : '*' ;
DIV       : '/' ;
RESTO     : '%' ;
AND       : '&&' ;
OR        : '||' ;
NOT       : '!' ;

// Delimitadores
PVIRG     : ';' ;
VIRG      : ',' ;
PAREN1    : '(' ;
PAREN2    : ')' ;
CHAVE1    : '{' ;
CHAVE2    : '}' ;
COLCH1    : '[' ;
COLCH2    : ']' ;

// Literais
NUM_DEC   : [0-9]+ '.' [0-9]+ ;
NUM_INT   : [0-9]+ ;
TEXTO     : '"' (~["\\] | '\\' .)* '"' ;

ID        : [a-zA-Z_][a-zA-Z0-9_]* ;

// Ignorar comentários e espaços
COMMENT   : '//' ~[\r\n]* -> skip ;
WS        : [ \t\r\n]+ -> skip ;