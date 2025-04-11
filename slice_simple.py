texto = "Awesome".lower()

# Primeras 3 letras
primeras_tres = texto[0:3]

# Las 3 letras en el medio
mitad = len(texto) // 2
tres_del_medio = texto[mitad - 1:mitad + 2]

# De la primera a la cuarta (incluida) y de la antepenúltima a la última (incluida)
primera_a_cuarta = texto[0:5]
antepenultima_a_ultima = texto[-3:]

# Imprimir resultados
print(primeras_tres)
print(tres_del_medio)
print(primera_a_cuarta + antepenultima_a_ultima)
