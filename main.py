import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from graphviz import Digraph


# ✅ Garante que o Python encontre o Graphviz
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"


class SymbolListener(ExprListener):
    def __init__(self):
        self.symbols = []       # [(num, nome, tipo)]
        self.id_counter = 0
        self.id_map = {}

    # Ao sair de uma lista de variáveis, adiciona os identificadores à tabela
    def exitListaVariaveis(self, ctx):
        tipo_ctx = ctx.tipo()
        if not tipo_ctx:
            # pode estar na forma recursiva: listaVariaveis tipo listaId PVIRG
            children = list(ctx.getChildren())
            for child in children:
                if hasattr(child, "tipo"):
                    tipo_ctx = child.tipo()
                    if tipo_ctx:
                        break
        tipo = tipo_ctx.getText() if tipo_ctx else "unknown"

        # Captura os identificadores declarados
        if ctx.listaId():
            ids_text = ctx.listaId().getText().split(',')
            for ident in ids_text:
                ident = ident.strip()
                if ident not in self.id_map:
                    self.id_map[ident] = self.id_counter
                    self.symbols.append((self.id_counter, ident, tipo))
                    self.id_counter += 1

    # Captura variáveis usadas em atribuições que não foram declaradas
    def exitAtribuicao(self, ctx):
        ident = ctx.ID().getText()
        if ident not in self.id_map:
            self.id_map[ident] = self.id_counter
            self.symbols.append((self.id_counter, ident, "unknown"))
            self.id_counter += 1


# 🔵 Função para desenhar árvore sintática
def desenhar_arvore(tree, parser, nome_saida="parse_tree"):
    dot = Digraph(comment='Árvore Sintática')
    dot.attr("node", shape="box", style="rounded,filled", fillcolor="lightgrey")

    contador = {"n": 0}

    def adicionar_nos(no, pai=None):
        nome_regra = parser.ruleNames[no.getRuleIndex()] if no.getChildCount() > 0 else no.getText()
        nome_no = f"node{contador['n']}"
        contador["n"] += 1
        dot.node(nome_no, label=nome_regra)

        if pai:
            dot.edge(pai, nome_no)

        for i in range(no.getChildCount()):
            adicionar_nos(no.getChild(i), nome_no)

    adicionar_nos(tree)

    arquivo_saida = dot.render(filename=nome_saida, format="png", cleanup=True)
    print(f"\n🌳 Árvore sintática salva em: {arquivo_saida}")


def main():
    try:
        with open('text.txt', encoding="utf-8") as exemplo:
            exemploTxt = exemplo.read()

        # Etapa 1 — Lexer + Parser
        lexer = ExprLexer(InputStream(exemploTxt))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.programa()

        # Etapa 2 — Percorre a árvore e coleta os símbolos
        listener = SymbolListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Etapa 3 — Exibe os tokens reconhecidos
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

        # Etapa 4 — Exibe a tabela de símbolos
        print("\nLista de símbolos/ID:")
        if listener.symbols:
            for num, ident, tipo in listener.symbols:
                print(f"{num}: {ident} ({tipo})")
        else:
            print("(nenhum símbolo encontrado)")

        # Etapa 5 — Gera árvore sintática gráfica
        desenhar_arvore(tree, parser)

        print("\n✅ Análise sintática concluída com sucesso!")

    except FileNotFoundError:
        print("❌ Erro: O arquivo 'text.txt' não foi encontrado.")
    except Exception as e:
        print(f"❌ Erro durante a execução: {str(e)}")


if __name__ == "__main__":
    main()
