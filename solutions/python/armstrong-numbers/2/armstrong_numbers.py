#numero de armstrong
# 9 tem um dígito logo, 9 elevado a 1 é o proprio 9
# 10 não é um armstrong number pois a soma dos dois digito elevado a 2 não resulta em 10.
''' 153is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 '''

def is_armstrong_number(number):


    algarismos = list(str(number))

    print(algarismos)
    tamanho = len(algarismos)
    print("A quantia de digitos é: ", tamanho)
    soma_final = 0

    for n in algarismos:

        if tamanho > 0:
            calculo = int(n) ** tamanho
            soma_final += calculo

    if soma_final == number:
            return True

    else:
            return False

#print(is_armstrong_number(number))






