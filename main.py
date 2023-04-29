from tkinter import *
import os


def Shutdown():
    os.system("shutdown \r \t 1")


def Logout():
    os.system("shutdown -l")


def Restart():
    os.system("shutdown \r \t 1")


def RestartTime():
    os.system("shutdown \r \t 20")

st = Tk()
st.title("Shutdown System")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"),  relief=RAISED, cursor="plus", command=Restart)
r_button.place(x = 150, y = 60, width=200, height=60)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20, "bold"),  relief=RAISED, cursor="plus", command = RestartTime)
rt_button.place(x = 150, y = 180, width=200, height=60)

s_button = Button(st, text="ShutDown", font=("Time New Roman", 20, "bold"),  relief=RAISED, cursor="plus", command= Shutdown )
r_button.place(x = 150, y = 300, width=200, height=60)

l_button = Button(st, text="Logout", font=("Time New Roman", 20, "bold"),  relief=RAISED, cursor="plus", command = Logout)
r_button.place(x = 150, y = 420, width=200, height=60)

st.mainloop()




