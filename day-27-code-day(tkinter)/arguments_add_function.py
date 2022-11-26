def add(*args):
    total = 0
    for n in args:
        total+=n
    return total

print(add(4,5,6,2,1,4,1))