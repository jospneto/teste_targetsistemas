#O dicionário(Object) com cada estado e o seu faturamento.
faturamentMensal = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

#A função que vai pegar o valor total do faturamento dos estados.
def valorTotalFaturamento(dados):
    #Soma todos os valores de cada estado para dar o total.
    valorTotal = (dados['SP'] + dados['RJ'] + dados['MG'] + dados['ES'] + dados['Outros'])

    #Aqui é feita o calculo de qual valor em porcentagem cada estado tem em relação ao valor total. Onde o valor de receita de cada estado é dividido pelo valor total e multiplicado por 100.
    rj = (dados['RJ']/valorTotal) * 100
    sp = (dados['SP']/valorTotal) * 100
    es = (dados['ES']/valorTotal) * 100
    mg = (dados['MG']/valorTotal) * 100
    outros = (dados['Outros']/valorTotal) * 100

    #É mostrado os valores do valor total e da porcentagem de cada estado.
    print(f"Valor total: R${valorTotal: .2f}")
    print(f"Porcentagem do valor total da média do Rio de Janeiro: {rj: .2f}%")
    print(f"Porcentagem do valor total da média do São Paulo: {sp: .2f}%")
    print(f"Porcentagem do valor total da média do Espírito Santo: {es: .2f}%")
    print(f"Porcentagem do valor total da média do Minas Gerais: {mg: .2f}%")
    print(f"Porcentagem do valor total da média do Outros: {outros: .2f}%")

valorTotalFaturamento(faturamentMensal)
