import tkinter as tk  # you can give a "short name" for the import file / 'tkinter' is a library / 'tk' as a short form

window = tk.Tk()    # 'tk' is the short form you chose above / (.tk) is the ending of Tkinter / Window is the variable
window.title("Weather Closet")     # Name your window anything
window.geometry("1000x600")

# adding the Label & something you can change
label = tk.Label(text="Welcome to Weather Closet!",    # this is the text inside the label
                 width=30,  # width of 10 'o' / 10 'o' ooooooooo (horizontal - width)
                 height=3,  # height of 10 'o' / same thing for height vertically
                 foreground="black",  # text color / change whatever color you want or google it
                 background="white")    # background color / same as above

label.pack()

#label2 = tk.Label(text="Goodbye World", width=100, height=50, foreground="black", backgroun='yellow')
# put the label into the window
#label2.pack()

canvas = tk.Canvas (width=1250, height=500)
canvas.pack()

img = tk.PhotoImage(file="clothing_line.pbm")
canvas.create_image(5, 700, anchor=tk.SW, image=img)

label2 = tk.Label(text="What's your name?", width=30, height=2, foreground='black', background='white')
label2.pack()
entry1 = tk.Entry (width=30).pack()

label3 = tk.Label(text="Gender", width=30, height=2, foreground='black', background='white')
label3.pack()
button1 = tk.Radiobutton(text="Female",  variable=1, value=1).pack()
button2 = tk.Radiobutton(text="Male", variable=2, value=2).pack()

label4 = tk.Label(text="Age", width=30, height=2, foreground='black', background='white').pack()
entry1 = tk.Entry (width=30).pack()

sv = tk.StringVar() # Create a Variable to track changes
label = tk.Label(text='Hello', textvariable=sv, foreground="black") # Create a Label
entry = tk.Entry(width=30) # Create an Entry for the User input
label.pack()
entry.pack()

def callback():  # This is a Callback to Set whatever the User input
    sv.set(entry.get()) #Then Set it inside the 'sv' variable
    print(sv)

button = tk.Button(text="Generate", width=10, height=2, command=callback)
button.pack()


# start the window loop
tk.mainloop()