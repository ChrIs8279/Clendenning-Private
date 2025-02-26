import tkinter as tk


class Type_LR(tk.Label):
    def __init__(self, master, text, delay=100, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.delay = delay
        self.index = 0
        self.update_text()

    def update_text(self):
        if self.index < len(self.text):
            self.config(text=self.text[:self.index+1])
            self.index += 1
            self.after(self.delay, self.update_text)


class StoryApp:
    def __init__(self, master):
        self.master = master
        self.story_index = 0
        
       
        # background image. comment out or replace with own image to run
        self.background_image = tk.PhotoImage(file="Click_game/river_bg_resize.png")
        
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.welcome_lbl = Type_LR(self.master, text="Welcome to the Unknown", fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland,20"))
        self.welcome_lbl.pack(pady=10)

        self.demo_explain = Type_LR(self.master, text=":top button only for demo:",fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland,5"))
        self.demo_explain.pack(pady=5)

        self.master.after(2000, self.next_animation)
        self.master.after(3500, self.button_show)
        self.master.after(3500, self.skip_show)
    def next_animation(self):
        self.press_start = Type_LR(self.master, text="Press Start :", fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland,20"))
        self.press_start.pack()
    def button_show(self):
        self.start_button = tk.Button(self.master, text="Start", command=self.toggle_prologue, fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RAISED, font=("woodland,20"), width=15,height=1)
        self.start_button.pack(pady=30)
    def skip_show(self):
        self.skip_button = tk.Button(self.master, text= "Skip Prologue", command= self.skip_prologue, fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RAISED, font=("woodland,20"), width=15,height=1)
        self.skip_button.pack(pady= 5)
            
    def create_widgets(self):
            
        self.story_text = tk.Label(self.master, text="Pick your starting point!", fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RIDGE, font=("woodland, 15"))
        self.story_text.pack(pady=20)
        self.st_txt2 = tk.Label(self.master, text="Chose Wisely :", fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland, 12"))
        self.st_txt2.pack(pady=2)

        self.st_txt3 = tk.Label(self.master, text="",fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland, 12"))
        self.st_txt3.pack(pady=2)

        self.option1_button = tk.Button(self.master, text="Story 1: Where?", fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RAISED, command=self.choose_option_1, font=("woodland, 10"))
        self.option1_button.pack(pady=5)

        self.option2_button = tk.Button(self.master, text="Story 2: Lost?", command=self.choose_option_2, fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RAISED, font=("woodland, 10"))
        self.option2_button.pack(pady=5)

    def toggle_prologue(self):
        self.start_button.pack_forget()
        self.welcome_lbl.pack_forget()
        self.press_start.pack_forget()
        self.skip_button.pack_forget()
        self.demo_explain.pack_forget()
        self.protext = Type_LR(self.master, text="Welcome to the Prologue", font=("woodland, 14"), fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RIDGE)
        self.protext.pack(pady=5)
        self.master.after(2000, self.two_protext)
        self.master.after(8000, self.three_protext)
        self.master.after(14000, self.four_protext)
        self.master.after(18000, self.five_protext)
        self.master.after(24000, self.six_protext)
        self.master.after(30000, self.procontinue)
    def two_protext(self):
        self.protext2 = Type_LR(self.master, text="You've been Stranded on a Remote Island after a Plane Malfunction.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.GROOVE)
        self.protext2.pack(pady=2)
    def three_protext(self):
        self.protext3 = Type_LR(self.master, text="The Pilot was able to Radio a Distress Signal Before Impact.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.GROOVE)
        self.protext3.pack(pady=2)
    def four_protext(self):
        self.protext4 = Type_LR(self.master, text="But Your Exact Location Remains Unclear.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.GROOVE)
        self.protext4.pack(pady=2)
    def five_protext(self):
        self.protext5 = Type_LR(self.master, text="Your Survival Skills and Resourcefulness will be put to the Test.", font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.GROOVE)
        self.protext5.pack(pady=2)
    def six_protext(self):
        self.protext6 = Type_LR(self.master, text="Expect the Worst, Have Fun. Discover the Unknown",font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.GROOVE)
        self.protext6.pack(pady=2)
    def procontinue(self):
        self.continue_button = tk.Button(self.master, text="Continue?", command=self.continue_story, font=("woodland, 10"), fg="#F5F5DC", bg="#8B4513", bd=4, relief=tk.RAISED)
        self.continue_button.pack(pady=10)
    
    def skip_prologue(self):
        self.create_widgets()
        self.start_button.pack_forget()
        self.welcome_lbl.pack_forget()
        self.press_start.pack_forget()
        self.skip_button.pack_forget()
        self.st_txt3.pack_forget()
        self.demo_explain.pack_forget()


    def continue_story(self):
        self.create_widgets()
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
# index 4 needs work
        elif self.story_index == 4:
            self.display_story("Bella:", "You don't remember me?", "It's your best friend Bella? The one from kindergarden?","Who? I don't know you?","Oh yeah I remember now (Lie)")
            self.story_index = 5

        elif self.story_index == 5:
            self.display_story("Shit!","You must of hit your head hard?","You're bleeding!","Do you know how I got here?","who am I?")
            self.story_index = 10

        elif self.story_index == 10:
            self.display_story("After the crash","You must of drifted down river","it's a miracle you're still alive","What happened?","who am I?")
            self.story_index = 11

        elif self.story_index == 11:
            self.display_story("we were in a plane flying to germany on a buisness trip","that's when it happened!","It all when to shit","how long ago did the plane go down?","Are there any survivors?")
            self.story_index= 12

        elif self.story_index == 12:
            self.display_story("The plane crashed 20 hours ago","the plane split in two","I was sent to look for the front half","There are others?","How far away Did the Front end land?")
            self.story_index = 13

        elif self.story_index == 13:
            self.display_story("A couple","theres about 9 of us","10 if I include you","can you take me to them?","I'll help you look for the plane")
            self.story_index = 14

        elif self.story_index == 14:
            self.display_story("You Follow your friend","After walking a couple minutes you reach the camp", "you smell the pleasent scent of the campfire","Continue","")
            self.option2_button.pack_forget()
            self.story_index = 21

        elif self.story_index == 8:
            self.display_story("If you say so.","If you start feeling weird tell me","understood?","understood",".")
            self.option2_button.pack_forget()
            self.story_index = 9

        elif self.story_index == 6:
            self.display_story("select a name:",".",".","Connor?","Abby?")
            self.st_txt2.pack_forget()
            self.st_txt3.pack_forget()
            self.story_index = 2
        
        elif self.story_index == 20:
            self.display_story("Ready for another?", "Select a story :", ".","Where?", "Lost?")
            self.st_txt3.pack_forget()
            self.story_index = 0

        elif self.story_index == 21:
            self.display_story("congratulations!","You're safe now!","Click continue to play again","Continue","")
            self.option2_button.pack_forget()
            self.story_index = 20
        
        elif self.story_index == 22:
            self.display_story("Yopu died","better luck next time?","Click continue to try again","Continue","")
            self.option2_button.pack_forget()
            self.story_index = 20
        
    def choose_option_2(self):
        self.story_text.pack_forget()
        self.st_txt2.pack_forget()
        self.st_txt3.pack_forget()
        self.option1_button.pack_forget()
        self.option2_button.pack_forget()
        self.create_widgets()
        if self.story_index == 0:
            self.display_story("You Break the Surface","Of all places!", "I ended up in a river","Try Swimming to land?","Keep treading down the river?")
            self.story_index = 4

        elif self.story_index == 4:
            self.display_story("You Struggle fighing the current","But it pulls you under","A Rock strikes your head, knocking you unconcience","Continue",".")
            self.option2_button.pack_forget()
            self.story_index = 0

        elif self.story_index == 2:
            self.display_story("You Hear a Voice:", "Abby! Abby! Thank god You're OK!", "How'd you end up here, The wreck is half a kilometer away","Who are you?","I'm not sure, I just woke up here")
            self.story_index = 4

        elif self.story_index == 4:
            self.display_story("Are you hurt?","Do you feel ok?",".","Just a little fuzzy.","I think I feel sick.")

        elif self.story_index == 5:
            self.display_story("You're scaring me :","You sure you're ok?","You're bleeding!","I'm all good, must of hit my head","I can't rememer anything!")
            self.story_index = 8

        elif self.story_index == 8:
            self.display_story("Shit! :","You must of hit your head hard?","You're bleeding!","Do you know how I got here?","Who am I?")
            self.story_index = 20

        elif self.story_index == 1:
            self.display_story("You lay silent with the sound of running water.","You hear a noice in the forest.",".","Get up and Scan for Danger.","Stay Low and Hope it Passes.")
            self.st_txt3.pack_forget()
            self.story_index = 6

        elif self.story_index == 6:
            self.display_story("You stay low.","The noise passes leaving you in silence","what should you do now?","Follow the noise?","Build up camp?")
            self.story_index = 23
        
        elif self.story_index == 23:
            self.display_story("You gather sticks and leaves","you build up a frame against a tree","then lay leaves and mud for walls","Continue.","Continue.")
            self.option1_button.pack_forget()
            self.story_index = 24

        elif self.story_index == 24:
            self.display_story("what should you do now?",".",".","Build a Fire?","Go Hunting?")
            self.st_txt2.pack_forget()
            self.st_txt3.pack_forget()
            self.story_index = 25

        elif self.story_index == 25:
            self.display_story("You pick up a stick","its thin but long like a spear","perfect for hunting small to medium animals","Continue.","")
            self.option2_button.pack_forget()
            self.story_index = 20

        # elif st


        elif self.story_index == 20:
            self.display_story("Ready for another?", "Select a story :", ".", "Where?", "Lost?")
            self.st_txt3.pack_forget()
            self.story_index = 0

def main():
    root = tk.Tk()
    root.title("Choose Your Own Adventure")
    app = StoryApp(root)
    app.background_label.lower()
    root.geometry("550x250")
    root.resizable(False,False)

    root.mainloop()
    
if __name__ == "__main__":
    main()


