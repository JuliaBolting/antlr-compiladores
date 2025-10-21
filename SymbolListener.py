from ExprListener import ExprListener
from ExprParser import ExprParser

class SymbolListener(ExprListener):


    def __init__(self):
        self.symbols = []  # Lista de tuplas: (id, nome, tipo, escopo, offset)
        self.functions = {}  # Dicionário: {nome_funcao: {"retorno": tipo, "params": [tipos]}}
        self.errors = []
        self.context = "global"
        self.current_function = None
        self.id_counter = 0
        self.offset_stack = {"global": 0}  # Offset atual por escopo
        self.scope_stack = ["global"]  # Pilha de escopos ativos


    def add_symbol(self, name, tipo):
        
        # Adiciona um símbolo ao escopo atual se não estiver já declarado ali.
        # Atualiza o offset para o próximo símbolo.
        
        if self.is_declared_in_scope(name, self.context):
            self.errors.append(f"Variável '{name}' já declarada em {self.context}.")
            return

        width = self.get_width(tipo)
        offset = self.offset_stack.get(self.context, 0)
        self.symbols.append((self.id_counter, name, tipo, self.context, offset))
        self.id_counter += 1
        self.offset_stack[self.context] = offset + width


    def lookup(self, name):
        
        # Procura um símbolo pelo nome no escopo atual e ancestrais.
        # Retorna a tupla completa do símbolo ou None.
        
        for scope in reversed(self.scope_stack):
            for s in self.symbols:
                if s[1] == name and s[3] == scope:
                    return s
        return None


    def is_declared_in_scope(self, name, scope):
        
        #Verifica se uma variável já foi declarada no escopo dado.
        return any(s[1] == name and s[3] == scope for s in self.symbols)


    def get_width(self, tipo):
        
        # Retorna a largura de memória (em bytes) para um tipo.
        return {"int": 4, "float": 8, "char": 1, "boolean": 1}.get(tipo, 4)


    def infer_type(self, expr_text):
        if not expr_text:
            return "int"
        
        stripped = expr_text.strip()
        
        # numeros literais
        if stripped.isdigit():
            return "int"
        if '.' in stripped and stripped.replace('.', '').replace('-', '').isdigit():
            return "float"
        
        # boolean nos operadores
        rel_ops = ['>', '<', '>=', '<=', '==', '!=']
        for op in rel_ops:
            if op in stripped:
                return "boolean"
        
        # boolean nos operadores logicos
        if any(op in stripped for op in ['&&', '||', '!']):
            return "boolean"
        
        # busca variavel na tabela de simbolos
        if (stripped.isalpha() or stripped[0] == '_') and all(c.isalnum() or c == '_' for c in stripped):
            symbol = self.lookup(stripped)
            if symbol:
                return symbol[2]
        
        # identifica texto entre aspas como char
        if stripped.startswith('"') and stripped.endswith('"'):
            return "char"
        
        # 6. default
        return "int"
       
        
    # -------------- Gramática: listaVariaveis : tipo listaId PVIRG | listaVariaveis tipo listaId PVIRG ;
    def exitListaVariaveis(self, ctx):
        
        # Extrai o tipo da declaração e registra todos os IDs em listaId.
        # Tenta extrair o tipo com try-except (compatível com regras sem labels)
        
        tipo = None
        try:
            tipo_ctx = ctx.tipo()
            if tipo_ctx:
                tipo = tipo_ctx.getText()
        except AttributeError:
            pass

        if not tipo:
            # Fallback: busca filhos imediatos por palavras-chave de tipo
            for i in range(ctx.getChildCount()):
                child_text = ctx.getChild(i).getText()
                if child_text in ["int", "float", "char", "boolean"]:
                    tipo = child_text
                    break
        if not tipo:
            tipo = "unknown"  # Não deve acontecer em parse válido

        # Registra IDs de listaId
        try:
            lista_id_ctx = ctx.listaId()
            if lista_id_ctx:
                self._registrar_lista_ids(lista_id_ctx, tipo)
        except AttributeError:
            pass


    # ----------------- Gramática: listaId : ID | listaId VIRG ID ;
    def _registrar_lista_ids(self, ctx, tipo):
        
        # Registra recursivamente IDs da subárvore listaId.
        
        if not ctx:
            return

        child_count = ctx.getChildCount()
        if child_count == 1:
            # Caso base: ID único
            id_node = ctx.getChild(0)
            self.add_symbol(id_node.getText(), tipo)
        elif child_count == 3:
            # Caso recursivo: listaId VIRG ID
            self._registrar_lista_ids(ctx.getChild(0), tipo)
            id_node = ctx.getChild(2)
            self.add_symbol(id_node.getText(), tipo)
        else:
            # Estrutura inesperada: fallback para tokens (raro, para robustez)
            try:
                for token in ctx.getTokens(ExprParser.ID):
                    self.add_symbol(token.getText(), tipo)
            except Exception:
                pass  # Ignora silenciosamente se o fallback falhar


    # ----------- Gramática: leitura : SCANF PAREN1 listaTermoLeitura PAREN2 PVIRG ;
    # ----------- Gramática: listaTermoLeitura : termoLeitura | listaTermoLeitura VIRG termoLeitura ;
    # ----------- Gramática: termoLeitura : ID dimensao2 ;
    def exitLeitura(self, ctx):
        
        # Verifica se todas as variáveis nos argumentos do scanf estão declaradas.
        # Usa try-except para acessar listaTermoLeitura
        
        try:
            lista_ctx = ctx.listaTermoLeitura()
        except AttributeError:
            lista_ctx = None
        if not lista_ctx:
            return

        ids = self._collect_ids_from_list(lista_ctx)
        for name in ids:
            if not self.lookup(name):
                self.errors.append(f"Variável '{name}' usada sem declaração em scanf.")
                

    # ----------- Gramática: chamadaFuncao : FUNC ID PAREN1 argumentos PAREN2 ;
    # ----------- Gramática: argumentos : listaArgumentos | /* vazio */ ;
    # ----------- Gramática: listaArgumentos : expressao | listaArgumentos VIRG expressao ;
    def exitChamadaFuncao(self, ctx):
        
        # Verifica a declaração da função e variáveis nos argumentos.
        # Verifica o nome da função
        
        func_ids = ctx.ID()
        if not isinstance(func_ids, list):
            func_ids = [func_ids] if func_ids else []
        if func_ids:
            nome_funcao = func_ids[0].getText()
            if nome_funcao not in self.functions:
                self.errors.append(f"Função '{nome_funcao}' chamada sem declaração.")
        else:
            self.errors.append("Chamada de função sem nome válido.")

        # Verifica argumentos para variáveis não declaradas (extração simples de ID)
        try:
            args_ctx = ctx.argumentos()
        except AttributeError:
            args_ctx = None
        if args_ctx:
            try:
                lista_args = args_ctx.listaArgumentos()
                if lista_args:
                    ids = self._collect_ids_from_list(lista_args)  # Assume expressões simples como ID
                    for name in ids:
                        if not self.lookup(name):
                            self.errors.append(f"Variável '{name}' usada sem declaração em argumento de função.")
            except AttributeError:
                pass


    def _collect_ids_from_list(self, ctx, token_type=ExprParser.ID):
        
        # Coleta recursivamente tokens ID de subárvores semelhantes a listas
        # Retorna lista de nomes de IDs (strings).
        
        ids = []
        if not ctx:
            return ids

        child_count = ctx.getChildCount()
        if child_count == 1:
            # Caso base: item único (ex.: termoLeitura -> ID ou expressao -> ID)
            try:
                item_child = ctx.getChild(0)
                id_token = item_child.ID()
                if id_token:
                    ids.append(id_token.getText())
            except (AttributeError, IndexError):
                pass
            if not ids:  # Fallback para tokens
                try:
                    token_ids = ctx.getTokens(token_type)
                    ids.extend([t.getText() for t in token_ids])
                except Exception:
                    pass
        elif child_count == 3:
            # Caso recursivo: list VIRG item
            rec_ctx = ctx.getChild(0)
            ids.extend(self._collect_ids_from_list(rec_ctx, token_type))
            try:
                item_child = ctx.getChild(2)
                id_token = item_child.ID()
                if id_token:
                    ids.append(id_token.getText())
            except (AttributeError, IndexError):
                pass
            if not ids:  # Fallback para o último item
                try:
                    token_ids = ctx.getTokens(token_type)
                    ids.extend([t.getText() for t in token_ids])
                except Exception:
                    pass
        return ids


    # ------------- Gramática: decFuncao : tipoRetorno ID PAREN1 parametros PAREN2 bloco ;
    def enterDecFuncao(self, ctx):
        
        # Entra no escopo da função: registra metadados e empilha escopo.
        
        nome_func = ctx.ID().getText()
        # Tenta extrair tipoRetorno com try-except
        tipo_retorno = "void"
        try:
            tipo_retorno_ctx = ctx.tipoRetorno()
            if tipo_retorno_ctx:
                tipo_retorno = tipo_retorno_ctx.getText()
        except AttributeError:
            pass

        if nome_func in self.functions:
            self.errors.append(f"Função '{nome_func}' já declarada.")
            return

        self.functions[nome_func] = {"retorno": tipo_retorno, "params": []}
        self.current_function = nome_func
        self.context = nome_func
        self.scope_stack.append(nome_func)
        self.offset_stack[nome_func] = 0


    def exitDecFuncao(self, ctx):
        
        # Sai do escopo da função: desempilha pilha.
        
        if self.scope_stack and self.scope_stack[-1] == self.current_function:
            self.scope_stack.pop()
        self.context = "global"
        self.current_function = None


    # ------------ Gramática: parametros : listaParametros | /* vazio */ ;
    # ------------ Gramática: listaParametros : tipo ID | listaParametros VIRG tipo ID ;
    def exitParametros(self, ctx):
        
        # Registra parâmetros da função como símbolos no escopo da função.
        # Usa try-except para acessar listaParametros
        
        try:
            lista_ctx = ctx.listaParametros()
        except AttributeError:
            lista_ctx = None
        if not lista_ctx:
            return

        def processar_lista(ctx_lp):
            # Extrai tipo com try-except
            tipo = "unknown"
            try:
                tipo_ctx = ctx_lp.tipo()
                if tipo_ctx:
                    tipo = tipo_ctx.getText()
            except AttributeError:
                pass

            # Extrai IDs
            try:
                id_tokens = ctx_lp.ID()
                if not isinstance(id_tokens, list):
                    id_tokens = [id_tokens] if id_tokens else []
            except AttributeError:
                id_tokens = []

            for id_token in id_tokens:
                if id_token:
                    nome = id_token.getText()
                    saved_context = self.context
                    self.context = self.current_function
                    self.add_symbol(nome, tipo)
                    self.context = saved_context
                    self.functions[self.current_function]["params"].append(tipo)

            # Recursão na listaParametros aninhada
            try:
                rec_ctx = ctx_lp.listaParametros()
                if rec_ctx:
                    processar_lista(rec_ctx)
            except AttributeError:
                pass

        processar_lista(lista_ctx)


    # ------------ Gramática: principal : MAIN PAREN1 PAREN2 bloco ;
    def enterPrincipal(self, ctx):
        
        # Entra no escopo principal (main).
        
        self.context = "main"
        self.current_function = "main"
        self.scope_stack.append("main")
        self.offset_stack["main"] = 0
        if "main" not in self.functions:
            self.functions["main"] = {"retorno": "void", "params": []}


    def exitPrincipal(self, ctx):
        
        # Sai do escopo principal (main).
        
        if self.scope_stack and self.scope_stack[-1] == "main":
            self.scope_stack.pop()
        self.context = "global"
        self.current_function = None


    # ------------ Gramática: bloco : CHAVE1 secaoVariaveis secaoComandos CHAVE2 ;
    def enterBloco(self, ctx):
        
        # Entra no bloco: cria sub-escopo se não estiver no corpo da função.
        
        top_scope = self.scope_stack[-1] if self.scope_stack else "global"
        if self.current_function == top_scope or (top_scope == "main" and self.current_function == "main"):
            self.context = top_scope  # Variáveis vão para o escopo da função/main
            return

        # Cria escopo de bloco aninhado
        parent = self.current_function if self.current_function else top_scope
        bloco_nome = f"{parent}_bloco_{len(self.scope_stack)}"
        self.scope_stack.append(bloco_nome)
        self.context = bloco_nome
        self.offset_stack[bloco_nome] = 0


    def exitBloco(self, ctx):
        
        # Sai do bloco: desempilha sub-escopo se aplicável.
        
        if self.scope_stack and self.scope_stack[-1] not in (self.current_function, "main"):
            self.scope_stack.pop()
        self.context = self.scope_stack[-1] if self.scope_stack else "global"


    # ------------ Gramática: atribuicao : ID ATRIB complemento PVIRG ;
    # ------------ Gramática: complemento : expressao | chamadaFuncao ;
    def exitAtribuicao(self, ctx):
        
        # Verifica declaração do lvalue e compatibilidade de tipos.
        
        id_tokens = ctx.ID()
        if not isinstance(id_tokens, list):
            id_tokens = [id_tokens] if id_tokens else []
        if not id_tokens:
            return

        nome_var = id_tokens[0].getText()
        symbol = self.lookup(nome_var)
        if not symbol:
            self.errors.append(f"Variável '{nome_var}' usada sem declaração.")
            return

        tipo_var = symbol[2]
        # Usa try-except para acessar complemento
        try:
            complemento_ctx = ctx.complemento()
        except AttributeError:
            complemento_ctx = None
        if not complemento_ctx:
            return

        tipo_expr = None
        # Verifica se complemento é uma chamada de função
        try:
            chamada_ctx = complemento_ctx.chamadaFuncao()
            if chamada_ctx:
                func_ids = chamada_ctx.ID()
                if not isinstance(func_ids, list):
                    func_ids = [func_ids] if func_ids else []
                if func_ids:
                    nome_funcao = func_ids[0].getText()
                    if nome_funcao in self.functions:
                        tipo_expr = self.functions[nome_funcao]["retorno"]
                    else:
                        self.errors.append(f"Função '{nome_funcao}' chamada sem declaração.")
        except AttributeError:
            pass
        
        # Fallback: inferir do texto (simples, para expressões)
        if not tipo_expr:
            tipo_expr = self.infer_type(complemento_ctx.getText())

        # Verificação de tipo (com promoção implícita int-para-float)
        if tipo_expr and tipo_var != tipo_expr:
            if not (tipo_var == "float" and tipo_expr == "int"):
                self.errors.append(
                    f"Tipo incompatível: '{nome_var}' é {tipo_var}, mas expressão é {tipo_expr}."
                )


    # ------------- Gramática: retorno : RETURN expressao PVIRG ;
    def exitRetorno(self, ctx):
        
        # Verifica se o tipo da expressão no return é compatível com o tipo de retorno da função atual.
        
        if not self.current_function:
            return  # Fora de contexto de func

        tipo_ret_func = self.functions[self.current_function]["retorno"]
        try:
            expr_ctx = ctx.expressao()
            if expr_ctx:
                tipo_expr = self.infer_type(expr_ctx.getText())
                if tipo_expr and tipo_expr != tipo_ret_func:
                    if not (tipo_ret_func == "float" and tipo_expr == "int"):  # Promoção implícita
                        self.errors.append(
                            f"Retorno incompatível em '{self.current_function}': esperado {tipo_ret_func}, mas é {tipo_expr}."
                        )
        except AttributeError:
            pass


    # -------------- Gramática: escrita : PRINTLN PAREN1 listaTermoEscrita PAREN2 PVIRG ;
    # -------------- Gramática: listaTermoEscrita : termoEscrita | listaTermoEscrita VIRG termoEscrita ;
    # -------------- Gramática: termoEscrita : ID dimensao2 | constante | TEXTO ;
    def exitEscrita(self, ctx):
        
        # Verifica variáveis usadas em println (ex.: checa declaração em IDs).
        
        try:
            lista_ctx = ctx.listaTermoEscrita()
            if lista_ctx:
                ids = self._collect_ids_from_list(lista_ctx)  # Reusa o helper pra IDs em termos
                for name in ids:
                    if not self.lookup(name):
                        self.errors.append(f"Variável '{name}' usada sem declaração em println.")
        except AttributeError:
            pass


    # ---------------------- Gramática: selecao : IF PAREN1 expressao PAREN2 bloco senao ;
    # ---------------------- Gramática: senao : ELSE bloco | /* vazio */ ;
    def exitSelecao(self, ctx):
        
        # Verifica se a condição do if é boolean.
        
        tipo_cond = self.infer_type(ctx.expressao().getText())
        if tipo_cond != "boolean":
            self.errors.append("Condição de if deve ser do tipo boolean.")


    # ----------------- Gramática: enquanto : WHILE PAREN1 expressao PAREN2 bloco ;
    def exitEnquanto(self, ctx):
        
        # Verifica se a condição do while é boolean (similar ao if).
        
        tipo_cond = self.infer_type(ctx.expressao().getText())
        if tipo_cond != "boolean":
            self.errors.append("Condição de while deve ser do tipo boolean.")


    # -------------------- Gramática: expressao : exprOu ; (e sub-regras: exprOu, exprE, exprRelacional, etc.)
    # -------------------- Nota: Isso é recursivo — adicione um método base pra type checking em expressões.
    def exitExpressao(self, ctx):
        
        # Verificação básica de tipos em expressões (heurística; expanda pra ops específicas).
        # Checa vars usadas e tipos em ops simples (ex.: relacional deve retornar boolean).
        # Coleta IDs na expr e checa declaração
        
        try:
            ids = ctx.getTokens(ExprParser.ID)
            for token in ids:
                name = token.getText()
                if not self.lookup(name):
                    self.errors.append(f"Variável '{name}' usada sem declaração em expressão.")
        except Exception:
            pass
        
        # Infer tipo da expr inteira (fallback simples)
        tipo_expr = self.infer_type(ctx.getText())
        # Exemplo: Pra relacional (>, <), assume boolean; adicione lógica por sub-regra se precisar
        if ">" in ctx.getText() or "<" in ctx.getText() or "==" in ctx.getText():
            if tipo_expr != "boolean":
                self.errors.append("Operador relacional deve retornar boolean.")


    # ------------------- Gramática: dimensao : dimensao COLCH1 NUM_INT COLCH2 | /* vazio */ ; (arrays)
    # ------------------- Gramática: dimensao2 : dimensao2 COLCH1 exprAditiva COLCH2 | /* vazio */ ;
    def exitDimensao(self, ctx):
        
        # Checagem básica pra arrays: verifica se tamanho é inteiro positivo.
        # Atualiza offset pra arrays (multiplica width por tamanho).
        
        try:
            num_ctx = ctx.NUM_INT()
            if num_ctx:
                tamanho = int(num_ctx.getText())
                if tamanho <= 0:
                    self.errors.append("Dimensão de array deve ser positiva.")
        except AttributeError:
            pass


    # ---------------- Gramática: exprAditiva : exprMultiplicativa | exprAditiva opAditivo exprMultiplicativa ;
    # ---------------- Gramática: opAditivo : SOMA | SUB ;
    def exitExprAditiva(self, ctx):
        """Verifica + / - : operandos numéricos (int/float, com promoção)."""
        op_text = ctx.getText()
        if '+' in op_text or '-' in op_text:
            tipo_esq = self.infer_type(ctx.getChild(0).getText())
            tipo_dir = self.infer_type(ctx.getChild(2).getText()) if ctx.getChildCount() > 2 else None
            if tipo_esq not in ["int", "float"] or (tipo_dir and tipo_dir not in ["int", "float"]):
                self.errors.append(f"Operadores + ou - requerem operandos numéricos (int ou float).")


    # ----------------- Gramática: exprOu : exprE | exprOu OR exprE ;
    def exitExprOu(self, ctx):
        
        # Verifica OR: operandos devem ser boolean.
        
        op_text = ctx.getText()
        if '||' in op_text:
            tipo_esq = self.infer_type(ctx.getChild(0).getText())
            tipo_dir = self.infer_type(ctx.getChild(2).getText()) if ctx.getChildCount() > 2 else None
            if tipo_esq != "boolean" or (tipo_dir and tipo_dir != "boolean"):
                self.errors.append("Operador OR (||) requer operandos boolean.")


    # ---------------- Gramática: exprE : exprRelacional | exprE AND exprRelacional ;
    def exitExprE(self, ctx):
        
        #Verifica AND: operandos devem ser boolean.
        
        op_text = ctx.getText()
        if '&&' in op_text:
            tipo_esq = self.infer_type(ctx.getChild(0).getText())
            tipo_dir = self.infer_type(ctx.getChild(2).getText()) if ctx.getChildCount() > 2 else None
            if tipo_esq != "boolean" or (tipo_dir and tipo_dir != "boolean"):
                self.errors.append("Operador AND (&&) requer operandos boolean.")


    # ------------------ Gramática: exprRelacional : exprAditiva | exprAditiva opRelacional exprAditiva ;
    # ------------------ Gramática: opRelacional : LT | LE | GT | GE | EQ | NEQ ;
    def exitExprRelacional(self, ctx):
        pass


    # ------------------ Gramática: exprMultiplicativa : fator | exprMultiplicativa opMultiplicativo fator ;
    # ------------------ Gramática: opMultiplicativo : MUL | DIV | RESTO ;
    def exitExprMultiplicativa(self, ctx):
        
        # Verifica * / % : operandos numéricos inteiros pra % (resto).
        
        op_text = ctx.getText()
        for op, req_int in [('*', False), ('/', False), ('%', True)]:
            if op in op_text:
                tipo_esq = self.infer_type(ctx.getChild(0).getText())
                tipo_dir = self.infer_type(ctx.getChild(2).getText()) if ctx.getChildCount() > 2 else None
                if tipo_esq not in ["int", "float"] or (tipo_dir and tipo_dir not in ["int", "float"]):
                    self.errors.append(f"Operador '{op}' requer operandos numéricos.")
                if op == '%' and (tipo_esq != "int" or (tipo_dir and tipo_dir != "int")):
                    self.errors.append("Operador % (resto) requer operandos inteiros.")
                break


    # ------------------- Gramática: fator : sinal ID dimensao2 | sinal constante | TEXTO | NOT fator | PAREN1 expressao PAREN2 ;
    def exitFator(self, ctx):
        
        # Verifica NOT: operando deve ser boolean.
        
        op_text = ctx.getText()
        if '!' in op_text:
            tipo_op = self.infer_type(ctx.getChild(1).getText() if ctx.getChildCount() > 1 else ctx.getText())
            if tipo_op != "boolean":
                self.errors.append("Operador NOT (!) requer operando boolean.")

        # Checa ID em fator (ex.: !a ou -a)
        try:
            id_token = ctx.ID()
            if id_token:
                name = id_token.getText()
                if not self.lookup(name):
                    self.errors.append(f"Variável '{name}' usada sem declaração em fator.")
        except AttributeError:
            pass


    # ------------ Gramática: programa : secaoFuncoes principal EOF ;
    def exitPrograma(self, ctx):
        
        # Imprime tabela de símbolos, funções e erros.
        
        print("\n=== TABELA DE SÍMBOLOS ===")
        print(f"{'ID':>3} | {'Nome':<10} | {'Tipo':<8} | {'Escopo':<15} | {'Offset':>6}")
        print("-" * 55)
        for s in self.symbols:
            print(f"{s[0]:>3} | {s[1]:<10} | {s[2]:<8} | {s[3]:<15} | {s[4]:>6}")

        print("\n=== FUNÇÕES ===")
        for f, info in self.functions.items():
            params_str = ", ".join(info["params"]) if info["params"] else ""
            print(f"{f}({params_str}) -> {info['retorno']}")

        if self.errors:
            print("\nERROS SEMÂNTICOS:")
            for e in self.errors:
                print(f" - {e}")
        else:
            print("\nNenhum erro semântico encontrado.")