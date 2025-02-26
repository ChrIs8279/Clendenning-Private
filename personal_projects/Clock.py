import tkinter as tk
import time
import datetime



def up_time():
    cur_time = time.strftime("%I:%M %p")
    clock_label.config(text=cur_time)
    root.after(1000, up_time)

def up_date():
    cur_date = datetime.datetime.now()
    date = cur_date.strftime("%a, %b %d %Y")
    date_label.config(text=date)
    root.after(3600000, up_date)


root=tk.Tk()
root.title("Clock")
root.minsize(width=400,height=100)
root.configure(bg="black")
root.resizable(False,False)

uframe = tk.Frame(root)
uframe.pack()

clock_label = tk.Label(uframe, text="",foreground="white",background="black", font=("helvetia, 54"))
clock_label.grid(row=0)

date_label = tk.Label(uframe, text="",foreground="white",background="black", font=("helvetia, 30"))
date_label.grid(row=1)


up_time()
up_date()



if __name__ == "__main__":
    root.mainloop()