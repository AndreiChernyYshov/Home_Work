def thesaurus(*args):
    my_dict = {}
    for i in sorted(args):
        my_dict.setdefault(i[0], list(filter(lambda x: x[0] == i[0], args)))

    return my_dict


print(f'Ваш словарь: {thesaurus("Иван", "Мария", "Петр", "Илья")}')
