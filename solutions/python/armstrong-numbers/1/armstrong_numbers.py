
    # preciso saber a quantia de dígitos ou algarismos: como?
    #talvez iterar. Preciso separar os dígitos.
    # se for dois algarismos, cada digito é elevado ao quadrado
    # e a soma entre eles deve ser igual ao numero original
    # se for 3, elevo ao cubo cada algarismo.
    

    #transformar os digitos em uma lista 


def is_armstrong_number(number):

    #transformar os digitos em uma lista 

    algarismos = list(str(number))

    quantia_digitos = len(algarismos)

    soma_total = 0


    for j in range(quantia_digitos):

        num = int(algarismos[j])

        soma_total += (num ** quantia_digitos)


    if soma_total == number:
        return True 
    else:
        return False


print(is_armstrong_number(153))
