# Classificação de Perfil de Consumo de Água




Este programa feito em [Python](https://docs.python.org/pt-br/3/) usa duas informações:

- perfil do imóvel avaliado
- volume do consumo de água em metros cúbicos


## Faixas


Através de estruturas de decisão ele emite mensagens de advertência sobre o consumo de água:
- Se o tipo for "comercial", exibir: Tarifa comercial aplicada – consulte o plano corporativo."
- Se o tipo for "apartamento" e o consumo for menor que 10 m3 , exibir: "Consumo econômico – excelente controle de água!"
- Se o tipo for "apartamento" ou for "casa" com consumo de até 25 m3 , exibir: "Consumo moderado – dentro do padrão residencial."
- Em qualquer outro caso (consumo acima do limite residencial), exibir: "Consumo excessivo – adote medidas de economia e verifique vazamentos."


## Fórmulas


O programa não usa fórmulas. Apenas avaliações sobre o perfil do imóvel e quantidade de água consumida.


## Funcionamento


- O programa critica caso seja digitada escolha diferente dos domicílios apresentados.
- Não funciona se forem digitados valores não-numéricos. 


## Como Executar

### No Windows

- Abra o prompt de comando (CMD em Executar **cmd**)
- Tendo o Python já instalado, digite **python app.py**


### No Linux

- Abra o prompt de comando (Bash, Zsh, Ksh etc.)
- Dê permissão de execução ao programa (**chmod +x app.py**)
- Tendo o Python já instalado, digite na linha de comando **./app.py**


## Testes 

Há um arquivo de print de tela dentro do diretório dos arquivos.
Na imagem da tela, são apresentadas as respostas do programa, conforme os valores são digitados nas várias execuções da aplicação.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
