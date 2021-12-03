tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klas = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

my_dict = [(i, k) for i, k in zip(tutors, klas)]
my_dict += [(tutors[i], 'None') for i in range(len(klas), len(tutors)) if len(tutors) > len(klas)]
print(my_dict)
