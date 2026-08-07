"""Módulo para verificar se um número é um número de Armstrong."""

def is_armstrong_number(number):
    """Verifica se o número fornecido é um número de Armstrong."""
    algarismos = list(str(number))
    tamanho = len(algarismos)
    soma_final = 0
    
    for digito in algarismos:
        if tamanho > 0:
            calculo = int(digito) ** tamanho
            soma_final += calculo
            
    return soma_final == number
    
# print(is_armstrong_number(number))






