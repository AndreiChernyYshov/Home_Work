from random import randrange
from random import choice


def get_jokes(n):
    """Какой-то текст"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    qwestion = input('Хотите, чтобы слова не повторялись?(не более 5): ')
    for i in range(n):
        if qwestion == 'Да' or qwestion == 'да':
            jokes.append(f'{nouns.pop(randrange(len(nouns)))} '
                         f'{adverbs.pop(randrange(len(adverbs)))} '
                         f'{adjectives.pop(randrange(len(adjectives)))}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes


print(f'Ваши шутки: {get_jokes(int(input("Сколько шуток вы хотите увидеть: ")))}')
print(help(get_jokes))
