import pandas
s = pandas.read_csv("squirrel_census.csv")
data = s['Primary_Fur_Color'].value_counts()
print(data)


#data.to_csv("squirrel_count.csv")