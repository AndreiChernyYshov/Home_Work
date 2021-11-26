def num_translate_adv(text):
    dictionary_of_number = dict([('one', 'один'), ('two', 'два'), ('three', 'три'), ('four', 'четыре'),
                                 ('five', 'пять'), ('six', 'шесть'), ('seven', 'семь'), ('eight', 'восемь'),
                                 ('nine', 'девять'), ('ten', 'десять')])
    if text.istitle():
        return dictionary_of_number.get(text.lower()).title()
    else:
        return dictionary_of_number.get(text)


print(f'Your Russian number: {num_translate_adv(input("Give me number: "))}')
