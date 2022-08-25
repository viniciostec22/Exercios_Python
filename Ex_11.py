'''11.Altere o programa de cálculo dos números primos, informando, caso o
número não seja primo, por quais número ele é divisível.'''
numero = int(input("Digite um numero "))
for x in range(1, numero+1):
      if (numero % x ==0):
        print(x, end=" ")
    
        

