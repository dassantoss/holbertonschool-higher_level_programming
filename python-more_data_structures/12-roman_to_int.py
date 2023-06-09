#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    valor = 0
    valor_anterior = 0
    total = 0

    for letra in reversed(roman_string):
        valor = roman_values[letra]

        if valor < valor_anterior:
            total -= valor
        else:
            total += valor
        valor_anterior = valor

    return (total)
