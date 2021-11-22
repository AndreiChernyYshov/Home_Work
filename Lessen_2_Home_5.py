import random
my_list = []

i = 0
while i < 20:
    a = random.uniform(0, 1000)
    my_list.append(round(a, 2))
    i += 1

print(f'id значения: {str(id(my_list[3]))}\nсамо значение: {str(my_list[3])}\nпозиция значения: 3')
id_number = id(my_list[3])
my_list = (sorted(my_list))

for k, meaning in enumerate(my_list):
    if id(meaning) == id_number:
        print(f'id значения: {str(id(meaning))}\nсамо значение: {str(my_list[k])}\nпозиция значения: {str(k)}')

    meaning = str(meaning)
    meaning = meaning.split(".")
    if len(meaning[1]) < 2:
        meaning[1] = meaning[1].ljust(2, '0')

    my_list[k] = meaning[0] + " руб " + meaning[1] + " коп"

reverse_list = reversed(my_list)

print(", ".join(my_list))
print(", ".join(reverse_list))
print("5 самых дорогих товаров: " + ", ".join(my_list[-5:]))