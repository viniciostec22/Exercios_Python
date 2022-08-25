'''10.Faça um programa que peça um número inteiro e determine se ele é ou
não um número primo. Um número primo é aquele que é divisível somente
por ele mesmo e por 1.'''

def primo(n):
    for x in range(2, n//2 +1):
        if (n % x ==0):
            return False
        return True

numero = int(input("Digite um numero "))
if(primo(numero)):
    print(f"O numero {numero} é Primo")
else:
    print(f"O numero {numero} não é Primo")