def verifier(palabra):
    """
    Function that checks if a word is palidrome or not
    Inputs:
        palabra (str): the word to be checked
    Output:
        A boolean indicating if it palindrome or not
    """
    if str(palabra.lower()) == str(palabra.lower())[::-1]:
        print("Si es palindroma")
        return True
    else:
        print("No es palindroma")
        return False

word = input("Ingrese una palabra sin tildes: ")