from stack import Stack

def isPalindromo(word):

    inverseWord = Stack(len(word))
    palindromo = True

    for char in word:
        inverseWord.push(char)

    for char in word:
       palindromo = palindromo and (char.lower() == inverseWord.pop().lower())

    print("é um palíndromo") if palindromo else print("Não é um palíndromo")


isPalindromo('subinoonibus')
# isPalindromo('Ana')