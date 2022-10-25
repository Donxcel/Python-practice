print("derivative calculator:")
derivative = input("Enter the derivative:  ")
a = derivative[derivative.index('^')+1:]
sum_1 = int(a)
b = derivative[:derivative.index('x')]
sum_2 = int(b)
if sum_1 == 0:
    print(f" the  answer to {derivative} is = 1")
elif sum_1 == 1:
    sum_2 = sum_2 * sum_1
    sum_1-=1
    print(f" the  answer to {derivative} is = {sum_2}")
else:
    sum_2 = sum_2 * sum_1
    sum_1-=1
    print(f" the  answer to {derivative} is = {sum_2}x^{sum_1}")
    game = "quite easily done"
    print(game.replace("",""))
if sum_2 == 0:
        print(f" the  answer to {derivative} is = 0")
