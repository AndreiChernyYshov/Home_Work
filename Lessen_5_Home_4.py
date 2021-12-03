src = [int(i) for i in (input('Give me list of numbers: ')).split()]
print([src[i] for i in range(1, len(src)) if src[i] > src[i - 1]])
