import tkinter as tk

wind = tk.Tk()

top_frame = tk.Frame(wind)
down_frame = tk.Frame(wind)

red_btn = tk.Button(top_frame, text="red", highlightbackground='red', command=lambda: update_canvas("red"))
blue_btn = tk.Button(top_frame, text="blue", highlightbackground='blue', command = lambda: update_canvas("blue"))

red_btn.pack()
blue_btn.pack()

top_frame.pack(side=tk.TOP)
down_frame.pack()


down_canvas = tk.Canvas(down_frame, width=600, height = 600, bg = "grey")
down_canvas.pack()


wind.geometry("700x700")


def update_canvas(color):
    down_canvas.config(bg=color)


wind.mainloop()
