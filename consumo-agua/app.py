#!/uar/bin/env python3

"""
    Progeama para mensagens ao consumidor conforme
    classificação do perfil do consumo de água
"""

"""
    Neste programa existem três tipos de imóveis
    para serem escolhidos de 1 a 3
"""

imovel = int(input("Digite o tipo de imóvel:\n\
       1 - Comercial\n\
       2 - Casa\n\
       3 - Apartamento\n ==> "))

"""
    Caso seja digitado um valor inválido,
    o programa é encerrado.
    Valores não-numéricos causam erro em
    tempo de execução.
"""

if imovel != 1 and imovel != 2 and imovel != 3:
    print("Escolha um número válido.")
    quit()

"""
    Recebe valor do consumo em metros cúbicos.
    Valores não-numéricos causam erro em
    tempo de execução.
"""

consumo = float(input("Digite o consumo de água em m³: "))

if imovel == 1: 
    """Comercial"""
    print("Tarifa comercial aplicada - consulte o plano corporativo.")
elif imovel == 3 and consumo < 10:
    """Apartamento de consumo inferior a 10"""
    print("Consumo econômico - excelente controle de água!")
elif (imovel == 2 or imovel == 3) and consumo < 25:
    """Apartamento ou casa de consumo inferior a 25"""
    print("Consumo moderado - dentro do padrão residencial.")
else:
    """Qualquer outro caso"""
    print("Consumo excessivo - adote medidas preventivas e evite vazamentos.")
