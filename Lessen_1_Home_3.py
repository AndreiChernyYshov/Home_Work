number = input("Введите число от 1 до 100:")
main = " процент"

if 9 < int(number) < 20:
    main += "ов"
else:
    mass_number = list(number)
    last_number = int(mass_number[-1])
    if 4 < last_number < 10 or last_number == 0:
        main += "ов"
    if 1 < last_number < 5:
        main += "а"

print(number + main)