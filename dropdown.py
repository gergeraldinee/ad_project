from tkinter import *

OPTIONS = [
"18 - 24 years old",
"25 - 34 years old",
"35 - 44 years old",
] #etc

age = Tk()

variable1 = StringVar(age)
variable1.set(OPTIONS[0])# default value

w = OptionMenu(age, variable1, *OPTIONS)
w.pack()

def ok():
    print (variable1.get())

button = Button(age, text="OK", command=ok)
button.pack()

mainloop()
