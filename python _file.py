from os import system

# creating a simple gcd calculator
list_a = []
list_b = []


def gcd(a, b):
    global list_a, list_b

    for i in range(1, a + 1):
        if a % i == 0:
            list_a.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            list_b.append(i)
    print('factors of ', a, 'are ', list_a)
    print('factors of ', b, 'are ', list_b)
    total = 0
    i = 0
    for test in list_b:
        for i in list_a:
            if test == i:
                total = test
    list_a = []
    list_b = []
    print('the gcd of both elements are ', total)


def main():
    int_a = eval(input("Enter the first value"))
    int_b = eval(input("Enter the second value"))
    gcd(a=int_a, b=int_b)
    system('cls')
    main()


if __name__ == '__main__':
    main()
