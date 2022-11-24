#from docx import *
#TODO: Create a letter using starting_letter.docx
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_a = []
new_list = []

with open(".\Input/Names\invited_names.txt") as file:
    list_a.append(file.readlines())
with open("./Output/saved_names.txt",mode="w") as store:
    for i in list_a:
        for testing in range(8):
            new_list.append(i[testing])
            store.write(new_list[testing])
with open("./Input/Letters/starting.docx",mode="r") as main:
    reserve = main.read()
with open("./Input/Names/invited_names.txt") as invitee:
    b = invitee.readlines()
    print(b)
    for final in b:
        c = final.strip()
        damn = reserve.replace("blessing",c)
        # with open(f"./Output/ReadyToSend/{c}.docx",mode="a+") as result:
        #  result.write(damn)


