import json

#A função de faturamento tem como objetivo ler o arquivo json e chamar as demais funções.
def faturamento():
    with open("dados.json") as arquivo:
        dados = json.load(arquivo)
    
    maiorValor(dados)
    menorValor(dados)
    mediaGeral(dados)

#Função de maior valor que recebe como paramentro o arquivo json contendo os dados.
def maiorValor(dados):
    #O array vazio que recebe os valores que estão contido no arquivo.
    valores = []

    #O laço de repetição percorre o arquivo de dados.
    for contador in range(len(dados)):
        #Atraves do indice e da sua chave no json é adicionado os valores no array de valores.
        valores.append(dados[contador]["valor"])
    
    #Aqui é printado o maior valor utilizando a função max que busca automaticamente o maior valor dentro de um array.
    print(f"O maior valor do faturamento no mês é: R${max(valores):.2f}")

def menorValor(dados):
    #O array vazio que recebe os valores que estão contido no arquivo.
    valores = []
    #O array vazio que recebe os valores que estão contido no arquivo mas sem os que tem 0.0 pois contam como feriados e finais de semana.
    valoresSemZero = []

    #O laço de repetição percorre o arquivo de dados.
    for contador in range(len(dados)):
        #Atraves do indice e da sua chave no json é adicionado os valores no array de valores.
        valores.append(dados[contador]["valor"])
        #Esse outro for percorre o array de valores junto a uma estrutura condicional verifica qual os valores não zeros e adiciona no outro array de valores.
        for contador in range(len(valores)):
            if(valores[contador] != 0.0):
                valoresSemZero.append(valores[contador])
    
    #Com a função min é mostrado o menor valor dentro do array de valores sem os zeros. Parecida com a max ela busca o menor valor dentro de um array ao invés do maior.
    print(f"O menor valor do faturamento no mês é: R${min(valoresSemZero):.2f}")

#Funçaõ que traz a média geral e os valores maiores que a média.
def mediaGeral(dados):
    #Iniciação das variaveis e arrays.
    valores = []
    valoresSemZero = []
    valoresSupMedia = []
    media = 0
    qtdDiasSuperiores = 0

    #Mesmo for da função menorValor.
    for contador in range(len(dados)):
        valores.append(dados[contador]["valor"])
        for contador in range(len(valores)):
            if(valores[contador] != 0.0):
                valoresSemZero.append(valores[contador])
    
    #A média é a soma de todos os valores do array ignorando os zeros divida pela quantidade de objetos dentro do array.
    #Aqui a função sum já realiza essa soma de todos os elementos do array. Utilizando a função len que lê o tamanho do array da para saber sua quantidade.
    media = sum(valoresSemZero)/len(valoresSemZero)
    
    #Aqui busca saber quais os dias os valores foram maiores que a média.
    for contador in range(len(dados)):
        #Esta condiconal verifica se algum valor é maior que a média caso sim é adicionado no array de valoresMaiores que a média de acordo com o dia em questão.
        if(dados[contador]["valor"] > media):
            valoresSupMedia.append(dados[contador]["dia"])
            #Aqui é para saber a quantidade de dias onde isso ocorreu. Caso o if dê verdadeiro o contador será incrementado, caso não ele continuará o laço.
            qtdDiasSuperiores += 1
    
    #aqui é uma formatação utlizando map e join que permite que os colchetes do array sejam retirados da string. Com o join ele vai adicionar ou retirar espaços de um array ou string. Já o map permite atribuir uma função a cada item de uma lista. 
    formatacao = ", ".join(map(str,valoresSupMedia))
    
    print(f"Quantidade de dias em que o valor foi maior que a média geral foram {qtdDiasSuperiores}")
    print(f"Sendo os dias respectivamente: {formatacao}")
    
faturamento()