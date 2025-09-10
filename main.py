from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener


class SymbolListener(ExprListener):
    def __init__(self):
        self.symbols = []

    def exitDeclaracoes(self, ctx):  # Alterado de exitDeclaration para exitDeclaracoes
        tipo = ctx.tipo().getText()  # Acessa o tipo da declaração
        for decl in ctx.ID():  # Itera diretamente sobre os IDs
            ident = decl.getText()
            self.symbols.append((ident, tipo))


def main():
    try:
        with open('text.txt', encoding="utf-8") as exemplo:
            exemploTxt = exemplo.read()

        input_stream = InputStream(exemploTxt)
        
        # Debug dos tokens
        lexer = ExprLexer(input_stream)
        all_tokens = lexer.getAllTokens()
        print(">>> Tokens reconhecidos pelo lexer:")
        for t in all_tokens:
            print(f"{t.text!r} -> {lexer.symbolicNames[t.type]}")

        # Reinicializa o lexer
        lexer = ExprLexer(InputStream(exemploTxt))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.programa()  # Alterado de program para programa

        listener = SymbolListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        print("\nTabela de símbolos:")
        for ident, tipo in listener.symbols:
            print(f"ID: {ident}  Tipo: {tipo}")

    except FileNotFoundError:
        print("Erro: O arquivo 'text.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")


if __name__ == "__main__":
    main()