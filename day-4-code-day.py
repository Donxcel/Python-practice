print("\t\ttreasure chest")
row_1 = ['M','M','M']
row_2 = ['M','M','M']
row_3 = ['M','M','M']
print('''
             ['M','M','M']
             ['M','M','M']
             ['M','M','M']   
                           
''')
print("\n where do you want to put ur treasure:  ")
get = input()
x_vector = int(get[0])
y_vector = int(get[1])
result = [row_1,row_2,row_3]
result[x_vector-1][y_vector-1] = 'x'
print(row_1)
print(row_2)
print(row_3)