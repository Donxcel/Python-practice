import string


print("@@@This is a love simolatorto test true love@@@")
name_1 = input("Enter your name:  ").upper()
name_2 = input("Enter your mates name: ").upper()
test ="TRUE LOVE"
a1=name_1.count("T")
b1 = name_1.count("R")
c1 = name_1.count("U")
d1 = name_1.count("E")
a2 = name_2.count("T")
b2 = name_2.count("R")
c2 = name_2.count("U")
d2 = name_2.count("E")
total_1 = a1+b1+c1+d1+a2+b2+c2+d2 

a=name_1.count("L")
b = name_1.count("O")
c = name_1.count("V")
d = name_1.count("E")
e = name_2.count("L")
f = name_2.count("O")
g = name_2.count("V")
h = name_2.count("E")
total_2 = a+b+c+d+e+f+g+h
print(f"the word  'TRUE' occurs {total_1} number of times ")
print(f"\nthe word  'LOVE' occurs {total_2} number of times ")

print(f"total is {total_1}{total_2}")
z = int(str(total_1)+str(total_2))
# print(z)
if z<10 or z>90:
    print(f"your score is {z},you go together like coke and mentos")
elif z>=40 and z<=50:
     print(f"your score is {z},\nyou go alright together")
else:
     print(f"your score is {z},not meant to b with each other")

