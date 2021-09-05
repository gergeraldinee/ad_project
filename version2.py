import tkinter as tk  # you can give a "short name" for the import file / 'tkinter' is a library / 'tk' as a short form

import requests #for weather information

#url = "https://community-open-weather-map.p.rapidapi.com/find"

#querystring = {"q":"Singapore","cnt":"1","mode":"null","lon":"0","type":"link, accurate","lat":"0","units":" metric"}

#headers = {
    #'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    #'x-rapidapi-key': "3877391548mshb52c2fa22f643a1p1ed7a5jsn6216001c854e"
    }

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

def submit(): #to collect data when user enters data
    username = entry.get() #gets entry text
    print(username)
    username2 = entry2.get()  # gets entry text
    print(username2)

window = tk.Tk()
window.title("Weather Closet")  # Name your window anything
window.geometry("800x400")

toplabel = tk.Label(text="Welcome to Weather Closet!",  # this is the text inside the label
                 width=100,  # width of 10 'o' / 10 'o' ooooooooo (horizontal - width)
                 height=3,  # height of 10 'o' / same thing for height vertically
                 foreground="black",  # text color / change whatever color you want or google it
                 background="white").pack()  # background color / same as above


canvas = tk.Canvas(width=800, height=400)
canvas.pack()

name = tk.Label(text="What's your name?", width=30, height=2, foreground='black', background='white')
name.pack()

entry = tk.Entry()
entry.config(font=('Times New Romans',12)) #change font
entry.config(bg='white') #background
entry.config(fg='black') #foreground
entry.config(width=20) #width displayed in characters
#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character
entry.pack()

gender = tk.Label(text="Gender", width=30, height=2, foreground='black', background='white')
gender.pack()
Female = tk.Radiobutton(text="Female", variable=1, value=1).pack()
Male = tk.Radiobutton(text="Male", variable=2, value=2).pack()


age = tk.Label(text="Age", width=30, height=2, foreground='black', background='white').pack()

entry2 = tk.Entry()
entry2.config(font=('Times New Romans',12)) #change font
entry2.config(bg='white') #background
entry2.config(fg='black') #foreground
entry2.config(width=20) #width displayed in characters
#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character
entry2.pack()


submit = tk.Button(window,text="submit",command=submit)
submit.pack()


window.mainloop()