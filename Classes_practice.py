from string import punctuation
class PLay:
    def __init__(self,a) -> None:
        self.a =a

    def fact(self):
        if self. a == 0 or self.a == 1:
            self.a = 1
            return self.a
        else:
            total = 1
            for i in range(1,self.a+1):
                total *= i
            
            return total

    def prime_number(self):
        test = 0
        for number in range(1,self.a+1):
            if self.a % number == 0:
                    test+=1
        if test == 2:
                print(f'{self.a} is a prime number')
        else:
                print(f'{self.a} is not a prime number')
get = eval(input("enter an integer:  "))
test = PLay(get)
print (f'the answer is  {test.fact()}')
test.prime_number()