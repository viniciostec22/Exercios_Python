'''7. Faça um Programa que leia três números e mostre o maior e o menor
deles.'''
n = []
for x in range(1,4):
    n.append(float(input(f"Digite o {x} numero: ")))

print("O maior numero é ", max(n))
print("O menor numero é ", min(n))