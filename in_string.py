def check_vowels(nombre):
    nombre = nombre.lower()

    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"

    return {
        "a": a in nombre,
        "e": e in nombre,
        "i": i in nombre,
        "o": o in nombre,
        "u": u in nombre
    }

if __name__ == "__main__":
    nombre = input("Ingresá un nombre: ")
    resultados = check_vowels(nombre)
    for vocal, presente in resultados.items():
        print(f"Contiene {vocal}: {presente}")
