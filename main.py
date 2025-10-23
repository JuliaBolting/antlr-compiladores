import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from SymbolListener import SymbolListener
from graphviz import Digraph

# Garante que o Graphviz seja encontrado
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"


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
    print(f"\nÁrvore sintática salva em: {arquivo_saida}")


def main():
    try:
        with open('text.txt', encoding="utf-8") as f:
            code = f.read()

        # Lexer e sintático
        lexer = ExprLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.programa()

        # Listener semântico
        listener = SymbolListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Tokens
        print("\n>>> Tokens:")
        lexer = ExprLexer(InputStream(code))
        for t in lexer.getAllTokens():
            print(f"Linha {t.line} Coluna {t.column+1}\t{lexer.symbolicNames[t.type]}\t{t.text}")

        # Árvore
        desenhar_arvore(tree, parser)

    except FileNotFoundError:
        print("Arquivo 'text.txt' não encontrado.")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()