duration = int(input("Введи время в секундах:"))
mass = []
mass_res = [" сек. ", " мин. ", " час.  ", " сут. "]
result = str()
t = 60
a = 0

i = len(mass_res)
while len(mass) < i:
    if a >= 2:
        t = 24
    if duration / t < 1:
        i = 0
        mass.append(duration % t)
    else:
        a += 1
        mass.append(duration % t)
        duration = duration // t

b = 0
while b < len(mass):
    k = len(mass) - 1 - b
    result += str(mass[k]) + mass_res[k]
    b += 1

print(result)
