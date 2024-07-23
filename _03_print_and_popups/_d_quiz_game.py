from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    q1 = simpledialog.askstring(title='Question 1', prompt="What happens when you mix sodium with chlorine.\n"
    "A. Sodium Chloride\n"
    "B. Nothing happens\n"
    "C. They explode and separate\n"
    "D. They freeze everything nearby")
    #      // 3.  Use an if statement to check if their answer is correct
    if q1 == "A" or q1 == "a" or q1 == "a." or q1 == "A.":
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        prompt = simpledialog.askstring(title='Correct', prompt="You earned 1 score. Total score: " + str(score))
    else:
        prompt = simpledialog.askstring(title='INCORRECT', prompt="You are 'dead'.\n")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    q1 = simpledialog.askstring(title='Question 2', prompt="How hard does an alligator bite.\n"
    "A. 5000-9000\n"
    "B. 1000-2000\n"
    "C. 2000-3000\n"
    "D. None of the Above")

    if q1 == "c" or q1 == "C" or q1 == "c." or q1 == "C.":
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
        prompt = simpledialog.askstring(title='Correct', prompt="You earned 1 score. Total score: " + str(score))
    else:
        prompt = simpledialog.askstring(title='INCORRECT', prompt="You are 'dead'.\n")

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function

    # Run the window's .mainloop() method
