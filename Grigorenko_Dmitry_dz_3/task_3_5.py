from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    counter = 0
    list_out = []
    while counter < count:
        some_joke = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}']
        list_out += some_joke
        counter += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))