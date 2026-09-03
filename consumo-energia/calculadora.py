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

def main():

    TIT = "Calculadora de Consumo de Energia Elétrica"
    QAP = "Digite o nome do aparelho: "
    QPO = "Digite a potência do aparelho (W): "
    QTE = "Digite o tempo médio diário de uso (h): "

    # Apresentação
    limpa_tela()

    print("=" * 50)
    print("   ", TIT)
    print("=" * 50)
    print("\n")

    # Entrada
    print("=" * 50)
    aparelho = input(f"  {QAP}")
    potencia = float(input(f"  {QPO}"))
    tempo = float(input(f"  {QTE}"))
    print("=" * 50)
    print("\n")

    # Processamento
    consumo = (potencia * tempo * 30) / 1000.0

    # Saída
    print("=" * 50)
    print(f"  Aparelho: {aparelho}")
    print(f"  Consumo estimado: {consumo:.2f} kWh/mês")
    print("=" * 50)


if __name__ == "__main__":
    main()
