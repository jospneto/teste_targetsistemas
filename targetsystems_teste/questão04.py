faturamentMensal = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

def valorTotalFaturamento(dados):
    valorTotal = (dados['SP'] + dados['RJ'] + dados['MG'] + dados['ES'] + dados['Outros'])

    rj = (dados['RJ']/valorTotal) * 100
    sp = (dados['SP']/valorTotal) * 100
    es = (dados['ES']/valorTotal) * 100
    mg = (dados['MG']/valorTotal) * 100
    outros = (dados['Outros']/valorTotal) * 100

    print(f"Valor total: R${valorTotal: .2f}")
    print(f"Porcentagem do valor total da média do Rio de Janeiro: {rj: .2f}%")
    print(f"Porcentagem do valor total da média do São Paulo: {sp: .2f}%")
    print(f"Porcentagem do valor total da média do Espírito Santo: {es: .2f}%")
    print(f"Porcentagem do valor total da média do Minas Gerais: {mg: .2f}%")
    print(f"Porcentagem do valor total da média do Outros: {outros: .2f}%")

valorTotalFaturamento(faturamentMensal)
