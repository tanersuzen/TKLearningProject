from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=60,pady=150)

my_label = Label()
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=100, pady=100)
my_label.pack()

#button
def button_click():
    print("button clickled")
    print(my_text.get("1.0",END))

my_button = Button(text="Button", command=button_click)
my_button.config(padx=100, pady=5)
my_button.pack()

#entry
my_entry = Entry(width=20)
my_entry.pack()

#multiline, text
my_text = Text(width=30, height=10)
my_text.pack()

#scale
def scale_selected(value):
    print(value)
my_scale = Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()


window.mainloop()