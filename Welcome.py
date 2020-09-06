#======================================== Libraries =================================================================
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

#===================================================================================================================

class Welcome_Window:
    def __init__(self,root):

        self.bg_icon=ImageTk.PhotoImage(file="images/bg3.jpg")

        self.root=root
        self.root.title("Home Page")
        self.root.geometry("1350x700+0+0")
        bg_lbl=Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root, text=f"Barcelona Home Page, logged in", font=("times new roman", 40, "bold"), bg="light grey", fg="blue", bd=10, relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        Main_Frame=Frame(self.root, bg="white")
        Main_Frame.place(x=400, y=150)

        logon_btn=Button(Main_Frame, text="Exit", width=15, command=self.exit, font=("times new roman", 14, "bold"), bg="blue", fg="white").grid(row=1, column=1,pady=10)
    
    def exit(self):
        sys.exit(0)