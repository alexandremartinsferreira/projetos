#!/usr/bin/env python3

"""
    Sistema de Pesquisa de Opinião
"""

"""
Declaração de variáveis
"""

nome, idade, opiniao = "", 0, 0
excelente, bom, ruim = 0, 0, 0

"""
    Laço de repetição "for" estipulado para contar
    até 100 ou quanto for estipulado para o teste
    através de lista criada pelo comando range().
"""

print("Pesquisa de Opinião - TudoWeb\n")

for i in range(1, 11):
    """
        Recebe nome e idade com o indicador de índice
        para mostrar quantas pwssoas já foram
        contabilizadas na pesquisa. A variável
        opiniao é reiniciada em zero por causa do
        laço de repetição "while".
    """

    nome = input(f"Digite nome[{i}]: ")
    idade = int(input(f"Digite idade[{i}]: "))
    opiniao = 0

    """
        Repete o laço até que um valor que seja 
        validado pelo "match...case" execute um
        comando "break".
    """

    while True:

        """
            Conforme o valor da variavel "opiniao"
            seja 1, 2 ou 3, os acumuladores (ou
            contadores) armazenam o número de vezes 
            que uma determinada opinião foi 
            contabilizada para o fechamento posterior
            da pesquisa de opinião.

            Caso o valor esteja fora da faixa, o
            programa pedirá novamente o valor 
            de uma opinião válida.
        """

        match opiniao:
            case 1:
                excelente += 1
                break
            case 2:
                bom += 1
                break
            case 3:
                ruim += 1
                break
            case _:
                opiniao = int(input(f"Digite opinião[{i}] \
1-Excelente 2-Bom 3-Ruim: "))

"""
    Neste ponto não há mais laços de repetição.
    O programa exibirá a soma das opiniões que se
    declararam como "Excelente" e "Ruim".
"""

print(f"O total de opiniões que se declararam como \
\"Excelente\" foi de {excelente} pessoa(s).")

print(f"O total de opiniões que se declararam como \
\"Ruim\" foi de {ruim} pessoa(s).")
