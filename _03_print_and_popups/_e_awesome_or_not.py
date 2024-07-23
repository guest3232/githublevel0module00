from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
    score = random.randint(0, 3)
    # 2. Print your variable to the console
    print(score)
    # 3. Get the user to enter something that they think is awesome
    q1 = simpledialog.askstring(title='What do YOU like to do.', prompt=".")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if score == 0:
        simpledialog.askstring(title='Excellent. I like that', prompt="")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if score == 1:
        simpledialog.askstring(title="It's ok.", prompt="You earned a 50% out of 100. You should do more reading studying next time.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if score == 2:
        simpledialog.askstring(title=q1 + "?", prompt="............................\n"
            ".")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if score == 3:
        simpledialog.askstring(title="That's really funny to me.", prompt="I would try it again sometime")
    # Run the window's .mainloop() method
