# Classe árvore:
class Tree:

# Um nó da árvore possui o token, e os filhos da esquerda e da direita.
	def __init__(self, token, left = None, right = None):
		self.token = token
		self.right = right
		self.left = left

# Função para separar a string de entrada por números, operadores e parênteses.
def lexer(stringEntrada):
	operadores = ["+", "-", "*", "/", "(", ")"]
	# Removendo os espaços da entrada.
	stringEntrada = stringEntrada.split(" ")
	stringEntrada = ''.join(stringEntrada)
	# Variável para ajudar no tratamento de sinal negativo.
	operadorAntes = 1
	token = ""
	listaTokens = []
	# Tratamento de caracter por caracter da string de entrada.
	for ch in stringEntrada:
		# Se não veio operador antes, o próximo símbolo não será um sinal negativo.
		if operadorAntes == 0:
			if ch in operadores:
				# Se for um operador, significa que o elemento anterior pode ser colocado na lista pois não terá mais concatenação.
				if len(token) > 0:
					if token in operadores:
						listaTokens.append(token)
						token = ""
					else:
						listaTokens.append(int(token))
						token = ""
				listaTokens.append(ch)
				if ch != ")":
					operadorAntes = 1
				# Se não é um operador, concatenamos o número no token (números com mais de 1 caracter).
			else:
				token = token + ch
				operadorAntes = 0
		# Caso veio um operador antes, podemos ter o caso do sinal negativo em sequência e devemos tratá-lo
		elif operadorAntes == 1:
			# Antes de vir o sinal negativo, também podem vir parênteses. Adicionamos ele na lista normalmente e continuamos com a flag = 1.
			if ch == "(" or ch == ")":
				listaTokens.append(ch)
				token = ""
			# Se é um operador, é o sinal do número. Adicionamos ele ao token.
			elif ch in operadores:
				if token in operadores:
					listaTokens.append(token)
				token = ch
			# Caso seja um número, concatenamos ele ao token.
			else:
				token = token + ch
				operadorAntes=0
	if len(token) > 0:
		listaTokens.append(int(token))
	return listaTokens

# Verificar se o operador do topo pilha tem maior ou igual precedência sobre o operador da lista
def greaterPrecedence(opList, opPilha):

	if opPilha == "/" or opPilha == "*":
		return True
	elif opList == "/" or opList == "*" or opPilha == "(":
		return False
	return True

# Função para gerar a expressão aritmética na forma de polonesa reversa.
def ShuntingYard(listaTokens):
	fila = []
	pilha = []
	operadores = ["+", "-", "*", "/"]
	for token in listaTokens:
		if token in operadores:
			if pilha:
				# Enquanto o topo da pilha possuir precedencia maior ou igual ao token da lista, desempilhamos ele da pilha e colocamos na fila.
				while greaterPrecedence(token, pilha[-1]):
					fila.append(pilha.pop())
					if not pilha:
						break
			pilha.append(token)
		elif token == "(":
			pilha.append(token)
		elif token == ")":
			if pilha:
				# Caso o token seja um "fecha parênteses" e o topo da pilha seja um "abre parênteses", desempilhamos e colocamos na fila
				while pilha[-1] != "(":
					fila.append(pilha.pop(-1))
					if not pilha:
						break
			pilha.pop(-1)
		else:
			fila.append(token)
	if pilha:
		# Colocamos todos os operadores que sobraram da pilha na fila.
		while pilha[-1] in operadores:
			fila.append(pilha.pop(-1))
			if not pilha:
				break
	return fila	

""" Função para testar se a árvore está certa:

def printarArvore(arvore, level):
	for i in range(level*4):
		print(' ', end='')
	if type(arvore) is not int:
		print(arvore.token)
		if type(arvore.token) is str:
			printarArvore(arvore.left, level+1)
			print()
			printarArvore(arvore.right, level+1)
	else:
		print(arvore, end = " ")
"""

# Função para construir a árvore binária de expressão a partir da fila de tokens.
def Parser(filaTokens):
	operadores = ["+", "-", "*", "/"]
	# Procuramos na lista um operador, e criamos um nó deste operador em que o filho da esquerda é a posição i-2 e o filho da direita é i-1 e colocamos no lugar do operador.
	for i in range(len(filaTokens)):
		if filaTokens[i] in operadores:
			no = Tree(filaTokens[i], filaTokens[i-2], filaTokens[i-1])
			filaTokens[i] = no
			# Removemos os elementos i-1 e i-2 que são filhos do operador da fila
			filaTokens.pop(i-1)
			filaTokens.pop(i-2)
			# Se há mais de um elemento na fila, a árvore ainda não está completa e chamamos a função recursivamente.
			if len(filaTokens) > 1:
				Parser(filaTokens)
			break
	return filaTokens

# Função para executar um passo da solução da expressão na árvore.
def evalStep(arvore):

	# Iremos fazer uma procura in-ordem de um operador em que seus filhos sejam inteiros. Então, salvaremos a árvore original para retornar no futuro.
	arvoreReal = arvore
	direcao = ""

	# Descemos na árvore a procura do operador com filhos inteiros, sempre guardando a direção em que estamos descendo para podermos alterarmos esse nó posteriormente
	if type(arvore.token) is not int:
		while type(arvore.left) is not int or type(arvore.right) is not int:
			if type(arvore.left) is int:
				direcao = "right"
				arvorePai = arvore
				arvore = arvore.right
			else:
				direcao = "left"
				arvorePai = arvore
				arvore = arvore.left

	# Quando acharmos o operador, realizamos a operação e trocamos o nó pelo inteiro que representa o resultado da operação.

	if arvore.token == "+":
		if direcao == "right":
			arvorePai.right = arvore.left + arvore.right
		elif direcao == "left":
			arvorePai.left = arvore.left + arvore.right
		else:
			arvoreReal = arvore.left + arvore.right
	elif arvore.token == "-":
		if direcao == "right":
			arvorePai.right = arvore.left - arvore.right
		elif direcao == "left":
			arvorePai.left = arvore.left - arvore.right
		else:
			arvoreReal = arvore.left - arvore.right
	elif arvore.token == "/":
		if direcao == "right":
			if arvore.right == 0:
				arvorePai.right = 1
			else:
				arvorePai.right = int(arvore.left / arvore.right)
		elif direcao == "left":
			if arvore.right == 0:
				arvorePai.left = 1
			else:
				arvorePai.left = int(arvore.left / arvore.right)
		else:
			if arvore.right == 0:
				arvoreReal = 1
			else:
				arvoreReal = int(arvore.left / arvore.right)
	elif arvore.token == "*":
		if direcao == "right":
			arvorePai.right = arvore.left * arvore.right
		elif direcao == "left":
			arvorePai.left = arvore.left * arvore.right
		else:
			arvoreReal = arvore.left * arvore.right
	return arvoreReal


# Função para transformarmos a árvore em uma String equivalente a expressão aritmética.
def toString(arvore, string, flag):

	# Caso a flag seja 1, significa que devemos colocar parênteses na expressão que iremos printar.
	flagAux = 0
	if flag == 1:
		string = string + "("
		flagAux = 1

	# Fazemos uma busca in-ordem para verificar se o sinal do filho possui precedência menor que o pai. Caso seja, a flag é settada como 1 pois precisaremos de parênteses.
	if type(arvore) is not int:
		if type(arvore.token) is str:
			if (arvore.token == "*" or arvore.token == "/") and (type(arvore.left) is not int):
				if arvore.left.token == "+" or arvore.left.token == "-":
					flag = 1
				else:
					flag = 0
			else: 
				flag = 0
			string = toString(arvore.left, string, flag)
			# Concatenamos a string com o operador
			string = string + " " + arvore.token + " "
			if (arvore.token == "*" or arvore.token == "/") and (type(arvore.right) is not int):
				if arvore.right.token == "+" or arvore.right.token == "-":
					flag = 1
				else:
					flag = 0
			else:
				flag = 0
			string = toString(arvore.right, string, flag)
	else:
		string = string + str(arvore)
	if flagAux == 1:
		string = string + ")"
		flag = 0
	return string


def main():

	stringEntrada = input()
	while stringEntrada:
		x = lexer(stringEntrada)
		x = ShuntingYard(x)
		arvore = Parser(x)
		print(toString(arvore[0], "", 0))
		while type(arvore[0]) is not int:
			arvore[0] = evalStep(arvore[0])
			print(toString(arvore[0], "", 0))
		print()
		stringEntrada = input()
if __name__ == "__main__":
	main()

