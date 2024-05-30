def evaluar(nombre_archivo):
	with open(nombre_archivo, "r", encoding="utf-8") as doc:
		lines = doc.readlines()

	matriz = [line.strip().split() for line in lines if line.strip()]
	patterns = [line.strip().split() for line in lines if not line.strip()]

	with open("resultado.txt", "w", encoding="utf-8") as output:
		for pattern in patterns:

			i = 0
			rows_found = []

			for i in range(len(matriz)):
				row = matriz[i]
				if len(row) == len(pattern) and match(row, pattern):
					i += 1
					rows_found.append(str(i))

			#output.write(f"{i} veces\n")

			if i > 0:
				output.write(" ".join(rows_found) + "\n\n")
			else:
				output.write("\n")


def match(row, pattern):
	for j in range(len(row)):
		if row[j] != pattern[j]:
			return False
	return True