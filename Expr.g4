grammar Expr;

// ---------------- Parser rules ----------------

programa
    : VOID MAIN PAREN1 PAREN2 CHAVE1 (declaracoes | comandos)* CHAVE2 EOF
    ;

declaracoes
    : tipo ID (ATRIB expressao)? (VIRG ID (ATRIB expressao)?)* PVIRG
    | tipo ID COLCH1 expressao COLCH2 (ATRIB CHAVE1 expressao (VIRG expressao)* CHAVE2)? PVIRG
    ;

tipo
    : INT | FLOAT | CHAR | BOOLEAN | VOID
    ;

comandos
    : comandoIf
    | comandoWhile
    | comandoFor
    | comandoAtribuicao
    | comandoPrint
    | comandoScanf
    | comandoReturn
    ;

comandoIf
    : IF PAREN1 expressao PAREN2 CHAVE1 comandos* CHAVE2 (ELSE (comandoIf | CHAVE1 comandos* CHAVE2))?
    ;

comandoWhile
    : WHILE PAREN1 expressao PAREN2 CHAVE1 comandos* CHAVE2
    ;

// For clássico: init ; cond ; update
// for(i=0;i<9;i++) { comandos }
comandoFor
    : FOR PAREN1 forInit? PVIRG expressao? PVIRG (ID ATRIB expressao)? PAREN2 CHAVE1 comandos* CHAVE2
    ;

forInit
    : tipo ID ATRIB expressao       // int i = 0
    | ID ATRIB expressao            // i = 0
    ;

comandoAtribuicao
    : ID ATRIB expressao PVIRG
    | ID COLCH1 expressao COLCH2 ATRIB expressao PVIRG
    ;

comandoPrint
    : PRINTLN PAREN1 (expressao | TEXTO (SOMA expressao)*) PAREN2 PVIRG
    ;

comandoScanf
    : SCANF PAREN1 TEXTO VIRG expressao PAREN2 PVIRG
    ;

comandoReturn
    : RETURN expressao? PVIRG
    ;

// ---------- Expressões com precedência ----------

expressao
    : assignExpr
    ;

assignExpr
    : logicOr (ATRIB assignExpr)?
    ;

logicOr
    : logicAnd (OR logicAnd)*
    ;

logicAnd
    : equality (AND equality)*
    ;

equality
    : relational ((EQ | NEQ) relational)*
    ;

relational
    : add ((LT | LE | GT | GE) add)*
    ;

add
    : mul ((SOMA | SUB) mul)*
    ;

mul
    : unary ((MUL | DIV | RESTO) unary)*
    ;

unary
    : SUB unary
    | SOMA unary
    | NOT unary
    | primary
    ;

primary
    : PAREN1 expressao PAREN2
    | NUM_INT
    | NUM_DEC
    | ID
    | ID COLCH1 expressao COLCH2
    | TEXTO
    ;

// ---------------- Lexer rules ----------------

// Keywords
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

// Operators
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

// Delimiters
PVIRG     : ';' ;
VIRG      : ',' ;
PAREN1    : '(' ;
PAREN2    : ')' ;
CHAVE1    : '{' ;
CHAVE2    : '}' ;
COLCH1    : '[' ;
COLCH2    : ']' ;

// Literals
NUM_DEC   : [0-9]+ '.' [0-9]+ ;
NUM_INT   : [0-9]+ ;
TEXTO     : '"' (~["\\] | '\\' .)* '"' ;

ID        : [a-zA-Z_][a-zA-Z0-9_]* ;

// Ignore
COMMENT   : '//' ~[\r\n]* -> skip ;
WS        : [ \t\r\n]+ -> skip ;
