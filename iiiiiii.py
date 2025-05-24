def pypypy(max_power):
    for n in range(max_power):
        yield 3 ** n

for power in pypypy(5):
    print(power)