def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))

digit = 2135

while digit >= 10:
    digit = sum_digits(digit)

print (digit)