import json

def faturamento():
    with open("dados.json") as arquivo:
        dados = json.load(arquivo)
    
    maiorValor(dados)
    menorValor(dados)
    mediaGeral(dados)

def maiorValor(dados):
    valores = []

    for contador in range(len(dados)):
        valores.append(dados[contador]["valor"])
    
    print(f"O maior valor do faturamento no mês é: R${max(valores):.2f}")

def menorValor(dados):
    valores = []
    valoresSemZero = []

    for contador in range(len(dados)):
        valores.append(dados[contador]["valor"])
        for contador in range(len(valores)):
            if(valores[contador] != 0.0):
                valoresSemZero.append(valores[contador])
    
    print(f"O menor valor do faturamento no mês é: R${min(valoresSemZero):.2f}")

def mediaGeral(dados):
    valores = []
    valoresSemZero = []
    valoresSupMedia = []
    media = 0
    qtdDiasSuperiores = 0

    for contador in range(len(dados)):
        valores.append(dados[contador]["valor"])
        for contador in range(len(valores)):
            if(valores[contador] != 0.0):
                valoresSemZero.append(valores[contador])
    
    media = sum(valoresSemZero)/len(valoresSemZero)
    
    for contador in range(len(dados)):
        if(dados[contador]["valor"] > media):
            valoresSupMedia.append(dados[contador]["dia"])
            qtdDiasSuperiores += 1
    
    formatacao = ", ".join(map(str,valoresSupMedia))
    
    print(f"Quantidade de dias em que o valor foi maior que a média geral foram {qtdDiasSuperiores}")
    print(f"Sendo os dias respectivamente: {formatacao}")
    
faturamento()