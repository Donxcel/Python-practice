from tkinter import *
COLOR_1 = "#B0BDF3"
COLOR_2 = "#A9EBC1"
COLOR_3 = "#6666BC"
FONT = 'Courier'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#todo 1: creating the main window
window = Tk()
window.minsize(width=600,height=600)
window.title("My password Manager")
window.config(padx=20,bg=COLOR_1,pady=20)

#todo 2: creating the password logo
password_logo = Canvas(width=200,height=200,highlightthickness=0,bg=COLOR_1)
pic  = PhotoImage(file = "./logo.png")
password_logo.create_image(100,100,image = pic)
password_logo.place(x=175,y=100)

#3 CREATING LABELS
label_web = Label(text = "Website",bg=COLOR_1,font=(FONT,10,'bold'),)
label_web.place(x=100,y=340)
# label 2
label_username = Label(text = "Email/user_name",bg=COLOR_1,font=(FONT,10,'bold'))
label_username.place(x=100,y=380)

label_password = Label(text = "Password",bg=COLOR_1,font=(FONT,10,'bold'))
label_password.place(x=100,y=420)

#todo: CREATING THE ENTRIES
entry_1 = Entry(width=45,show='www.example.com')
entry_1.place(x= 240,y=340)

entry_2 = Entry(width=45,show="...@gmail.com")
entry_2.place(x=240,y=380)

entry_3 = Entry(width=21)
entry_3.place(x=240,y=420)

#todo: CREATING A BUTTON
#button 1
my_button = Button(text="Generate password",bg=COLOR_2)
my_button.place(x = 400,y=420)

#button 2
my_button2 = Button(text="Add",bg=COLOR_2,width=39)
my_button2.place(x=239,y=460)

window.mainloop()