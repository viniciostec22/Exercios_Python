'''2. Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
notas = []
for x in range(1,5):
    notas.append(float(input(f"Digite a {x} nota ")))

media = sum(notas)/len(notas)

print(f"A media alcansada foi {media}")