from itertools import permutations, product
import numpy

def Tema3(sucesiones):
	n = len(sucesiones)
	G = 0
	for k in range(2, n + 1):
		N = range(1, n + 1)
		m = len(sucesiones[0])
		M = range(1, m + 1)

		#eleccion de los i's
		permutaciones = tuple(permutations(N, k))
		permutaciones_crecientes = []
		for p in permutaciones:
			if p == tuple(sorted(p)):
				permutaciones_crecientes.append(p)


		js = tuple(product(M, repeat = k))

		for i in permutaciones_crecientes:
			suecesiones_electas = []
			for j in i:
				suecesiones_electas.append(sucesiones[j - 1])

			for e in js:
				q = 0
				lista_A = []
				for y in e:
					lista_A.append(suecesiones_electas[q][y - 1])
					q += 1
				
				G += numpy.gcd.reduce(lista_A)

	return(G % (10**9 + 7))


def main():
	T = int(input("").split(' ')[0])

	sucesiones = []
	for t in range(T):
		S_str = input("").split(' ')

		S = []
		for i in S_str:
			S.append(int(i))

		sucesiones.append(S)

	print(Tema3(sucesiones))

main()
