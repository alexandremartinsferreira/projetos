#!/usr/bin/env python3

"""Programa para cálculo de descontos
   em compras por faixa de valores estipulados
"""

# recebe valor gasto em compras
compra = float(input("Digite o valor da compra: "))

# declaração das variáveis que receberão os valores de
# desconto, valor a ser abatido e total a ser pago
desconto = 0.0
abatimento = 0.0
total = 0.0

# início das verificações condicionais


if compra >= 300: # se a compra for superior ou igual a 300
    desconto = 15 # desconto será de 15%

# se a compra for superior ou igual a 200 e inferior a  300
elif compra >= 200 and compra < 300: 
    desconto = 10 # desconto será de 10%


# se a compra for inferior a 200 e superior a zero
elif compra < 200 and compra > 0: 
    desconto = 5 # desconto será igual a 5%

else: # caso nenhuma condição acima se verifique
      # isto é valor zero ou negativo
      # apresentará uma mensagem de orientação
    print("Digite valor diferente de zero ou não-negativo.")

# este condicional verifica se a variável de desconto
# sofreu alteração, ou seja, executar uma sequência de
# código sem necessidade de repetição para exibir a
# informação de desconto e pagamento inúmeras vezes no
# código economizando recursos e facilitando a leitura

if desconto != 0: # se houve desconto

    # calcula abatimento do valor da compra
    abatimento = compra * (desconto / 100.0)

    # calcula o total a ser pago descontando o
    # valor a ser abatido
    total = compra - abatimento

    # exibe informações formatadas sobre
    # valor gasto, desconto, abatimento e total a ser pago
    print(f"Voce comprou {compra:.2f} em mercadorias.")
    print(f"e teve {desconto}% de desconto")
    print(f"com um abatimento de {abatimento:.2f}")
    print(f"pagando no total o valor de {total:.2f}")
