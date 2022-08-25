'''Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total.'''
import math

area_a_ser_pintada = int(input("Tamanho da area a ser pintada "))
litros_por_lata = 18
valor_da_lata = 80
litros_a_serem_usados = area_a_ser_pintada /3
latas_usadas = litros_a_serem_usados

numero_de_latas = litros_a_serem_usados / litros_por_lata
numero_de_latas = math.ceil(numero_de_latas)
total_paga = numero_de_latas * valor_da_lata

print(f"Latas de tintas usadas {numero_de_latas} valor unt R$ {valor_da_lata} Total a Pagar R$ {total_paga}")