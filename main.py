from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener

class SymbolListener(ExprListener):
    def __init__(self):
        self.symbols = []

    def exitDeclaration(self, ctx):
        tipo = ctx.getChild(0).getText()   
        for decl in ctx.declarator():
            ident = decl.ID().getText()
            self.symbols.append((ident, tipo))

def main():
    input_text = InputStream("""
        int a = 5;
    """)

    lexer = ExprLexer(input_text)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()

    listener = SymbolListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("Tabela de símbolos:")
    for ident, tipo in listener.symbols:
        print(f"ID: {ident}  Tipo: {tipo}")

if __name__ == "__main__":
    main()
