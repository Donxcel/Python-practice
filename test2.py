def prime_number(number):
    space = number
    test = 0
    for i in range(1,number+1):
        if number%i == 0:
            test+=1
    #print(test)
    if test == 2:
        print("the number is prime")
    else:
        print("this is not a prime number")
    
get = eval(input("Enter a number "))
prime_number(get)
