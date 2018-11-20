from itertools import permutations

def C_count(cadena):
	C = {}
	for i in range(len(cadena)):
		letra_i = cadena[i]
		if letra_i not in C:
			C[letra_i] = cadena.count(letra_i)

	C_str = ''
	for i in C.keys():
		C_str += i

	return(C, C_str)

def tema2(cadena):
	C_C_str = C_count(cadena)
	C_dict = C_C_str[0]
	C_str = C_C_str[1]

	permutaciones = tuple(permutations(C_str))

	for p in permutaciones:
		cont = 0
		for i in range(len(p) - 2):
			l1 = p[i+2]
			l2 = p[i+1]
			l3 = p[i]

			if C_dict.get(l1) != (C_dict.get(l2) + C_dict.get(l3)):
				break
			else:
				cont += 1

		if cont == (len(p)-2):
			return("Dynamic")
			break

	return("Not")

def main():
	cadenas = []
	T = int(input(""))

	for t in range(T):
		S = input("")

		cadenas.append(S)

	for c in cadenas:
		print(tema2(c))

main()
