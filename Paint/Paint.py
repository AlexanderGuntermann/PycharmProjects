import tkinter as tk
import tkinter.messagebox as msg
import tkinter.colorchooser as clr


class GetPointsDialog():
    DEFAULT_COLOR = 'black'

    def __init__(self, master, Wid_type):
        """
        THIS METHOD SHOULD CONSTRUCT THE TOPLEVEL WINDOW AND INITIATLIZE THE MAIN LOGIC FOR TAKING INPUT FROM USER FOR THE CORDINATES OF CIRCLE, RETANGLE AND LINE
        """

    pass

    def choose_color(self):
        """
        SELECT THE COLOR FROM LIST OF COLOR'S AVAILABLE AND PASS THE COLOR TO MAIN WINDOW
        """
        self.get_color = clr.askcolor()

    self.color = self.get_color[1]
    pass


def submit(self):
    """
    IT SHOULD GET THE INPUT FROM USER AND SHOULD CHECK ALL THE CONDITIONS GIVEN FROM USER AND VALIDATE, ONCE VALUES ARE GOOD SEND VALUES TO MAIN CLASS ELSE RESET THE VALUES.
    """


pass


def reset(self):
    """
    SHOULD RESET THE VALUES IN THE ENTRY BOXES IF THERE ARE ANY ALPHANUMERIC ERRORS
    """


pass


class Painter():
    def __init__(self):
        """
        SHOULD INITIALISE ALL THE ROOT ATTRIBUTES FOR BASE WINDOW.

        CAN ADD ANY NUMBER OF ATTRIBUTES REQUIRED FOR THE PROGRAM
        """

    self.root = tk.Tk()
    self.root.title("Python Paint")
    self.root.geometry("800x800")
    self.paint_Menu = tk.Menu(self.root)
    self.root.mainloop()


def init_widgets(self):
    """
    SHOULD DO THE BELOW LISTED OPERATIONS.
    """
    # Adding Menu Bar TO BASE WINDOW

    # CREATE ALL MENUBAR'S

    # CREATE ALL SUB MENUS FOR MAIN MENU AND ACTIVATING DYNAMICALLY.

    # ADD BUTTONS TO THE MAIN WINDOW AND ACTIVATE THEM DYNAMICALLY

    ###########################################

    ##
    pass


def create_New_Canvas(self):
    """
    CREATE A NEW CANVAS OF SIZE 600x600 TO THE MAIN FRAME
    """
    self.frm1 = tk.Frame(self.root)


self.frm1.pack(side=tk.BOTTOM, anchor=tk.S)
self.cnvs = tk.Canvas(self.frm1, width=600, height=600, bg='white')
self.cnvs.pack()
self.enable_menu()


def activate_button(self, Btn_Typ):
    """
    HANDLE THE BUTTONS ADDED ON THE FRAME FOR FREE PAINT BUTTONS
    """
    self.old_x = None


self.old_y = None

if Btn_Typ == "LINE":
    self.cnvs.bind('<B1-Motion>', self.line_click)
    self.cnvs.bind('<ButtonRelease-1>', self.button_released)
    elif:
    pass
else:
    pass
pass


def button_released(self, event):
    """
    WHEN THE MOUSE BUTTON IS RELEASED SHOULD RESET THE CO-ORDINATES OF THE PREVIOUS BINDED VALUES.
    """
    pass


def Brush(self, event):
    """
    CAN USE THE BELOW GIVEN CODE FOR BRUSH OR CAN MODIFY ACCORDING TO YOUR INITIASED ATTRIBUTES.
    """
    if self.old_x and self.old_y:


self.cnvs.create_line(self.old_x, self.old_y, event.x, event.y, width=2,
                      capstyle=tk.BUTT, fill='black', splinesteps=50)
self.old_x = event.x
self.old_y = event.y
pass


def redraw(self):
    """
    SHOULD ABLE TO SAVE ALL THE PREVIOUS CO-ORDINATE VALUES FOR OVAL(CIRCLE), LINE
    """


pass


def line_click(self, event):
    """
    SHOULD ABLE TO HANDLE THE MOUSE CLICK EVENT AND PASS CO-ORDINATES TO THE CREATE_LINE EVENT FOR THE CANVASE AND PASS THE FILL COLOR AND SET WIDTH PROPERTIES AND SHOULD ABLE TO CLEAR THE PREVIOUS VALUES
    """


pass


def Circle_Click(self, event):
    """
    SAME AS THE LINE-CLICK METHOD BUT SHOULD CREATE A OVAL HERE
    """

    pass


def enable_menu(self):
    """
    THIS METHOD SHOULD BE ABLE TO HANDLE THE MENUBAR STATUS AND CONFIGURE TO NORMAL STATUS WHEN NEW BUTTON IS SELECTED
    """
    if enabled:


enabled = False
self.paint_Menu.entryconfigure(2, state=tk.DISABLED)
else:
enabled = True
self.paint_Menu.entryconfigure(2, state="normal")
# .................
# .....................
# .........................
pass

pass


def Get_Cordinate_Points(self, wid_typ):
    call = GetPointsDialog(self.root, wid_typ)

    """
    CALL THE TOPLEVEL WINDOW FROM THIS METHOD, SHOULD GET THE CO-ORDINATES AND COLOR AND STRIKE/UNSTRIKE PROPERTIES AND DECIDE TO CALL THE Create_Circle OR Create_OR Create_Rect Line METHODS

    """


pass


def Create_Circle(self, x1, y1, rad, Da_or_UDa, Colo):
    """
    CREATE CIRCLE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
    """


pass


def Create_Line(self, x1, y1, x2, y2, Da_or_UDa, Colo):
    """
    CREATE LINE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
    """


pass


def Create_Rect(self, x1, y1, x2, y2, Da_or_UDa, Colo):
    """
    CREATE RECTANGE ON THE CANVAS WITH THE CORDINATES AND VALUES RECEIVED FROM THE USER INPUT
    """


pass


def clear_canvas(self):
    '''
    triggered when the menu command 'Clear' is clicked
    delete everything from the canvas and set the coefficients to 0's
    '''
    self.cnvs.delete("all")


pass


def save_canvas(self):
    '''
    triggered when the menu command 'Save plot as .PS' is clicked
    save the graph as '{your_student_id_number}.ps'
    '''
    self.cnvs.postscript(file="1015211.ps")


pass


def show_help_about(self):
    '''
    triggered when the menu command 'About' is clicked
    Show an information dialog displaying your name on one line and id number on the second
    '''
    pass


def exit(self):
    '''
    triggered when the menu command 'Exit' is clicked
    Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
    '''
    pass


p = Painter();