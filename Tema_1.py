
def tema1(cadena):
	cantidad_R = cadena.count('R')
	cantidad_G = cadena.count('G')
	cantidad_B = cadena.count('B')

	cantidades = sorted((cantidad_R, cantidad_G, cantidad_B))

	if cantidades.count(0) == 2:
		return(0)
	else:
		salida = sum(cantidades[0:2])
		return(salida)


def main():
	cadenas = []

	T = int(input(""))

	for t in range(T):
		N = int(input(""))

		S = input("")

		cadenas.append(S)

	for c in cadenas:
		print(tema1(c))

main()