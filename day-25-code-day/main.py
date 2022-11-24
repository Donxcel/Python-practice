import pandas

storing_students ={
    "name":["ange","Mary","Solange"],
    "score":[50,70,65]
}
print(storing_students.values())
new_data = pandas.DataFrame(storing_students)
#print(new_data)
new_data.tot