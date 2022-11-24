from pandas import *
tester = read_csv("./us-states-game-start/50_states.csv")
data = tester.y.max() == tester.y
print(data)
