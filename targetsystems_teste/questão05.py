#Função que inverte a string
def inverteString(string):
    #Array vazio que vai receber cada caracter da string de forma invertida.
    stringInvertida = []

    #tamanho da string.
    tamanho = len(string)
    #O laço de repetição que enquanto o tamanho da string for maior que zero ele vai continuar repetindo até que chegue no último caracter da string.
    while tamanho > 0:
        #aqui o array vai recebendo cada caracter do string de acordo com o indice começando de trás para frente por isso o menos 1. Ele começa do último indice ou seja do último caracter.
        stringInvertida.append(string[tamanho-1])
        #após que o caracter seja adiciona ao array o tamanho é decrementado até que chegue a 0.
        tamanho -= 1
    
    #aqui é uma formatação utlizando map e join que permite que os colchetes do array sejam retirados da string. Com o join ele vai adicionar ou retirar espaços de um array ou string. Já o map permite atribuir uma função a cada item de uma lista. 
    formatacao = "".join(map(str,stringInvertida))
    #aqui com a função upper todos os caracteres ficarão maiúsculos.
    print(f"Palavra invertida: {str.upper(formatacao)}")

string = input("Digite uma palavra: ")
inverteString(string)