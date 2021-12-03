def odd_nums(n):
    for k in range(1, n + 1, 2):
        yield k


number = int(input("Введите число: "))
odd_to_15 = odd_nums(number)
for i in range(1, number + 1, 2):
    print(next(odd_to_15))
