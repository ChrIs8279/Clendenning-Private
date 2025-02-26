import tkinter as tk



class TypingLabel(tk.Label):
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
        self.create_widgets()

        self.welcome_lbl = TypingLabel(self.master, text="Welcome to the Unknown", fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland", 20))
        self.welcome_lbl.pack(pady=10)

        # Schedule the typing animation for the second label after a delay
        self.master.after(2000, self.start_next_animation)  # Adjust the delay as needed

    def create_widgets(self):
        pass

    def start_next_animation(self):
        # Start typing animation for the second label
        self.press_start = TypingLabel(self.master, text="Press Start :", fg="#F5F5DC", bg="#8B4513", bd=3, relief=tk.RIDGE, font=("woodland", 20))
        self.press_start.pack()

def main():
    root = tk.Tk()
    root.title("Typing Animation Example")
    app = StoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()