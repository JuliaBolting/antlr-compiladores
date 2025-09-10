from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener


class SymbolListener(ExprListener):
    def __init__(self):
        self.symbols = []
        self.id_counter = 0
        self.id_map = {}

    def exitDeclaracoes(self, ctx):
        tipo = ctx.tipo().getText()
        # Declarações normais
        if not ctx.COLCH1():  # Processa apenas se não for um array
            for decl in ctx.ID():
                ident = decl.getText()
                if ident not in self.id_map:
                    self.id_map[ident] = self.id_counter
                    self.id_counter += 1
                self.symbols.append((self.id_map[ident], ident, tipo))
        # Declarações de arrays
        if ctx.COLCH1():
            ident = ctx.ID(0).getText()
            if ident not in self.id_map:
                self.id_map[ident] = self.id_counter
                self.id_counter += 1
            self.symbols.append((self.id_map[ident], ident, f"{tipo}[]"))

    def exitForInit(self, ctx):
        if ctx.tipo():  # Verifica se há uma declaração (tipo ID ATRIB expressao)
            tipo = ctx.tipo().getText()
            ident = ctx.ID().getText()
            if ident not in self.id_map:
                self.id_map[ident] = self.id_counter
                self.id_counter += 1
            self.symbols.append((self.id_map[ident], ident, tipo))


def main():
    try:
        with open('text.txt', encoding="utf-8") as exemplo:
            exemploTxt = exemplo.read()

        input_stream = InputStream(exemploTxt)
        
        # Debug dos tokens com linha e coluna
        lexer = ExprLexer(input_stream)
        all_tokens = lexer.getAllTokens()
        print(">>> Tokens reconhecidos pelo lexer:")
        for t in all_tokens:
            line = t.line
            column = t.column + 1  # Ajuste para base 1
            token_name = lexer.symbolicNames[t.type]
            token_text = t.text
            print(f"Linha {line} Coluna {column}\t{token_name}\t{token_text}")

        # Reinicializa o lexer
        lexer = ExprLexer(InputStream(exemploTxt))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.programa()

        listener = SymbolListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        print("\nLista de símbolos/ID:")
        for num, ident, tipo in listener.symbols:
            print(f"{num}: {ident} ({tipo})")

    except FileNotFoundError:
        print("Erro: O arquivo 'text.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")


if __name__ == "__main__":
    main()