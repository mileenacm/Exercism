def steps(number):
    k = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed") 
    while number != 1: 
        if number % 2 == 0:
            number = number//2 
            print(number)
        else:
            number = (number*3) + 1
            print(number)
        k += 1 
    return k