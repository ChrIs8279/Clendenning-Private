import tkinter as tk


class StoryApp:
    def __init__(self, master):
        self.master = master
        self.story_index = 0
        self.prologue_displayed = False
        
       
        # for home
        # self.background_image = tk.PhotoImage(file="/home/_chrixxy_/python_shit/river_bg_resize.png")
        # for school
        self.background_image = tk.PhotoImage(file="Click_game/Ambient_forest_resize.png")
        
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        self.create_widgets(show=False)
    

        self.welcome_lbl = tk.Label(self.master, text="Welcome to the Unknown", fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland,20"))
        self.welcome_lbl.pack(pady=10)

        self.press_start = tk.Label(self.master, text="Press Start :", fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland,20"))
        self.press_start.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.toggle_prologue, fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland,20"))
        self.start_button.pack(pady=20)
        
    def create_widgets(self, show=True):
        if show:
            # Create widgets if show is True
            self.story_text = tk.Label(self.master, text="Pick your starting point!", fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland, 15"))
            self.story_text.pack(pady=20)

            self.st_txt2 = tk.Label(self.master, text="Chose Wisely :", fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland, 12"))
            self.st_txt2.pack(pady=2)

            self.st_txt3 = tk.Label(self.master, text="",fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland, 12"))
            self.st_txt3.pack(pady=2)

            self.option1_button = tk.Button(self.master, text="Story 1: Where?", fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, command=self.choose_option_1, font=("woodland, 10"))
            self.option1_button.pack(pady=5)

            self.option2_button = tk.Button(self.master, text="Story 2: Lost?", command=self.choose_option_2, fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE, font=("woodland, 10"))
            self.option2_button.pack(pady=5)

            self.prologue_displayed = True
        else:
            # Remove widgets if show is False
            if hasattr(self, 'story_text'):
                self.story_text.pack_forget()
            if hasattr(self, 'option1_button'):
                self.option1_button.pack_forget()
            if hasattr(self, 'option2_button'):
                self.option2_button.pack_forget()

    def toggle_prologue(self):
        self.create_widgets(show=False)
        self.protext = tk.Label(self.master, text="Welcome to the Prologue", font=("woodland, 14"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext.pack(pady=5)
        self.protext2 = tk.Label(self.master, text="You've been Stranded on a Remote Island after a Plane Malfunction.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext2.pack(pady=2)
        self.protext3 = tk.Label(self.master, text="The Pilot was able to Radio a Distress Signal Before Impact.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext3.pack(pady=2)
        self.protext4 = tk.Label(self.master, text="But Your Exact Location Remains Unclear.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext4.pack(pady=2)
        self.protext5 = tk.Label(self.master, text="Your Survival Skills and Resourcefulness will be put to the Test as you wait for Rescue.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext5.pack(pady=2)
        self.protext6 = tk.Label(self.master, text="Expect the Worst, Discover the Unknown. Trust no one.",font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.protext6.pack(pady=2)
        self.continue_button = tk.Button(self.master, text="Continue?", command=self.continue_story, font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=2, relief=tk.GROOVE)
        self.continue_button.pack(pady=10)
        self.start_button.pack_forget()
        self.welcome_lbl.pack_forget()
        self.press_start.pack_forget()

    def continue_story(self):
        self.create_widgets(show=True)
        self.continue_button.pack_forget()
        self.protext.pack_forget()
        self.protext2.pack_forget()
        self.protext3.pack_forget()
        self.protext4.pack_forget()
        self.protext5.pack_forget()
        self.protext6.pack_forget()
        self.st_txt3.pack_forget()

    def display_story(self, action, word, info, option1_text, option2_text):
        self.story_text.config(text=action)
        self.st_txt2.config(text=word)
        self.st_txt3.config(text=info)
        self.option1_button.config(text=option1_text)
        self.option2_button.config(text=option2_text)

    


    def choose_option_1(self):
        self.story_text.pack_forget()
        self.st_txt2.pack_forget()
        self.st_txt3.pack_forget()
        self.option1_button.pack_forget()
        self.option2_button.pack_forget()
        self.create_widgets()
        if self.story_index == 0:
            self.display_story("You Wake up:", "Where am I? How'd I get here?", ".", "Get up and look around?","Stay on the soft warm grass?")
            self.st_txt3.pack_forget()
            self.story_index = 1
        elif self.story_index == 1:
            self.display_story("You Stand up, your vision white and blury:", "I remember nothing", "What's my name again?","Connor?","Abby?")
            self.story_index = 2
        elif self.story_index == 2:
            self.display_story("You Hear a Voice:", "Connor! Connor! Thank god You're OK!", "How'd you end up here, The wreck is half a kilometer away","Who are you?","I'm not sure, I just woke up here")
            self.story_index = 3
        elif self.story_index == 3:
            self.display_story("Adam:", "You don't remember me?", "It's your best friend Adam? The one from kindergarden?","I can't Remember anything","Oh yeah I remember now (Lie)")
            self.story_index = 5
        elif self.story_index == 4:
            self.display_story("Bella:", "You don't remember me?", "It's your best friend Bella? The one from kindergarden?","Who? I don't know you?","Oh yeah I remember now (Lie)")
            self.story_index = 5
        elif self.story_index == 5:
            self.display_story("Shit! :","You must of hit your head hard?","You're bleeding!","Do you know how I got here?","who am I? Like supposed to be?")
            self.story_index = 20
        
        elif self.story_index == 20:
            self.display_story("Ready for another?", "Select a story :", ".","Where?", "Lost?")
            self.st_txt3.pack_forget()
            self.story_index = 0
        
    def choose_option_2(self):
        self.story_text.pack_forget()
        self.st_txt2.pack_forget()
        self.st_txt3.pack_forget()
        self.option1_button.pack_forget()
        self.option2_button.pack_forget()
        self.create_widgets()
        if self.story_index == 0:
            self.display_story("You Break the Surface","Holy Shit! Of all places!", "I ended up in a river","Try Swimming to land?","Keep treading down the river?")
            self.story_index = 4
        elif self.story_index == 4:
            self.display_story("You Struggle fighing the current","But it pulls you under","A Rock strikes your head, knocking you unconcience","Continue",".")
            self.option2_button.pack_forget()
            self.story_index = 0
        elif self.story_index == 2:
            self.display_story("You Hear a Voice:", "Abby! Abby! Thank god You're OK!", "How'd you end up here, The wreck is half a kilometer away","Who are you?","I'm not sure, I just woke up here")
            self.story_index = 4
        elif self.story_index == 5:
            self.display_story("You're scaring me :","You sure you're ok?","You're bleeding!","I'm all good, must of hit my head","I can't rememer anything!")
            self.story_index = 20
        elif self.story_index == 20:
            self.display_story("Ready for another?", "Select a story :", ".", "Where?", "Lost?")
            self.story_index = 0

def main():
    root = tk.Tk()
    root.title("The Unkown")
    app = StoryApp(root)
    app.background_label.lower()
    root.geometry("550x250")
    root.resizable(False,False)

    root.mainloop()
    
if __name__ == "__main__":
    main()


