'''6. Faça um Programa que leia três números e mostre o maior deles.'''

n = []
for x in range(1,4):
    n.append(float(input(f"Digite o {x} numero: ")))

print("O maior numero é", max(n))