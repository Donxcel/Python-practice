# number = [1,2,3]
#
# new_list = [i+1 for i in number]
# print(new_list)
import math
# new_numbers = [i for i in range(1,5) if i%2 == 0]
# print(new_numbers)
# # exx 1
# number = [1,2,3,4,6,8,9,11,15]
# squared_numbers = [num for num in number if num**2 in number  ]
# print(squared_numbers)

# number = [1,1,2,3,5,8,13,21,34,55]
# even_numbers = [test for test in number if test%2 == 0 ]
# print(even_numbers)

# exercise 3:
#TODO: CHECKING VALUES OF 2 TEXT FILES AND GRASP THE COMMON VALUES
new_l = []
with open("./list1") as file:
    new_l = [ int(i) for i in file ]
print(new_l)
set1 = set(new_l)
with open("./list2") as file2:
    new_s =[int(n) for n in file2 ]
print(new_s)
set2 = set(new_s)
s = [ test for test in set1 if test in set2]
print(s)

