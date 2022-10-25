            #program to sum and subrtract from 1 to 2000
from re import X


print("\t\t @@@@@@@@@@@This is an exquisite program just for u  @@@@@@@@@@@@@@@ \n")
total=0
x=100
y=10
x,y = y,x
print(f"{x}{y}")
for i in range(1,2001):
    b= i
    if i%2== 0:
        total = total -i
    else:
         total = total +i

print("Expected outcome ")
print("The result is ",total)