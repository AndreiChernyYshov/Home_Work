mass_mass = [[], []]
mass_summa = [0, 0]

a = 1
while a < 1000:
    mass_mass[0].append(a ** 3)
    mass_mass[1].append(a ** 3 + 17)
    a += 2

t = 0
while t < len(mass_summa):
    summa_7 = 0
    i = 0
    while i < len(mass_mass[t]):
        k = list(str(mass_mass[t][i]))

        summa = 0
        b = 0
        while b < len(k):
            summa += int(k[b])
            b += 1

        if summa % 7 == 0:
            summa_7 += mass_mass[t][i]

        i += 1

    mass_summa[t] = summa_7
    t += 1

print(mass_summa)