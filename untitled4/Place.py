import tkinter
wind = tkinter.Tk()

lbl1 = tkinter.Label(wind)



lbl2 = tkinter.Label(wind, text = "Please enter your value here")

wind.geometry("400x400")
lbl2.grid(row = 4, column =4)
lbl1.grid(row = 10,column = 10)

entry_box = tkinter.Entry(wind)

def add():
    userentry = entry_box.get()
    lbl1["text"] = userentry
    # print(userentry)
    
entry_box.grid(row=0,column=1)

wind.title("First Window")


button = tkinter.Button(wind, text = "Click Me",command = add)

button.grid(row=10,column=10)




wind.mainloop()