import tkinter as tk

window = tk.Tk()

window.geometry("400x400") # creates the size of the window
window.title("GUI example") # sets title of the window


label1 = tk.Label(window,text ="Label 1")
label2 = tk.Label(window,text = "Label 2")
label3 = tk.Label(window,text="Label 3")
label4 = tk.Label(window,text="Label 4")



def add():
    label1["text"] = "hello"

add()


label1.pack(side=tk.LEFT)

label2.pack(side=tk.RIGHT)

label3.pack(side = tk.TOP)
label3.pack(side = tk.BOTTOM)


# label1.grid(row=0,column=0)
# label2.grid(row=0,column=0)
# label3.grid(row=0,column=0)
# label4.grid(row=0,column=0)


window.mainloop()   # must include this for the window to launch and show up
