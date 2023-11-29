import tkinter

#window
window = tkinter.Tk()
window.title("Python Title")
window.minsize(500,500)
window.config(bg="grey")

#label
my_label = tkinter.Label(text="This is a label",font=("Times New Roman", 35 , "italic"))
my_label.config(bg="black",fg="white")
my_label.pack()

def click_button():
    user_input = my_entry.get()
    print(user_input)

#button
my_button = tkinter.Button(text="This is a button",command=click_button)
my_button.pack()

#entry
my_entry = tkinter.Entry(width=20)
my_entry.pack()



window.mainloop()