def check_vowels():
    nombre = input("Ingresá un nombre: ").lower()

    print(f"Contiene a: {'a' in nombre}")
    print(f"Contiene e: {'e' in nombre}")
    print(f"Contiene i: {'i' in nombre}")
    print(f"Contiene o: {'o' in nombre}")
    print(f"Contiene u: {'u' in nombre}")

if __name__ == "__main__":
    check_vowels()
