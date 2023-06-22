def primecheck(number):
    for divisor in range(2,1 + int(number/2)):
        if number%divisor == 0:
            return False
    else:
        return True

from_number = int(input("Lower limit (e.g. 11): "))
to_number = int(input("Upper limit (e.g. 20): "))
print ("Prime numbers between", from_number, "and", to_number, "are:")
for num in range(1 + from_number, to_number):
    if primecheck(num) == True:
        print(num)