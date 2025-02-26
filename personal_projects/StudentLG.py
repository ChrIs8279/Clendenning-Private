from tkinter import *
import csv


def printMessage():

    with open("student_database.csv", "a") as w_csv:
        fields = ["username", "password", "Student ID", "Homeroom", "firstname", "lastname", "Grade", "Age" ] # ADD MORE ROW HEADER
        csvwrite =  csv.DictWriter(w_csv, fieldnames=fields)
        csvwrite.writerow({"username": passname.get(), "password": passcode.get(), "Student ID": passSID.get(), "Homeroom": passhome.get(), "firstname":passfirst.get(), "lastname":passlast.get(), "Grade":passgrade.get(), "Age":passage.get()}) #ADD MORE key:value pairs

    if passname.get()==("") or passcode.get()==("") or passhome.get()==("") or passSID.get()==("") or passfirst.get()==("") or passlast.get()==("") or passgrade.get()==("") or passage.get()==(""):
        print("please enter all information")
    else:
        print("Record created successful")

    passname.delete(0,END)
    passcode.delete(0,END)
    passhome.delete(0,END)
    passSID.delete(0,END)
    passfirst.delete(0,END)
    passlast.delete(0,END)
    passgrade.delete(0,END)
    passage.delete(0,END)
    
    

root = Tk()
root.title("Student record creator")
root.minsize(width=400,height=200)
root.iconbitmap("LHHS_IMG.png")


upperframe = Frame(root)
upperframe.pack(side="top")
Lmiddleframe = Frame(root)
Lmiddleframe.pack()
# Rmiddleframe = Frame(root)
# Rmiddleframe.pack(side="right")
bottomframe = Frame(root)
bottomframe.pack(side="bottom")

Ttable = Label(upperframe, text="student record creator:")
Ttable.grid(row=0,column=0)
blank1=Label(upperframe, text="")
blank1.grid(row=1,column=0,sticky=E)
blank2=Label(upperframe,text="")
blank2.grid(row=2,column=0)

Name = Label(Lmiddleframe, text="username")
Name.grid(row=0, column=0, sticky=E)
passname = Entry(Lmiddleframe)
passname.grid(row=0, column=1, sticky=E)

password= Label(Lmiddleframe, text="password")
password.grid(row=1,column=0,sticky=E)
passcode = Entry(Lmiddleframe)
passcode.grid(row=1,column=1,sticky=E)

SID = Label(Lmiddleframe, text="Student ID")
SID.grid(row=0,column=2,sticky=E)
passSID= Entry(Lmiddleframe)
passSID.grid(row=0,column=3,sticky=E)

HomeRoom=Label(Lmiddleframe, text="Homeroom")
HomeRoom.grid(row=1,column=2,sticky=E)
passhome= Entry(Lmiddleframe)
passhome.grid(row=1,column=3,sticky=E)

grade=Label(Lmiddleframe,text="Grade")
grade.grid(row=3,column=2,sticky=E)
passgrade= Entry(Lmiddleframe)
passgrade.grid(row=3,column=3,sticky=E)

age=Label(Lmiddleframe,text="Age")
age.grid(row=4,column=2,sticky=E)
passage= Entry(Lmiddleframe)
passage.grid(row=4,column=3,sticky=E)

first= Label(Lmiddleframe, text="firstname")
first.grid(row=3,column=0,sticky=E)
passfirst = Entry(Lmiddleframe)
passfirst.grid(row=3,column=1,sticky=E)

last= Label(Lmiddleframe, text="lastname")
last.grid(row=4,column=0,sticky=E)
passlast = Entry(Lmiddleframe)
passlast.grid(row=4,column=1,sticky=E)

# blank=Label(Rmiddleframe,text="")
# blank.grid(row=5,column=0,sticky=E)





submit= Button(Lmiddleframe,text="submit",command=printMessage, width=25)
submit.grid(row=6,column=2,sticky=E)
blank3=Label(Lmiddleframe,text="")
blank3.grid(row=5,column=2)
# submit.pack()
root.mainloop()

