#!/uar/bin/env python3

imovel = int(input("Digite o tipo de imóvel:\n\
       1 - Comercial\n\
       2 - Casa\n\
       3 - Apartamento\n ==> "))

if imovel != 1 and imovel != 2 and imovel != 3:
    print("Escolha um número válido.")
    quit()

consumo = float(input("Digite o consumo de água em m³: "))

if imovel == 1:
    print("Tarifa comwrcial aplicada - consulte o plano corporativo.")
elif imovel == 3 and consumo < 10:
    print("Consumo econômico - excelente controle de água.")
elif (imovel == 2 or imovel == 3) and consumo < 25:
    print("Consumo moderado - dentro do padrão residencial.")
else:
    print("Consumo excessivo - adote medidas preventivas e evite vazamentos.")
