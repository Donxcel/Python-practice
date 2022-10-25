# this is a dictionary
dictionary= {
    'donal':5,
    'randy':8
}
print(dictionary)
num = 0
for names in dictionary:
    if num > dictionary[names]:
        num = num
    else:
        num = dictionary[names]
for response in dictionary:
    if dictionary[response] == num:
        print(f"{response} has the greatest score which is {num}")