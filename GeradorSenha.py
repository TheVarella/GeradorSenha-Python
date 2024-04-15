import random
import string


def generator_password(length):
    # adicionando todas as letras, números e pontuações
    char = string.ascii_letters + string.digits + string.punctuation

    # escolhendo caracteres aleátorios da variável "char" baseado no tamanho da senha (length)
    password = "".join(random.choice(char) for _ in range(length))
    return password


length = int(input("Qual o tamanho da senha que deseja criar? \n"))
print(f"A sua nova senha é: {generator_password(length)}\n")