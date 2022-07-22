def inverteString(string):
    string_Invertida = []

    for contador in range(len(string)):
        string_Invertida += string[contador-1]
        contador -= 1
    
    formatacao = "".join(map(str,string_Invertida))
    print(f"Palavra invertida: {formatacao}")

string = input("Digite uma palavra: ")
inverteString(string)