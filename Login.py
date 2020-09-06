#======================================== Libraries =================================================================
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
from sqlite3 import Error
import sys
import Welcome as welcome

#===================================================================================================================

conn = sqlite3.connect(r'db\pythonsqlite.db')


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Barcelona FC Login System")
        self.root.geometry("1350x700+0+0")

        #==========================================     Resources   =============================================================================
        self.bg_icon=ImageTk.PhotoImage(file="images/bg3.jpg")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/password.png")
        self.logo_icon=PhotoImage(file="images/ninja.png")

        #==========================================     Variables   ==============================================================================
        self.uname=StringVar()
        self.pass_=StringVar()

        #==========================================     All Layout================================================================================

        #============================ TITLE & BACKGROUND ===================================================
        bg_lbl=Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root, text="Barcelona Login App", font=("times new roman", 40, "bold"), bg="light grey", fg="blue", bd=10, relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        #============Login Frame============================================================================
        Login_Frame=Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        logolbl=Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame, bd=5, relief=GROOVE, show='*', textvariable=self.pass_, font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame, text="Login", width=15, command=self.login, font=("times new roman", 14, "bold"), bg="blue", fg="white").grid(row=3, column=1,pady=10)

    #==============     Login Function ======================================================================
    def login(self):
        c = conn.cursor()
        c.execute(
            '''
                SELECT * FROM users where UserName = ? AND Password = ?
            ''', 
            (self.uname.get(), self.pass_.get())
        )
        

        if self.uname.get()!="" or self.pass_.get()!="":
            if c.fetchall():
                command = self.new_window()
                conn.close()
            else:
                messagebox.showerror("Error!", "Invalid username or password!")
                self.uname.set("")
                self.pass_.set("")
        else:
            messagebox.showerror("Error", "All fields are required!! \nPlease enter username and password!")

    def new_window(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = welcome.Welcome_Window(self.newWindow)