def verifier(palabra):
    if str(palabra.lower()) == str(palabra.lower())[::-1]:
        print("Si es palindroma")
        return True
    else:
        print("No es palindroma")
        return False

word = input("Ingrese una palabra sin tildes: ")