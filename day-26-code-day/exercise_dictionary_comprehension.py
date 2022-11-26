#TODO: CONVERTING A WEATHER DICTIONARY IN CELSUIS
#TODO: TO A FARHENHEIT DICTIONARY
#
# weather = {
#     "Monday":12,
#     "Tuesday":24,
#     "Wednesday":25,
#     "Thursday":25,
#     "Friday":25,
#     "Saturday":25,
#     "Sunday": 28,
# }
# # f =(temp_c *9/5) +30
# weather_f = {day:(temp * 9/5)+30 for (day,temp) in weather.items() }
# print(weather_f)


#TODO: CONVERTING A SENTENCE INTO WORDS AND COUNTING THE CORRESPONDING NUMBER OF WORDS
#
# sentence = "Donal I am seeing a bright future in you"
# s = sentence.split()
# new_l = list(s)
# f_dict = {word:len(word) for word in new_l}
# print(f_dict)

#TODO: ITERATING OVER PANDAS DATAFRAME
student_dict = {
    "student":['mary','john','paul'],
    "score":[25,25,40]
}
import pandas
new_panda_sheet = pandas.DataFrame(student_dict)

#main inbuilt function
for (index,row) in new_panda_sheet.iterrows():
    if row.student == "mary":
        print(row)