from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num + random.randint(0, 100))
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range (10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        number = simpledialog.askinteger(title='Choose a random number', prompt="???-???")
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if number == random_num:
            simpledialog.askstring(title='You won...', prompt="Now close the game.")
            sys.exit(0)
        # 7. if the guess is high
        else:
            if number > random_num:
                simpledialog.askstring(title='WRONG', prompt="/.")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            else:
                if number < random_num:
                    simpledialog.askstring(title='WRONG', prompt="\.")
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    simpledialog.askstring(title='GAME', prompt="OVER. No more games for you. *******")
    # window.mainloop()
