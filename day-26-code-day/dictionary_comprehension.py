    #learning dictionary comprehension
# dict1 = {
#     {"name":"legima Donal",
#     "age":19,
#     "gender":"male",
#     "height":1.89},
# {"name":"Mbeufet  Dore",
#     "age":20,
#     "gender":"female",
#     "height":1.20},
# }
#
# new_dict = { }
import random
list_l = ['alex',"beth",'caroline',"dave",'eleanor','freddie']
new_scores = {student:random.randint(1,100) for student in list_l}
print(new_scores)
for i in new_scores.keys():
    print(i)
passed_students = {name:score for (name,score) in new_scores.items() if score >=50}
print(passed_students)

