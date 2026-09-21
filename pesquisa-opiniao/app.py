#!/usr/bin/env python3

nome, idade, opiniao = "", 0, 0
excelente, bom, ruim = 0, 0, 0

for i in range(1, 4):
    nome = input(f"Digite nome[{i}]: ")
    idade = int(input(f"Digite idade[{i}]: "))
    opiniao = 0

    while True:

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

print("Excelente: ", excelente)
print("Ruim: ", ruim)
