from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    waste = simpledialog.askstring(title='What.', prompt="Do you know how to create games... (Only Yes or No question)")

    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if waste == "Yes" or waste == "yes":
        prompt = simpledialog.askstring(title='You guessed WRONG', prompt="You don't know how to do code")
    else:
        if waste == "no" or waste == "No":
            prompt = simpledialog.askstring(title='You guessed WRONG', prompt="You DO know how to do code")
        else:
            prompt = simpledialog.askstring(title="We didn't understand your question.", prompt="asdfghjkl;'qwertyuiop[]zxcvbnm,./")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
