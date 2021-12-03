src = [int(i) for i in (input('Give me list of numbers: ')).split()]
print([i for i in src if src.count(i) == 1])
