# Sistema de Descontos Progressivos




Este programa feito em [Python](https://docs.python.org/pt-br/3/) usa uma informação:

- valor gasto em compras


## Faixas


Através de estruturas de decisão ele calcula o valor de desconto a ser dado dentre valores de descontos progressivos a ser abatido no valor final a ser pago:

- desconto de 5% para valores inferiores a 200
- desconto de 10% para valores superiores ou iguais a 200 e inferiores a 300
- dwsconto de 15% para valores superiores a 300


## Fórmulas


Os cálculos são feitos baseados no valor de compra e na taxa de desconto selecionada

- abatimento = valor de compra * desconto / 100
- valor a pagar = valor de compra - abatimento


## Funcionamento


- O programa critica caso sejam digitados valor nulo ou negativo
- Não funciona se for digitado valor não-numérico


## Como Executar

### No Windows

- Abra o prompt de comando (CMD em Executar **cmd**)
- Tendo o Python já instalado, digite **python descontos.py**


### No Linux

- Abra o prompt de comando (Bash, Zsh, Ksh etc.)
- Dê permissão de execução ao programa (**chmod +x descontos.py**)
- Tendo o Python já instalado, digite na linha de comando **./descontos.py**


## Testes 

Há um arquivo de print de tela de com um teste automatizado usando shell script dentro do diretório dos arquivos.
Na imagem da tela são apresentadas as respostas do programa, conforme os valores são aceitos pelo programa.
Na automatização, os valores digitados só aparecem no resultado doa cálculos do programa.
Ainda na tela, é apresentado o script de automação de testes, digitado diretamente em linha de comando.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
