import tkinter as tk
import GetPointsDialog as GPD

import math


class Painter():
    def __init__(self):
        # """
        # SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.
        #
        # CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM
        # """
        self.root = tk.Tk()
        self.root.title("Python Paint")
        self.root.geometry("800x800")
        self.menuBar = tk.Menu(self.root)
        self.frm1 = tk.Frame(self.root)

        self.X1_CORD = 0
        self.Y1_CORD = 0
        self.X2_CORD = 0
        self.Y2_CORD = 0
        self.radius = 0

        self.x1Casted = 0
        self.y1Casted = 0
        self.radCasted = 0

        self.x1 = 0
        self.y1 = 0
        self.rad = 0

        self.paint_Menu = tk.Menu()
        self.penButton = tk.Button(self.root)
        self.lineButton = tk.Button(self.root)
        self.circleButton = tk.Button(self.root)

        self.filemenu = ""
        self.helpmenu = ""
        self.optionsmenu = ""

        self.circle = False
        self.line = False
        self.rect = False



        # Toplevel windows that pop up above root
        self.aboutWindow = ""
        self.exitWindow = ""
        self.circleWindow = ""
        self.rectWindow = ""
        self.lineWindow = ""

        self.cnvs = tk.Canvas()

        # self.circleWindow = tk.TopLevel(self)

        # self.aboutWindow = tk.TopLevel(self)

        self.init_widgets()
        # self.Create_Circle()
        self.root.mainloop()

    def init_widgets(self):

        # """
        # SHOULD DO THE BELOW LISTED OPERATIONS.
        # """
        # Adding Menu Bar TO BASE WINDOW

        # CREATE ALL MENUBAR'S

        # CREATE ALL SUB MENUS FOR MAIN MENU AND ACTIVATING DYNAMICALLY.

        # ADD BUTTONS TO THE MAIN WINDOW AND ACTIVATE THEM DYNAMICALLY
        def doNothing():
            print(" ")

        def clearAll():
            self.cnvs.delete("all")

        self.filemenu = tk.Menu(self.menuBar)
        self.optionsmenu = tk.Menu(self.menuBar)
        self.helpmenu = tk.Menu(self.menuBar)

        # FILE dropdown menu
        self.filemenu.add_command(label="New", command=self.create_New_Canvas)
        self.filemenu.add_command(label="Save", command=self.save_canvas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit)
        self.menuBar.add_cascade(label="File", menu=self.filemenu)

        # OPTIONS dropdown menu
        self.optionsmenu.add_command(label="Circle", command= lambda: self.Get_Cordinate_Points("CIRCLE"))
        self.optionsmenu.add_command(label="Line", command=lambda: self.Get_Cordinate_Points("LINE"))
        self.optionsmenu.add_command(label="Rectangle", command=lambda: self.Get_Cordinate_Points("RECT"))
        self.optionsmenu.add_separator()
        self.optionsmenu.add_command(label="Clear All", command=clearAll)
        self.menuBar.add_cascade(label="Options", menu=self.optionsmenu, state="disabled")

        # HELP dropdown menu
        self.helpmenu.add_command(label="Help", command=self.show_help_about)
        self.menuBar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menuBar)

        # Buttons on the top left of the screen
        self.penButton = tk.Button(self.root, text="Pen", command=lambda:self.activate_button("PEN"), state="disabled")
        self.lineButton = tk.Button(self.root, text="Line", command=lambda:self.activate_button("LINE"), state="disabled")
        self.circleButton = tk.Button(self.root, text="Circle", command=lambda:self.activate_button("CIRCLE"), state="disabled")

        # Pack Buttons
        self.penButton.pack(side='left', anchor="n")
        self.lineButton.pack(side='left', anchor="n")
        self.circleButton.pack(side="left", anchor="n")

    def create_New_Canvas(self):

        # """
        # CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME
        # """
        self.frm1.pack(side=tk.BOTTOM, anchor=tk.S)
        self.cnvs = tk.Canvas(self.frm1, width=700, height=700, bg='grey')

        self.cnvs.pack()

        enable = True
        self.enable_menu(enable)

    def activate_button(self, Btn_Typ):
        # """
        # HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
        # """
        self.old_x = None

        self.old_y = None
        self.old_w = None

        if Btn_Typ == "PEN":

            self.cnvs.bind('<B1-Motion>', self.Brush)
            self.cnvs.bind("<ButtonRelease-1>", self.button_released)
        if Btn_Typ == "LINE":
            self.cnvs.bind("<ButtonPress-1>", self.line_click)
            self.cnvs.bind("<ButtonPress-2>", self.button_2_clicked)
            pass
        if Btn_Typ == "CIRCLE":

            self.cnvs.bind("<ButtonPress-1>", self.Circle_Click)
            self.cnvs.bind("<ButtonPress-2>",self.button_2_clicked)
            pass



        # elif Btn_Typ == "LINE":
        #     self.cnvs.bind('<B1-Motion>', self.line_click)
        #     self.cnvs.bind('<ButtonRelease-1>', self.button_released)
        #
        # elif Btn_Typ =="CIRCLE":
        #     self.cnvs.bind('<B1-Motion>', self.line_click)
        #     self.cnvs.bind('<ButtonRelease-1>', self.button_released)


    def button_2_clicked(self,event):
        self.cnvs.delete("all")
        self.old_x = None
        self.old_y = None

    def button_released(self, event):
        # """
        # WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
        # """
        self.old_y = None
        self.old_x = None

        pass

    def Brush(self, event):
        # """
        # CAN USE THE BELOW GIVEN CODE FOR BRUSH OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.
        # """

        if self.old_x and self.old_y:
            self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y, width=5,
                                  capstyle=tk.BUTT, fill='black', splinesteps=50)

        self.old_x = event.x
        self.old_y = event.y



    def redraw(self):

        # """ # SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES FOR OVAL(CIRCLE), LINE
        # """

        pass


    def line_click(self, event):
        # """
        # SHOULD ABLE TO HANDLE THE MOUSE CLICK EVENT AND PASS CO-ORDINATES TO THE CREATE_LINE EVENT FOR THE CANVASE AND PASS
        #  THE FILL COLOR AND SET WIDTH PROPERTIES AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
        # """
        if self.old_x and self.old_y:
            self.cnvs.create_line(self.old_x, self.old_y,event.x, event.y,  width=5,
                                  capstyle=tk.BUTT, fill='black', splinesteps=50)

        self.old_x = event.x
        self.old_y = event.y





        pass

    def Circle_Click(self, event):
        # """
        # SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
        # """
        if self.old_x and self.old_y:
            self.cnvs.create_oval(self.old_x, self.old_y, event.x+10, event.y+10,
                                   fill='black')

        self.old_x = event.x
        self.old_y = event.y

        pass

    def enable_menu(self, enable):
        # """
        # THIS METHOD SHOULD BE ABLE TO HANDLE THE MENUBAR STATUS AND CONFIGURE TO NORMAL STATUS WHEN NEW BUTTON IS SELECTED
        # """


        if enable == True:
            self.penButton.config(state="normal")
            self.lineButton.config(state="normal")
            self.circleButton.config(state="normal")
            self.menuBar.entryconfigure("Options", state=tk.NORMAL)




            # self.paint_Menu.entryconfigure(2, state="normal")
        else:
            enabled = False

            self.paint_Menu.entryconfigure(2, state=tk.DISABLED)

    # .................
    # .....................
    # .........................


    def Get_Cordinate_Points(self, wid_typ):


        call = GPD.GetPointsDialog(self.root,wid_typ)
        self.root.wait_window(call.topLevelWindow)

        if wid_typ is "CIRCLE":
            self.Create_Circle(call.x1,call.y1,call.rad,call.color, call.daOrUda)
        if wid_typ is "LINE":
            self.Create_Line(call.x1,call.y1,call.x2,call.y2,call.color, call.daOrUda)

        if wid_typ is "RECT":
            self.Create_Rect(call.x1, call.y1,call.x2,call.y2,call.color, call.daOrUda)

        #if wid_typ is "CIRCLE":
            #self.create_Circle(self, call.x1, call.y1, call.rad, )




        # """
        # CALL THE TOPLEVEL WINDOW FROM THIS METHOD, SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE
        # PROPERTIES AND DECIDE TO CALL THE Create_Circle OR Create_OR Create_Rect Line METHODS
        #
        # """

    def Create_Circle(self, x1, y1, rad, clr,daorUnda):

        # """
        # CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        # """
        if daorUnda is "dashed":
            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad, y1 + rad, fill=clr, dash = (2,4))
        elif daorUnda is "undashed":
            self.cnvs.create_oval(x1 - rad, y1 - rad, x1 + rad, y1 + rad, fill=clr, dash = ())

    def Create_Line(self, x1, y1, x2, y2, Colo, daorUnda):
        # """
        # CREATE LINE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT

        if daorUnda is "dashed":
            self.cnvs.create_line(x1, y1, x2, y2, fill=Colo, dash = (2,4))
        elif daorUnda is "undashed":
            self.cnvs.create_line(x1, y1, x2, y2, fill=Colo, dash = ())

        # """

    def Create_Rect(self, x1, y1, x2, y2, Colo, daorUnda):
        # """
        # CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
        # """
        if daorUnda is "dashed":
            self.cnvs.create_rectangle(x1, y1, x2, y2, fill=Colo, dash = (2,4))
        elif daorUnda is "undashed":
            self.cnvs.create_rectangle(x1, y1, x2, y2, fill=Colo, dash = ())

    def clear_canvas(self):
        # '''
        # triggered when the menu command 'Clear' is clicked
        # delete everything from the canvas and set the coefficients to 0's
        # '''
        self.cnvs.delete("all")

    pass

    def save_canvas(self):
        # '''
        # triggered when the menu command 'Save plot as .PS' is clicked
        # save the graph as '{your_student_id_number}.ps'
        # '''
        self.cnvs.postscript(file="1015211.ps")

    pass

    def show_help_about(self):
        # '''
        # triggered when the menu command 'About' is clicked
        # Show an information dialog displaying your name on one line and id number on the second
        # '''
        self.aboutWindow = tk.Toplevel()
        self.aboutWindow.attributes("-topmost", True)
        self.aboutWindow.geometry("300x300")
        self.aboutWindow.title("About PY Paint")

        w = 300  # width for the window
        h = 300  # height for the window

        # get screen width and height
        ws = self.aboutWindow.winfo_screenwidth()  # width of the screen
        hs = self.aboutWindow.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.aboutWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        message = tk.Message(self.aboutWindow, text="Created by: Alex Guntermann \n ID: 0999934")
        message.pack()

        button = tk.Button(self.aboutWindow, text="Ok", command=self.aboutWindow.destroy)
        button.pack()

    def exit(self):
        # '''
        # triggered when the menu command 'Exit' is clicked
        # Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        # '''
        self.exitWindow = tk.Toplevel()
        self.exitWindow.attributes("-topmost", True)
        self.exitWindow.geometry("200x100")
        self.exitWindow.title("Exit")

        w = 200  # width for the window
        h = 100  # height for the window

        # get screen width and height
        ws = self.exitWindow.winfo_screenwidth()  # width of the screen
        hs = self.exitWindow.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.exitWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        message = tk.Message(self.exitWindow, text="Are you sure you want to quit?")
        message.pack()

        button = tk.Button(self.exitWindow, text="Yes", command=self.root.destroy)
        button.pack()


p = Painter()
