from tkinter import *
root=Tk()
root.title("Calculator")
root.minsize(height=280,width=200)

inputstring= StringVar()
inputstring.set("")

# def expression(Value):
#     current = inputstring.get()
#     new = current + Value
#     inputstring.set(new)
    
# def answer():


def plus_min():
    global expression
    total = int(eval(expression))
    plmi = str(total - total * 2)
    inputstring.set(plmi)
    
    



expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    inputstring.set(expression)

def answer():
    try:
        global expression
        total = str(eval(expression))
        inputstring.set(total)
        expression = ""
    except:
        inputstring.set(" error ")
        expression = ""

def clear_all():
    global expression
    expression = ""
    inputstring.set("")
    while FALSE:
        break

# def eval():
#     pass

# def ans(responce):
#     answer = current.get()
    
   

main=LabelFrame(root,padx=5,pady=5)
main.place(relx=0.5,rely=0.5,anchor="center")

buttonframe = Frame(main)
buttonframe.pack()

inputfeild=Label(buttonframe, textvariable=inputstring, bd=2,relief="sunken",bg="white", height=4)
inputfeild.grid(row=0, columnspan=4,sticky="nwse",pady=5)

button7=Button(buttonframe,text="7", width=5, height=2, command=lambda: press(7))
button7.grid(row=1,column=0)
button8=Button(buttonframe,text="8", width=5, height=2, command=lambda: press(8))
button8.grid(row=1,column=1)
button9=Button(buttonframe,text="9", width=5, height=2, command=lambda: press(9))
button9.grid(row=1,column=2)
div=Button(buttonframe,text="/", width=5, height=2, command=lambda: press("/"))
div.grid(row=1,column=3)

button4=Button(buttonframe,text="4", width=5, height=2, command=lambda: press(4))
button4.grid(row=2,column=0)
button5=Button(buttonframe,text="5", width=5, height=2, command=lambda: press(5))
button5.grid(row=2,column=1)
button6=Button(buttonframe,text="6", width=5, height=2, command=lambda: press(6))
button6.grid(row=2,column=2)
mul=Button(buttonframe,text="x", width=5, height=2, command=lambda: press("*"))
mul.grid(row=2,column=3)

button1=Button(buttonframe,text="1", width=5, height=2, command=lambda: press(1))
button1.grid(row=3,column=0)
button2=Button(buttonframe,text="2", width=5, height=2, command=lambda: press(2))
button2.grid(row=3,column=1)
button3=Button(buttonframe,text="3", width=5, height=2, command=lambda: press(3))
button3.grid(row=3,column=2)
min=Button(buttonframe,text="-", width=5, height=2, command=lambda: press("-"))
min.grid(row=3,column=3)

pm=Button(buttonframe,text="+/-", width=5, height=2, command=plus_min)
pm.grid(row=4,column=0)
button0=Button(buttonframe,text="0", width=5, height=2, command=lambda: press(0))
button0.grid(row=4,column=1)
dot=Button(buttonframe,text=".", width=5, height=2, command=lambda: press("."))
dot.grid(row=4,column=2)
plus=Button(buttonframe,text="+", width=5, height=2, command=lambda: press("+"))
plus.grid(row=4,column=3)

equal = Button(buttonframe, text="=",width=5, height=2, command=answer)
equal.grid(row=5,column=0)

clear = Button(buttonframe, text= "AC", width=5,height=2, command= clear_all)
clear.grid(row=5, column=1)

# enter=Button(buttonframe,text="enter",command=ans)


root.mainloop()