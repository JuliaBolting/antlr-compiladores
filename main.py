from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener


class SymbolListener(ExprListener):
    def __init__(self):
        self.symbols = []
        self.id_counter = 0
        self.id_map = {}
        self.current_type = None  # Para rastrear o tipo durante declarações
        self.expr_ids = []        # Para armazenar IDs de expressões temporariamente

    def enterDeclaracoes(self, ctx):
        # Guarda o tipo de cada ID
        self.current_type = ctx.tipo().getText()
        self.expr_ids = []

    # Verifica se id já existe na lista de símbolos
    def exitPrimary(self, ctx):
        if ctx.ID():
            ident = ctx.ID().getText()
            if ident not in self.id_map:
                # Não incrementa id_counter aqui; será feito em exitDeclaracoes
                tipo = "boolean" if ident in ["true", "false"] else "unknown"
                self.expr_ids.append((ident, tipo))

    def exitDeclaracoes(self, ctx):
        # Processa identificadores declarados (ex.: cond, a, b, c, vetor)
        if not ctx.COLCH1():  # Declarações normais
            for decl in ctx.ID():
                ident = decl.getText()
                if ident not in self.id_map:
                    self.id_map[ident] = self.id_counter
                    self.symbols.append((self.id_map[ident], ident, self.current_type))
                    self.id_counter += 1
        # Declarações de arrays
        if ctx.COLCH1():
            ident = ctx.ID(0).getText()
            if ident not in self.id_map:
                self.id_map[ident] = self.id_counter
                self.symbols.append((self.id_map[ident], ident, f"{self.current_type}[]"))
                self.id_counter += 1
        # Adiciona IDs de expressões (ex.: true) após os declarados
        # Se não for nenhuma das de cima vem aqui
        for ident, tipo in self.expr_ids:
            if ident not in self.id_map:
                self.id_map[ident] = self.id_counter
                self.symbols.append((self.id_map[ident], ident, tipo))
                self.id_counter += 1
        self.expr_ids = []
        self.current_type = None

    # Verifica variáveis dentro dos parenteses do for
    def exitForInit(self, ctx):
        if ctx.tipo():
            ident = ctx.ID().getText()
            if ident not in self.id_map:
                self.id_map[ident] = self.id_counter
                self.symbols.append((self.id_map[ident], ident, ctx.tipo().getText()))
                self.id_counter += 1


def main():
    try:
        with open('text.txt', encoding="utf-8") as exemplo:
            exemploTxt = exemplo.read()

        # Primeiro: roda parser e listener para preencher id_map
        lexer = ExprLexer(InputStream(exemploTxt))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.programa()

        listener = SymbolListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Agora: imprime tokens com IDs numerados
        lexer = ExprLexer(InputStream(exemploTxt))
        all_tokens = lexer.getAllTokens()
        print(">>> Tokens reconhecidos pelo lexer:")
        for t in all_tokens:
            line = t.line
            column = t.column + 1
            token_name = lexer.symbolicNames[t.type]
            token_text = t.text
            if token_name == "ID" and token_text in listener.id_map:
                token_text = f"{listener.id_map[token_text]}, {token_text}"
            print(f"Linha {line} Coluna {column}\t{token_name}\t{token_text}")

        # Lista final de símbolos
        print("\nLista de símbolos/ID:")
        for num, ident, tipo in listener.symbols:
            print(f"{num}: {ident} ({tipo})")

    except FileNotFoundError:
        print("Erro: O arquivo 'text.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")


if __name__ == "__main__":
    main()