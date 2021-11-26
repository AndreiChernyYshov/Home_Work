def num_translate(text):
    dictionary_of_number = dict([('one', 'один'), ('two', 'два'), ('three', 'три'), ('four', 'четыре'),
                                 ('five', 'пять'), ('six', 'шесть'), ('seven', 'семь'), ('eight', 'восемь'),
                                 ('nine', 'девять'), ('ten', 'десять')])
    return dictionary_of_number.get(text)


print(f'Your Russian number: {num_translate(input("Give me number: "))}')
