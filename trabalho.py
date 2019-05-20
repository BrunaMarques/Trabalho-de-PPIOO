import operator

class Tree:
	def __init__(self, token, left = None, right = None):
		self.token = token
		self.right = right
		self.left = left

def lexer(stringEntrada):
	operadores = ["+", "-", "*", "/", "(", ")"]
	# Removendo os espaços da entrada
	stringEntrada = stringEntrada.split(" ")
	stringEntrada = ''.join(stringEntrada)
	# Variável para ajudar no tratamento de sinal negativo
	operadorAntes = 1
	token = ""
	listaTokens = []
	# Tratamento de caracter por caracter da string de entrada
	for ch in stringEntrada:
		if operadorAntes == 0:
			if ch in operadores:
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
			else:
				token = token + ch
				operadorAntes = 0
		elif operadorAntes == 1:
			if ch == "(" or ch == ")":
				listaTokens.append(ch)
				token = ""
			elif ch in operadores:
				if token in operadores:
					listaTokens.append(token)
				token = ch
			else:
				token = token + ch
				operadorAntes=0
	if len(token) > 0:
		listaTokens.append(int(token))
	print (listaTokens)
	return listaTokens


def ShuntingYard(listaTokens):
	fila = []
	pilha = []
	operadores = ["+", "-", "*", "/"]
	for token in listaTokens:
		if token in operadores:
			if pilha:
				while pilha[-1] == "/" or pilha[-1] == "*":
					fila.append(pilha.pop(-1))
					if not pilha:
						break
			pilha.append(token)
		elif token == "(":
			pilha.append(token)
		elif token == ")":
			if pilha:
				while pilha[-1] != "(":
					fila.append(pilha.pop(-1))
					if not pilha:
						break
			pilha.pop(-1)
		else:
			fila.append(token)
	if pilha:
		while pilha[-1] in operadores:
			fila.append(pilha.pop(-1))
			if not pilha:
				break
	print(fila)	
	return fila	

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

def Parser(filaTokens):
	operadores = ["+", "-", "*", "/"]
	for i in range(len(filaTokens)):
		if filaTokens[i] in operadores:
			no = Tree(filaTokens[i], filaTokens[i-2], filaTokens[i-1])
			filaTokens[i] = no
			filaTokens.pop(i-1)
			filaTokens.pop(i-2)
			if len(filaTokens) > 1:
				Parser(filaTokens)
			break
	return filaTokens

def evalStep(arvore):

	arvoreReal = arvore
	direcao = ""
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
			arvorePai.right = int(arvore.left / arvore.right)
		elif direcao == "left":
			arvorePai.left = int(arvore.left / arvore.right)
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


def main():

	stringEntrada = input("Insira a expressão aritmética: ")
	x = lexer(stringEntrada)
	x = ShuntingYard(x)
	arvore = Parser(x)
	print("\n")
	printarArvore(arvore[0], 0)
	print("\n\n")
	while type(arvore[0]) is not int:
		arvore[0] = evalStep(arvore[0])
		printarArvore(arvore[0], 0)
		print("\n\n")
	print()
if __name__ == "__main__":
	main()

