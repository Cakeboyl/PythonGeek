def transform_string(number):
    numbers = [10,11,12,13]
    if number % 10 == 1:
        return f'{number}, процент'
    if number in numbers:
        return f'{number}, процентов'
    if 1 < number % 10 < 5:
        return f'{number}, процента'
    else:
        return f'{number}, процентов'

for n in range(1, 101):
    print(transform_string(n))