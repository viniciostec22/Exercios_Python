'''12.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.'''
n_char = int(input("Informe o numero caracteres: "))
lista_char = []

for i in range (0,n_char):
    caracteres = str(input(f"Insira o {i+1} caractere: "))
    lista_char.append(caracteres)
print("Lista de caracteres: ",lista_char)

def conta_consoante(caracteres):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    consoantes = set(consoantes + consoantes.upper()) # incluir maiúsculas e minúsculas
    soma = 0
    for i in caracteres:
        if i in consoantes:
            soma += 1
    return soma

conta_consoante(lista_char)