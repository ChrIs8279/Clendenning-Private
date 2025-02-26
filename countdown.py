import tkinter as tk
from tkinter import StringVar
import math
import datetime


root=tk.Tk()
root.geometry("500x200")
root.title("timecounter")
root.configure(bg="black")
root.resizable(False,False)


clockTime = StringVar()
mainFrame = tk.Frame(root)
mainFrame.pack()

def tileft():
    cday = datetime.datetime.now()
    bday = datetime.datetime(2007,4,17)
    tirem = bday - cday
    remtotal= tirem.total_seconds()
    remsec= math.floor((remtotal%60))
    remmin = math.floor((remtotal/60)%60)
    remhour= math.floor(remtotal/3600%24)
    remday = math.floor(remtotal/86400)
    yearold = math.floor((remday/365))
    lastleap = datetime.datetime(2024,1,1)
    prevleap=lastleap-bday
    leapprev= prevleap / 4
    leapyr = 
    # addleap = leapyr 
    if remday < 0:
        remday= remday - 365 * yearold
    days_hours.config(text=(f"{remday} days, {remhour} hours"))
    minutes_seconds.config(text=(f"{remmin} mins, {remsec} seconds"))
    clockTime.set("RUNNING")
    root.after(400, tileft)

name_lbl = tk.Label(mainFrame, text= "Time Left Till my Birthday",foreground="white",background="black", font=("helvetia, 25"))
name_lbl.pack(ipadx=10,ipady=10)
days_hours = tk.Label(mainFrame,text="",foreground="white",background="black", font=("helvetia, 37"),relief=tk.RIDGE)
days_hours.pack(ipadx=10)
minutes_seconds = tk.Label(mainFrame, text= "",bd=3, relief=tk.RIDGE, font=("helvetia, 30"),background="black",foreground="white")
minutes_seconds.pack(ipady=10,ipadx=10)



if __name__ == "__main__":
    tileft()
    root.mainloop()