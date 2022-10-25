
print("####this is a tip calculator####")
total= eval(input("Enter the total amount : "))
print("total amount is:  ",total," $")
print("The number of people:  ")
people = eval(input(""))
print("What percentage tip would you like to give, 10% ,12%,15%")
percentage = eval(input())

amount = ((100-percentage)*total)/100
result = amount/people
print("the amswer is:  ",round(result,2))
#   Today's gone be a great day
print(type(result))