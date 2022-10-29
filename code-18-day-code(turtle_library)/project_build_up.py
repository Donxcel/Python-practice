# from colorgram import *
from random import *
from turtle import *
donal = Turtle()

screen = Screen()
# play = colorgram
# color_list = play.extract("hist_painting.jpg", 100)
# color_palette = []
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color  = (r,g,b)
#     color_palette.append(new_color)
# print(color_palette)
# #print('play')
donal.dot(10)

color = [(246, 240, 228), (248, 237, 243), (234, 246, 239), (235, 240, 247), (196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112), (223, 172, 184), (227, 175, 167), (103, 44, 60), (50, 56, 94), (168, 207, 185), (167, 158, 66), (60, 155, 174), (111, 122, 155), (97, 49, 44), (178, 188, 214), (152, 207, 219), (221, 219, 20), (25, 94, 68), (78, 71, 42), (18, 88, 101)]
for i in range(10):
print

    for _ in range(10):
        #donal.color(choice(color))
        donal.dot(10)
        donal.forward(10)
    donal.right(90)
    donal.backward(10)

screen.exitonclick()