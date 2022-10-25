# # reading to a file
# s = open('opening_a_file.txt').read()
# print(s)
# # writing to a file
# test  = open('example','w')
# print('''God is indeed awesome
#         always stay humble in life and never depart from your ambitions
#
#
#
#
#
#
# ''', file=test)
# test.close()
#
# # reading degree temperatures from a list and converting them
# # to farheiheit and storing them in another file

file_1 = open('opening_a_file.txt','w')
ftemp = [line.strip() for line in open('example')]
get = 0
for temp in ftemp:
    if temp != '\n':
        get = int(temp)
    print(type(temp))
    print(get * 9 / 5 + 32, file=file_1)

file_1.close()

