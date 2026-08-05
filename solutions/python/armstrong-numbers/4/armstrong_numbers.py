def is_armstrong_number(number):
    algarismos = list(str(number))
    tamanho = len(algarismos)
    soma_final = 0
    for n in algarismos:
        if tamanho > 0:
            calculo = int(n) ** tamanho
            soma_final += calculo
    if soma_final == number:
            return True
    return False
#print(is_armstrong_number(number))






