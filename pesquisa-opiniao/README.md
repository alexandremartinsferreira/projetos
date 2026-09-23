# Sistema de Pesquisa de Opinião




Este programa feito em [Python](https://docs.python.org/pt-br/3/) trabalha com informações de 50 pesquisados sendo perguntadas em grupos de três perguntas:

- nome do entrevistado
- idade do entrevistado
- opinião do entrevistado

## Fórmula


Não são usadas fórmulas neste programa. Apenas soma de resultados cadastrados.


## Funcionamento

- Os dados de nome e data não são armazenados.
- Os dados de opinião são classificados e contwbilizados conforme sua categoria.
- Acusa erro se forem digitados valores não-numéricos para idade ou opinião.
- Para opinião, será aceito apenas um dos três valores abaixo:
-- 1 para Excelente
-- 2 para Bom
-- 3 para Ruim
- Caso seja digitado algum valor numérico inteiro diferente destes, a pergunta é refeita até a digitação de uma opinião válida ou erro com dado inválido


## Como Executar

### No Windows

- Abra o prompt de comando (CMD em Executar **cmd**)
- Tendo o Python já instalado, digite **python app.py**


### No Linux

- Abra o prompt de comando (Bash, Zsh, Ksh etc.)
- Dê permissão de execução ao programa (**chmod +x app.py**)
- Tendo o Python já instalado, digite na linha de comando **./app.py**



## Testes


Foi incluído um arquivo de imagem de testes feitos para dez entrevistados.
Os testes procedem com o funcionamento teórico do programa.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
