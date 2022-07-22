##Função que gera a sequência de fibonnaci, ela recebe a quantidade e o número a ser verificado.
def fibonnaci(quantidade, numero):
    #o ultimo dígito.
    ultimo = 1
    #o penultimo dígito.
    penultimo = 1
    #o array que vai armazenar a sequência.
    sequencia = []

    #nesta estrutura condicional o objeto é verificar a quantidade de digitos que a sequência terá.
    #caso a quantidade seja 1 o único dígito que ele irá printar será o zero dando início a sequência.
    if(quantidade == 1):
        print("0")
    #caso a quantidade seja 2 ele irá printar será o 0 e o 1 dando início a sequência.
    elif(quantidade == 2):
        print("0","1")
    #quando nenhuma dessas exigências forem atendidadas ele vai printar a sequência completa.
    else:
        #aqui é adicionado o penultimo termo e o último no array. O penultimo é subtraído 1 do seu valor para que o 0 esteja dentro do array.
        sequencia.append(penultimo-1)
        sequencia.append(ultimo)
        print("+-------------+SEQUÊNCIA DE FIBONNACI+-------------+")
        print(f"0\n{ultimo}\n{penultimo}")
        #o laço de repetição utilizado é o for que tem tamanho definido subtraindo a quantidade menos 3 que seria o 3 primeiro digitos da sequência, 0, 1 e a soma dos dois que é 1 também.
        for contador in range(quantidade - 3):
            #aqui acontece a soma dos dígitos o ultimo e penultimo.
            termo = ultimo + penultimo
            #para que de continuidade a sequência vai haver uma inversão onde o penultimo recebe o ultimo e o ultimo recebe o termo atual. 
            penultimo = ultimo
            ultimo = termo
            #o contador é incrementado para o laço continuar até o fim.
            contador += 1
            #o termo é adicionado ao array.
            sequencia.append(termo)
            #aqui ele vai printar os termos de acordo com a sequência.
            print(termo)
    #a função que verifica se o número pertence a sequência é chamada recebendo o array e o número.
    verificarNumero(sequencia, numero)

#Função que verifica se o número pertence ou não a sequência de fibonnaci
def verificarNumero(array, numero):
    #um for que percorre o array de acordo com o seu tamanho.
    for contador in range(len(array)):
        mensagem = " "
        #caso o número seja igual a algum elemento do array o número pertence a sequência.s
        if(numero == array[contador]):
            mensagem = f"O número {numero} pertence a sequência de fibonnaci."
            break
        else:
            mensagem = f"O número {numero} não pertence a sequência de fibonnaci."
    print(mensagem)
        
    
quantidade = int(input("Digite a quantidade de números para a série de fibonnaci: "))
numero = int(input("Digite um número para verificar se ele pertence a sequência de fibonnaci: "))
fibonnaci(quantidade, numero)
