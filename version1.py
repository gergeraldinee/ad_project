import tkinter as tk  # you can give a "short name" for the import file / 'tkinter' is a library / 'tk' as a short form
import self as self
import PIL


window = tk.Tk()  # 'tk' is the short form you chose above / (.tk) is the ending of Tkinter / Window is the variable
window.title("Weather Closet")  # Name your window anything
window.geometry("1000x600")

# adding the Label & something you can change
label = tk.Label(text="Welcome to Weather Closet!",  # this is the text inside the label
                 width=30,  # width of 10 'o' / 10 'o' ooooooooo (horizontal - width)
                 height=3,  # height of 10 'o' / same thing for height vertically
                 foreground="black",  # text color / change whatever color you want or google it
                 background="white").pack()  # background color / same as above

canvas = tk.Canvas(width=1250, height=300)
canvas.pack()

img = tk.PhotoImage(file="clothing_line.pbm")
canvas.create_image(1, 100, anchor=tk.W, image=img)



def submit():  # This is a callback function to Set whatever the User input
    print(usergender.get())
    print(variable1.get())
    print(variable2.get())
    print(variable3.get())
    print("Skirt: %d,\nShirt: %d,\nPants: %d,\nCardigan %d"
          % (var1.get(), var2.get(), var3.get(), var4.get()))
    print(response.text)


# Weather API - OK!

import requests

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {"location":"Singapore","format":"json","u":"f"}

headers = {
    'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
    'x-rapidapi-key': "ab1a89a265msh87b1c2de190624ap10b909jsn6a80b3eebdef"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# Gender - User Input - OK!

usergender = tk.StringVar(window)
gender_label = tk.Label(text="Gender", width=30,
                 height=2, foreground='black',
                  background='white')
gender_label.pack()

female = tk.Radiobutton(window, text="Female", variable=usergender,
                        value='Female', command=submit)
female.pack()
male = tk.Radiobutton(window, text="Male", variable=usergender,
                      value='Male', command=submit)
male.pack()

# Age - User Input - OK!

age_label = tk.Label(text="Age", width=30,
                     height=2, foreground='black',
                     background='white')
age_label.pack()

OPTIONS = [
"18 - 24 years old",
"25 - 34 years old",
"35 - 44 years old",
] #etc


variable1 = tk.StringVar(window)
variable1.set(OPTIONS[0])# default value

w = tk.OptionMenu(window, variable1, *OPTIONS)
w.pack()


# Country of Residence - OK!

country_label = tk.Label(text="Age", width=30,
                     height=2, foreground='black',
                     background='white')
country_label.pack()

OPTIONS = [
"Singapore",
"Malaysia",
"Indonesia",
] #etc

variable2 = tk.StringVar(window)
variable2.set(OPTIONS[0])# default value

w = tk.OptionMenu(window, variable2, *OPTIONS)
w.pack()

# Occasions - OK!

occasion_label = tk.Label(text="Age", width=30,
                     height=2, foreground='black',
                     background='white')
occasion_label.pack()

OPTIONS = [
"Office",
"Casual",
"Party",
"Sports"
] #etc

variable3 = tk.StringVar(window)
variable3.set(OPTIONS[0])# default value

w = tk.OptionMenu(window, variable3, *OPTIONS)
w.pack()

# Category - OK!

category_label = tk.Label(text="Category", width=30,
                     height=2, foreground='black',
                     background='white')
category_label.pack()

var1 = tk.IntVar()
cb1 = tk.Checkbutton(window, text="Skirt", variable=var1).pack()

var2 = tk.IntVar()
cb2 = tk.Checkbutton(window, text="Shirt", variable=var2).pack()

var3 = tk.IntVar()
cb3 = tk.Checkbutton(window, text="Pants", variable=var3).pack()

var4 = tk.IntVar()
cb4 = tk.Checkbutton(window, text="Cardigan", variable=var4).pack()


# Button - OK!

button1 = tk.Button(text="Generate", width=10, height=2,
                   command=submit).pack()

# start the window loop
tk.mainloop()
