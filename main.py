#======================================== Libraries =================================================================
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

import Login as login

#===================================================================================================================

class Main_Window:
        def __init__(self,root):
            self.root=root
            self.root.title("Home Page")
            self.root.geometry("1350x700+0+0")
            
            title=Label(self.root, text=f"Barcelona Landing Page, Login or Sign Up", font=("times new roman", 40, "bold"), bg="light grey", fg="blue", bd=10, relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)
            Main_Frame=Frame(self.root, bg="white")
            Main_Frame.place(x=400, y=150)

            logon_btn=Button(Main_Frame, text="Login", width=15, command=self.new_window, font=("times new roman", 14, "bold"), bg="blue", fg="white").grid(row=1, column=1,pady=10)

        def new_window(self):
            self.root.withdraw()
            self.newWindow = Toplevel(self.root)
            self.app = login.Login_System(self.newWindow)

root=Tk()
obj=Main_Window(root)
root.mainloop()