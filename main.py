from  tkinter import *
from tkinter import messagebox
screen = Tk()
screen.title("message box")
screen.geometry("400x600")
def show():
    messagebox.showinfo("information","this is information message box")
def show_warning():
    messagebox.showwarning("warning","Proceed with caution")
def show_error():
    messagebox.showerror("error","AN ERROR HAS OCCURED")
def ask_question():
    messagebox.askquestion("question","do you want to proceed")
def askokcancel():
    messagebox.askokcancel("YES or no","do you want to cancel")
Button(screen,text="show info",command=show).pack(pady=10)
Button(screen,text="show warning",command=show_warning).pack(pady=10)
Button(screen,text="show error",command=show_error).pack(pady=10)
Button(screen,text="show question",command=ask_question).pack(pady=10)
Button(screen,text="askokcancel",command=askokcancel).pack(pady=10)
screen.mainloop()


