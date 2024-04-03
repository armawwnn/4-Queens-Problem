def decimal_to_base_4(number):
    base_4_digits = []
    while number > 0:
        digit = number % 4
        base_4_digits.insert(0, digit)
        number //= 4

    while len(base_4_digits) < 4:
        base_4_digits.insert(0, 0)

    return base_4_digits


def base_4_to_decimal(arr):
    decimal_number = 0
    power = len(arr) - 1
    for digit in arr:
        decimal_number += digit * (4 ** power)
        power -= 1
    return decimal_number


def successor(arr):
    next_state = []
    decimal_number = base_4_to_decimal(arr)

    inc = decimal_number +1
    if inc == 256:
        inc = 0
    dec = decimal_number -1 
    if dec == -1:
        dec = 255
    next_state.append(decimal_to_base_4(inc))
    next_state.append(decimal_to_base_4(dec))
    return next_state


print(successor([1,0,0,0]))


