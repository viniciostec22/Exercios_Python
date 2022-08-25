'''Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual
a sete;
• A mensagem "Reprovado", se a média for menor do que sete;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
from re import L


notas = []
cont, x = 1, 0
while(cont != 0):
    x += 1
    notas.append(float(input(f"Digite a {x} nota ")))
    cont = int(input("Digite qualquer tecla para inserir outra nota ou 0 para sair "))
   
media = sum(notas)/len(notas)
if(media>=7 and media < 10):
    print(f"Aluno aprovado com a media {media}")
elif(media == 10):
    print(f"Parabens!!! media obtida foi {media}")
else:
    print(f"Aluno reprovado por nota {media}")
