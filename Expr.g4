grammar Expr;

// ------------------ Parser rules ------------------

program
    : (declaration | stmt)* EOF
    ;

declaration
    : (INT | FLOAT | CHAR | BOOLEAN | VOID) declarator (COMMA declarator)* SEMI
    ;

declarator
    : ID (ASSIGN expr)?
    ;

stmt
    : expr SEMI
    | IF LPAREN expr RPAREN block ( ELSE block )?
    | WHILE LPAREN expr RPAREN block
    | FOR LPAREN (declaration | expr? SEMI) expr? SEMI expr? RPAREN block
    | RETURN expr? SEMI
    | block
    ;

block
    : LBRACE (declaration | stmt)* RBRACE
    ;

// expressions (precedence via separate rules)
expr
    : assignExpr
    ;

assignExpr
    : logicOr (ASSIGN assignExpr)?
    ;

logicOr
    : logicAnd (OR logicAnd)*
    ;

logicAnd
    : equality (AND equality)*
    ;

equality
    : relational ( ( '==' | '!=' ) relational )*
    ;

relational
    : add ( ( '<' | '<=' | '>' | '>=' ) add )*
    ;

add
    : mul ( (PLUS | MINUS) mul )*
    ;

mul
    : unary ( (MULT | DIV | MOD) unary )*
    ;

unary
    : NOT unary
    | PLUS unary
    | MINUS unary
    | primary
    ;

primary
    : LPAREN expr RPAREN
    | NUM_DEC
    | NUM_INT
    | ID
    | TEXTO
    ;

// ------------------ Lexer rules ------------------

// fragments for reuse
fragment D : [0-9] ;
fragment L : [a-zA-Z_] ;

// numbers & identifiers
NUM_INT  : D+ ;
NUM_DEC  : D+ '.' D+ ;
ID       : L [a-zA-Z0-9_]* ;

// string literal (supports escaped chars inside)
TEXTO
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    ;

// keywords (use literals so they take precedence over ID if matched)
INT     : 'int' ;
FLOAT   : 'float' ;
CHAR    : 'char' ;
BOOLEAN : 'boolean' ;
VOID    : 'void' ;
IF      : 'if' ;
ELSE    : 'else' ;
FOR     : 'for' ;
WHILE   : 'while' ;
SCANF   : 'scanf' ;
PRINTLN : 'println' ;
MAIN    : 'main' ;
RETURN  : 'return' ;

// operators and punctuation
ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MULT    : '*' ;
DIV     : '/' ;
MOD     : '%' ;

AND     : '&&' ;
OR      : '||' ;
NOT     : '!' ;

// comparison operator token (each alternative is a literal)
COMP    : '>=' | '>' | '<=' | '<' | '!=' | '==' ;

// separate tokens for parentheses/brackets/braces/etc.
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACK  : '[' ;
RBRACK  : ']' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
COMMA   : ',' ;
SEMI    : ';' ;

// comments and whitespace
COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;
