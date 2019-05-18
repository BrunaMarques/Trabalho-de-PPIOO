class Tree:
	def __init__(self, token, left, right):
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
		listaTokens.append(token)
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



def Parser(filaTokens):
	operadores = ["+", "-", "*", "/"]
	for i in range(len(filaTokens)):
		if filaTokens[i] in operadores:
			no = Tree(filaTokens[i], filaTokens[i-2], filaTokens[i-1])
			print(no)
			filaTokens[i] = no
			filaTokens.pop(i-1)
			filaTokens.pop(i-1)
			if len(filaTokens) > 0:
				Parser(filaTokens)
			break
	print(filaTokens)


def main():

	stringEntrada = input("Insira a expressão aritmética: ")
	x = lexer(stringEntrada)
	x = ShuntingYard(x)
	Parser(x)
if __name__ == "__main__":
	main()

