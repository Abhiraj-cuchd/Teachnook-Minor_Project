# Importing the Modules
import tkinter as tk
import datetime
from win11toast import toast


class Countdown(tk.Frame):
    """
    Creating the Countdown Class
    """

    def __init__(self, master):
        super().__init__(master)
        self.timer_on_ = False
        self.show_bg()
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self.seconds_passed = 0

    def show_bg(self):
        """
        This function brings up the header
        """
        bg = tk.PhotoImage(file='tkinter-bg.png')

        my_canvas = tk.Canvas(self, width=600, height=50)
        my_canvas.pack(fill="both", expand=True)

        my_canvas.create_image(0, 0, image=bg, anchor='nw')

        my_canvas.create_text(290, 30, text="Apna Time Aayega!!", font=('Ubuntu', 20), fill="Black")

    def show_widgets(self):
        """
        Function to show the buttons and other widgets on the screen
        """
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.resume.pack()

    def create_widgets(self):
        """
        Creating the buttons , textfield , etc
        """
        self.label = tk.Label(self, text='Enter the time in seconds..')
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.reset = tk.Button(self, text='Reset', command=self.reset_button)
        self.stop = tk.Button(self, text='Pause', command=self.stop_button)
        self.start = tk.Button(self, text='Start', command=self.start_button)
        self.resume = tk.Button(self, text='Resume', command=self.resume_button)

    def countdown(self):
        """
        This function starts the countdown
        """
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self.seconds_passed += 1
            self.timer_on_ = self.after(1000, self.countdown)
        else:
            self.timer_on_ = False

            # This function triggers when time is Over.
            toast('Countdown Timer', 'Apna Time Chala Gaya! :(', button='Dismiss', audio='ms-winsoundevent'
                                                                                         ':Notification.Looping.Alarm')

    def reset_button(self):
        """
        Function to trigger reset_timer function
        """
        self.seconds_left = 0
        self.entry.delete(0, 'end')
        self.stop_timer()
        self.timer_on_ = False
        self.label['text'] = "Enter the time in seconds"
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_button(self):
        """
        Function to trigger the stop_timer function
        """
        self.seconds_left = int(self.entry.get())
        self.stop_timer()

    def resume_button(self):
        """
        Function to resume the timer in case the timer is paused
        """
        self.seconds_left = int(self.entry.get()) - self.seconds_passed
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def start_button(self):
        """
        Function that starts the countdown
        """
        self.seconds_left = int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_timer(self):
        """
        Function to stop the timer
        """
        if self.timer_on_:
            self.after_cancel(str(self.timer_on_))
            self.timer_on_ = False

    def convert_seconds_left_to_time(self):
        """
        This function converts the time entered the textfield from string format to datetime
        """
        return datetime.timedelta(seconds=self.seconds_left)


# Creating the Driver Code
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x300")
    root.iconbitmap(r'icon.ico')

    root.title("Countdown Timer")

    countdown = Countdown(root)

    countdown.pack()

    root.mainloop()
