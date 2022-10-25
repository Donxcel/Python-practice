student_scores = {
'Randy': 81, 
'Naa': 78,
'Dinga':99,
'Daniel':74,
'yvette':62
}
student_grades={}
for key in student_scores:
    if student_scores[key] >=91:
        student_grades[key] = 'outstanding'
    elif student_scores[key] >=81 and student_scores[key]<90:
        student_grades[key] = 'Exceeds expectaton'
    elif student_scores[key] >=71 and student_scores[key]<80:
        student_grades[key] = 'acceptable'
    elif student_scores[key] <=70 :
        student_grades[key] = 'fail'
print(student_grades)
#############nesting##############
travel_list=[
{
    "country": "cameroon",
    "visited": ["buea","douala","bafoussa"],
    'number_of_times': 12
},
{
"country": "france",
    "visited": ["paris","lille","dijon"],
    'number_of_times': 8

}
]
def add_country(country,visited,number_of_times):
    new_country = {}
    new_country["country"] = country
    new_country['visited'] = visited
    new_country['number_of_times'] = number_of_times 
    travel_list.append(new_country)
add_country(country="united_States",visited=['new_jersey','new_york'],number_of_times=12)
print(travel_list)