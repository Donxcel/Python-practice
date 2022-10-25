import random
import string
computer_guess = ['rock','paper','scissor']
print('''@@@@@@@@this is a game of rock paper and scissor@@@@@@@@@@@@
                 |        TIME TO RUMBLE                |
                 |    lets go  hommie                   |  

''')
a=0
b=0
for i in range(5,0,-1):
    print(f"\n{i} gamesleft to play good luck: \n")
    get = input("'Rock','paper','scissor'; input your choice:   ").lower()
    test = random.choice(computer_guess)
    if get == 'rock' and test == 'rock':
        print(test,"\n")
        print("Its a draw ")
    elif get =='rock' and test == 'paper':
        print(test,"\n")

        print("The computer won")
        b+=1
    elif get == 'rock' and test == 'scissor':
        print(test,"\n")

        print("You won")
        a+=1
    elif get == 'paper' and test == 'rock':
        print(test,"\n")

        print("You won ")
        a+=1
    elif get =='paper' and test == 'paper':
        print(test,"\n")
        print("Its a draw")
        
    elif get == 'paper' and test == 'scissor':
        print(test,"\n")
        print(" The computer won")
        b+=1
    elif get == 'scissor' and test == 'rock':
        print(test,"\n")

        print(" The computer won")
        b+=1
    elif get =='scissor' and test == 'paper':
        print(test,"\n")

        print("You won ")
        a+=1
        
    elif get == 'scissor' and test == 'scissor':
        print(test,"\n")

        print("Its a draw")
    
print("End of the game  ")
if a>b:
    print("Congrats you won the unbeaten computer")
elif a<b:
    print("'sad song' sorry you lost ")
else:
    print("its a miserable draw")
