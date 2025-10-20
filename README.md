# Projeto de Compilador - ANTLR

## Descrição

Este projeto implementa um **compilador simples** para uma linguagem de programação didática, utilizando **ANTLR 4** para análise lexical e sintática, e **listeners semânticos** para análise de tipos e verificação de variáveis.  

O compilador realiza as seguintes etapas:

1. **Análise Lexical**: converte o código-fonte em tokens.
2. **Análise Sintática**: verifica a estrutura do programa com base na gramática definida.
3. **Análise Semântica**: verifica tipos de variáveis, compatibilidade de atribuições e chamadas de função.
4. **Geração de Árvore Sintática**: cria uma representação gráfica da árvore sintática com Graphviz.
5. **Exibição de Tokens e Tabela de Símbolos**: imprime todos os tokens e informações sobre variáveis e funções.

O projeto é voltado para aprendizado de compiladores e análise de linguagens.

## Estrutura do Projeto
antlr/
- ExprLexer.g4           # Gramática do lexer
- ExprParser.g4          # Gramática do parser
- SymbolListener.py      # Listener semântico
- main.py                # Script principal de execução
- text.txt               # Código-fonte de teste
- parse_tree.png         # Saída da árvore sintática (gerada)
- README.md              # Documentação do projeto

## Gramática da Linguagem

A linguagem possui:

- **Tipos primitivos**: `int`, `float`, `char`, `boolean`
- **Vetores**: tipo com dimensão, ex: `int[5]`
- **Estruturas de controle**: `if-else`, `while`
- **Funções**: declaração e chamada com parâmetros
- **Comandos de entrada/saída**: `scanf`, `println`
- **Expressões aritméticas e lógicas**: `+`, `-`, `*`, `/`, `%`, `&&`, `||`, `!`
- **Atribuições e retorno**: `ID = expressao;`, `return expressao;`

## Execução do Projeto

Para executar o compilador semântico e gerar a árvore sintática, siga os passos abaixo:

1. Certifique-se de que todas as dependências estão instaladas (Python 3, ANTLR 4 e Graphviz).

2. Abra o terminal na pasta do projeto.

3. Execute o script principal:

```bash
python main.py text.txt
```

## Dependências

O projeto requer as seguintes ferramentas instaladas:

- **Python 3**  
  Para executar os scripts do compilador.  
  [Site oficial](https://www.python.org/)

- **ANTLR 4**  
  Para gerar lexer e parser a partir das gramáticas.  
  [Site oficial](https://www.antlr.org/)

- **Graphviz**  
  Para gerar a árvore sintática em formato gráfico (PNG).  
  [Site oficial](https://graphviz.org/)
