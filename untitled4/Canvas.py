import tkinter as tk

wind = tk.Tk()


canvs = tk.Canvas(wind, width= 700, height = 600, bg='grey')

wind.geometry("800x800")

canvs.pack(side=tk.BOTTOM)

wind.mainloop()