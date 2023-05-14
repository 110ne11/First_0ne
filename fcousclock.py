import tkinter as tk

class Timer:
    def __init__(self, minutes):
        self.minutes = minutes

        # create the GUI
        self.root = tk.Tk()
        self.root.title("专注时钟")
        self.time_label = tk.Label(self.root, text="")
        self.time_label.pack()
        self.start_button = tk.Button(self.root, text="开始", command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        self.seconds = self.minutes * 60
        self.update_time()
        
    def update_time(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_string)
        
        if self.seconds == 0:
            self.time_label.config(text="时间到！")
        else:
            self.seconds -= 1
            self.root.after(1000, self.update_time)

if __name__ == "__main__":
    timer = Timer(25)
    timer.root.mainloop()
