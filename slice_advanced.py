def slice_from_fifth(texto):
    return texto[4::2]

if __name__ == "__main__":
    texto = input("Ingresá un texto: ")
    resultado = slice_from_fifth(texto)
    print(resultado)
