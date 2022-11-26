import tkinter
window = tkinter.Tk()
window.title("donal's first size")
window.minsize(width=600,height=400)


mylabel = tkinter.Label(text = "I am Donxcel",font=("Arial",40,"bold"))
mylabel.pack(side="top")

window.mainloop()