#!/usr/bin/env python3


"""
   Programa para cálculo de consumo de energia 
   de um aparelho elétrico em kWh
"""

import os

def limpa_tela():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Apresentação
limpa_tela()

print("=" * 50)
print("        Calculadora de Consumo de Energia   ")
print("=" * 50)
print("\n")

# Entrada
print("=" * 50)
aparelho = input("  Digite o nome do aparelho: ")
potencia = float(input("  Digite a potência do aparelho elétrico (W): "))
tempo = float(input("  Digite o tempo médio diário de uso (h): "))
print("=" * 50)
print("\n")

# Processamento
consumo = (potencia * tempo * 30) / 1000.0

# Saída
print("=" * 50)
print(f"  Aparelho: {aparelho}")
print(f"  Consumo estimado: {consumo:.2f} kWh/mês")
print("=" * 50)
