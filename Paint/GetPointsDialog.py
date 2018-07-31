import tkinter as tk
import tkinter.colorchooser as clr
import tkinter.messagebox as msg



class GetPointsDialog():
    DEFAULT_COLOR = 'black'

    def __init__(self, master, Wid_type):

        self.topLevelWindow = tk.Toplevel(master)
        self.topLevelWindow.transient(master)
        self.topLevelWindow.grab_set()


        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.rad = 0

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.rad = 0
        # circle
        self.X1_CORD_Entry = 0
        self.Y1_CORD_Entry = 0
        self.radius_Entry = 0

        # line & rectangle
        self.X2_CORD_Entry = 0
        self.Y2_CORD_Entry = 0

        # boolean check for line,rect,circle



        self.get_color = ""
        self.color = ""

        self.Wid_type = Wid_type

        if Wid_type is "CIRCLE":

            self.topLevelWindow.title("Enter Co-Ordinate Points - Circle")
            self.topLevelWindow.attributes("-topmost", True)
            self.topLevelWindow.geometry("500x200")

            w = 500  # width for the window
            h = 200  # height for the window

            # get screen width and height
            ws = self.topLevelWindow.winfo_screenwidth()  # width of the screen
            hs = self.topLevelWindow.winfo_screenheight()  # height of the screen

            # calculate x and y coordinates for the window
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)

            # set the dimensions of the screen
            # and where it is placed
            self.topLevelWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

            x1Label = tk.Label(self.topLevelWindow, text="X1").grid(row=0)
            y1Label = tk.Label(self.topLevelWindow, text="Y1").grid(row=0, column=2)
            radiusLabel = tk.Label(self.topLevelWindow, text="Enter Radius").grid(row=1)

            self.X1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.Y1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.radius_Entry = tk.Entry(self.topLevelWindow)

            self.X1_CORD_Entry.grid(row=0, column=1)
            self.Y1_CORD_Entry.grid(row=0, column=3)
            self.radius_Entry.grid(row=1, column=1)

            self.submitButton = tk.Button(self.topLevelWindow, text="Submit", command=lambda: self.submit("CIRCLE"))
            self.submitButton.grid(row=3, column=0)

            self.colorButton = tk.Button(self.topLevelWindow, text="Color",
                                         command=self.choose_color)  # command=self.circleWindow.destroy)
            self.colorButton.grid(row=2, column=2)

            self.resetButton = tk.Button(self.topLevelWindow, text="Reset", command=self.reset)
            self.resetButton.grid(row=3, column=3)

            dc = tk.IntVar()
            self.text = ""
            self.lineChoice = ["dashed", "undashed"]
            self.daOrUda = ""


            # radio buttons for Dashed and undashed
            def getDashed():

                self.text = self.lineChoice[dc.get()]
                if self.text is "dashed":
                    self.daOrUda = "dashed"
                elif self.text is "undashed":
                    self.daOrUda = "undashed"






            dashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[0], variable=dc, value=0,command = getDashed)
            dashedRadiob.grid(row=2, column=0)



            undashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[1], variable=dc, value=1, command = getDashed)
            undashedRadiob.grid(row=2, column=1)


        elif Wid_type is "LINE":
            self.topLevelWindow.title("Enter Co-Ordinate Points - Line")
            self.topLevelWindow.attributes("-topmost", True)
            self.topLevelWindow.geometry("500x200")

            w = 500  # width for the window
            h = 200  # height for the window

            # get screen width and height
            ws = self.topLevelWindow.winfo_screenwidth()  # width of the screen
            hs = self.topLevelWindow.winfo_screenheight()  # height of the screen

            # calculate x and y coordinates for the window
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)

            # set the dimensions of the screen
            # and where it is placed
            self.topLevelWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

            x1Label = tk.Label(self.topLevelWindow, text="X1").grid(row=0, column=0)
            x2Label = tk.Label(self.topLevelWindow, text="X2").grid(row=0, column=2)
            y1Label = tk.Label(self.topLevelWindow, text="Y1").grid(row=1, column=0)
            y2Label = tk.Label(self.topLevelWindow, text="Y2").grid(row=1, column=2)

            self.X1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.Y1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.Y2_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.X2_CORD_Entry = tk.Entry(self.topLevelWindow)

            self.X1_CORD_Entry.grid(row=0, column=1)
            self.X2_CORD_Entry.grid(row=0, column=3)
            self.Y1_CORD_Entry.grid(row=1, column=1)
            self.Y2_CORD_Entry.grid(row=1, column=3)

            self.submitButton = tk.Button(self.topLevelWindow, text="Submit", command= lambda:self.submit("LINE"))
            self.submitButton.grid(row=3, column=0)

            self.colorButton = tk.Button(self.topLevelWindow, text="Color",
                                         command=self.choose_color)  # command=self.circleWindow.destroy)
            self.colorButton.grid(row=2, column=2)

            self.resetButton = tk.Button(self.topLevelWindow, text="Reset", command=self.reset)
            self.resetButton.grid(row=3, column=3)

            # radio buttons for Dashed and undashed

            dc = tk.IntVar()
            self.text = ""
            self.lineChoice = ["dashed", "undashed"]
            self.daOrUda = ""

            # radio buttons for Dashed and undashed
            def getDashed():

                self.text = self.lineChoice[dc.get()]
                if self.text is "dashed":
                    self.daOrUda = "dashed"
                elif self.text is "undashed":
                    self.daOrUda = "undashed"

            dashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[0], variable=dc, value=0,
                                          command=getDashed)
            dashedRadiob.grid(row=2, column=0)

            undashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[1], variable=dc, value=1,
                                            command=getDashed)
            undashedRadiob.grid(row=2, column=1)


        elif Wid_type is "RECT":
            self.Rect = "RECT"
            self.topLevelWindow.title("Enter Co-Ordinate Points - Rect")
            self.topLevelWindow.attributes("-topmost", True)
            self.topLevelWindow.geometry("500x200")

            w = 500  # width for the window
            h = 200  # height for the window

            # get screen width and height
            ws = self.topLevelWindow.winfo_screenwidth()  # width of the screen
            hs = self.topLevelWindow.winfo_screenheight()  # height of the screen

            # calculate x and y coordinates for the window
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)

            # set the dimensions of the screen
            # and where it is placed
            self.topLevelWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

            x1Label = tk.Label(self.topLevelWindow, text="X1").grid(row=0, column=0)
            x2Label = tk.Label(self.topLevelWindow, text="X2").grid(row=0, column=2)
            y1Label = tk.Label(self.topLevelWindow, text="Y1").grid(row=1, column=0)
            y2Label = tk.Label(self.topLevelWindow, text="Y2").grid(row=1, column=2)

            self.X1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.Y1_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.Y2_CORD_Entry = tk.Entry(self.topLevelWindow)
            self.X2_CORD_Entry = tk.Entry(self.topLevelWindow)

            self.X1_CORD_Entry.grid(row=0, column=1)
            self.X2_CORD_Entry.grid(row=0, column=3)
            self.Y1_CORD_Entry.grid(row=1, column=1)
            self.Y2_CORD_Entry.grid(row=1, column=3)

            self.submitButton = tk.Button(self.topLevelWindow, text="Submit", command= lambda :self.submit("RECT"))
            self.submitButton.grid(row=3, column=0)

            self.colorButton = tk.Button(self.topLevelWindow, text="Color",
                                         command=self.choose_color)  # command=self.circleWindow.destroy)
            self.colorButton.grid(row=2, column=2)

            self.resetButton = tk.Button(self.topLevelWindow, text="Reset", command=self.reset)
            self.resetButton.grid(row=3, column=3)

            # radio buttons for Dashed and undashed

            dc = tk.IntVar()
            self.text = ""
            self.lineChoice = ["dashed", "undashed"]
            self.daOrUda = ""

            # radio buttons for Dashed and undashed
            def getDashed():

                self.text = self.lineChoice[dc.get()]
                if self.text is "dashed":
                    self.daOrUda = "dashed"
                elif self.text is "undashed":
                    self.daOrUda = "undashed"

            dashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[0], variable=dc, value=0,
                                          command=getDashed)
            dashedRadiob.grid(row=2, column=0)

            undashedRadiob = tk.Radiobutton(self.topLevelWindow, text=self.lineChoice[1], variable=dc, value=1,
                                            command=getDashed)
            undashedRadiob.grid(row=2, column=1)

    def choose_color(self):
        # """
        # SELECT THE COLOR FROM LIST OF COLOR'S AVAILABLE AND PASS THE COLOR TO MAIN WINDOW
        # """
        self.get_color = clr.askcolor()

        self.color = self.get_color[1]

        # self.line = True

    def submit(self, Wid_type):
        # """
        # IT SHOULD GET THE INPUT FROM USER AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE,
        # ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
        # """

        if Wid_type is "CIRCLE":

            self.x1 = (str(self.X1_CORD_Entry.get()))
            self.y1 = (str(self.Y1_CORD_Entry.get()))
            self.rad = (str(self.radius_Entry.get()))


            if self.x1.isdigit() and self.y1.isdigit() and self.rad.isdigit():
                self.x1 = int(self.x1)
                self.y1 = int(self.y1)
                self.rad = int(self.rad)
                if self.x1 > 50 and self.y1 > 50:
                    self.topLevelWindow.destroy()
                else:
                    msg.showwarning("Error", "Please input an x1 and y1 value greater than 50")


            elif self.x1.isalpha() or self.y1.isalpha() or self.rad.isalpha() or self.color is "":
                msg.showwarning("Error","Please input only valid integers for x1, y1, rad and make sure to choose a color")





        elif Wid_type is "LINE":
            self.x1 = (str(self.X1_CORD_Entry.get()))
            self.x2 = (str(self.X2_CORD_Entry.get()))
            self.y1 = (str(self.Y1_CORD_Entry.get()))
            self.y2 = (str(self.Y2_CORD_Entry.get()))


            if self.x1.isdigit() and self.y1.isdigit() and self.x2.isdigit() and self.y2.isdigit():
                self.x1 = int(self.x1)
                self.y1 = int(self.y1)
                self.x2 = int(self.x2)
                self.y2 = int(self.y2)
                if self.x1 > 50 and self.y1 > 50 and self.x2 > self.x1 and self.y2 > self.y1:

                    self.topLevelWindow.destroy()
                else:
                    msg.showwarning("Error", "Please input and x1,y1 > 50 and a x2,y2 that are > x1,y1")

            elif self.x1.isalpha() or self.y1.isalpha() or self.x2.isalpha() or self.y2.isalpha() or self.color is "":
                msg.showwarning("Error", "Please input only valid integers for x1, y1, x2, y2, and choose a color!")




        elif Wid_type is "RECT":
            self.x1 = (str(self.X1_CORD_Entry.get()))
            self.x2 = (str(self.X2_CORD_Entry.get()))
            self.y1 = (str(self.Y1_CORD_Entry.get()))
            self.y2 = (str(self.Y2_CORD_Entry.get()))

            if self.x1.isdigit() and self.y1.isdigit() and self.x2.isdigit() and self.y2.isdigit():
                self.x1 = int(self.x1)
                self.y1 = int(self.y1)
                self.x2 = int(self.x2)
                self.y2 = int(self.y2)
                if self.x1 > 50 and self.y1 > 50 and self.x2 > self.x1 and self.y2 > self.y1:

                    self.topLevelWindow.destroy()
                else:
                    msg.showwarning("Error", "Please input and x1,y1 > 50 and a x2,y2 that are > x1,y1")

            elif self.x1.isalpha() or self.y1.isalpha() or self.x2.isalpha() or self.y2.isalpha() or self.color is "":
                msg.showwarning("Error", "Please input only valid integers for x1, y1, x2, y2, and choose a color!")

    def reset(self):
        if self.Wid_type is "CIRCLE":
            self.X1_CORD_Entry.delete(0, 'end')
            self.Y1_CORD_Entry.delete(0, 'end')
            self.radius_Entry.delete(0, 'end')
        elif self.Wid_type is "LINE":
            self.X1_CORD_Entry.delete(0, 'end')
            self.X2_CORD_Entry.delete(0, 'end')
            self.Y1_CORD_Entry.delete(0, 'end')
            self.Y2_CORD_Entry.delete(0, 'end')
        elif self.Wid_type is "RECT":
            self.X1_CORD_Entry.delete(0, 'end')
            self.X2_CORD_Entry.delete(0, 'end')
            self.Y1_CORD_Entry.delete(0, 'end')
            self.Y2_CORD_Entry.delete(0, 'end')

        # SHOULD RESET THE VALUES IN THE ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
        # """


