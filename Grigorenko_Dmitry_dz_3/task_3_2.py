def num_translate_adv(value: str) -> str:
    dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if value in dictionary:
        str_out = dictionary[value]
    elif value.lower() in dictionary:
        str_out = dictionary[value.lower()].capitalize()
    else:
        str_out = None
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print(num_translate_adv("twelve"))