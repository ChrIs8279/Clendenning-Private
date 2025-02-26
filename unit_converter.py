import tkinter as tk

class unitconverter:
    def __init__(self,master):
        self.master = master

        frame = tk.Frame()
        frame.pack(fill=tk.BOTH, expand=True)

        self.title = tk.Label(frame, text="Select a Converter",width=20,height=2, bd=4,relief=tk.SOLID, font=("Helvetica", 12))
        self.title.pack(ipady=10)

        self.Meters_to_Kilometer = tk.Button(frame, text="Meters to Kilometers",bd=4,relief=tk.RAISED, command=self.cmd_Meters_Kilometers)
        self.Meters_to_Kilometer.pack()

        self.Kilometers_to_Meters = tk.Button(frame, text="Kilometers to Meters", bd=4,relief=tk.RAISED)
        self.Kilometers_to_Meters.pack()

        self.Feet_to_Meters = tk.Button(frame,text="Feet to Meters",bd=4, relief=tk.RAISED)
        self.Feet_to_Meters.pack()

        self.Meters_to_Feet = tk.Button(frame, text="Meters to Feet",bd=4,relief=tk.RAISED)
        self.Meters_to_Feet.pack()

        self.Miles_to_Kilometers = tk.Button(frame,text="Miles to Kilometers", bd=4,relief=tk.RAISED)
        self.Miles_to_Kilometers.pack()

        self.Kilometers_to_Miles = tk.Button(frame,text="Kilometers to Miles",bd=4,relief=tk.RAISED)
        self.Kilometers_to_Miles.pack()

            tk.mainloop()

    # def get_number(self):
    #     Meters_Kilometers.get + Kilometrer_Meters.get + Feet_Meters.get + Meters_Feet.get + Miles_Kilometers.get + Kilometers_Milesdef cmd_Meters_kilometers(self):
        self.Kilometers_to_Meters.pack_forget
        self.Meters_to_Kilometer.pack_forget
        self.Feet_to_Meters.pack_forget
        self.Meters_to_Feet.pack_forget
        self.Kilometers_to_Miles.pack_forget
        self.Miles_to_Kilometers.pack_forget   

   

    
    
    


# submit.pack()
