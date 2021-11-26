def thesaurus_adv(*args):
    last_dict = {}
    for k in sorted(args, key=lambda s_n: s_n.split()[1][0]):
        my_dict = {}
        for i in sorted(list(filter(lambda x: x.split()[1][0] == k.split()[1][0], args))):
            my_dict.setdefault(i[0], list(filter(lambda x: x[0] == i[0], sorted(list(filter(lambda x: x.split()[1][0] == k.split()[1][0], args))))))
        last_dict.setdefault(k.split()[1][0], my_dict)

    return last_dict


print(f'Ваш словарь: {thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")}')
