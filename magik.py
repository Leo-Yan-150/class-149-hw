from tkinter import *
import random

root=Tk()

root.title("Lucky Friend")
root.geometry("500x500")
root.configure(background = 'lavender')

wable = Label(root)

zl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ""]
print(zl)

def rw():
    random_no1 = random.randint(0,26)
    random_no2 = random.randint(0,26)
    random_no3 = random.randint(0,26)
    random_no4 = random.randint(0,26)
    random_no5 = random.randint(0,26)
    rl1 = zl[random_no1]
    rl2 = zl[random_no2]
    rl3 = zl[random_no3]
    rl4 = zl[random_no4]
    rl5 = zl[random_no5]
    wable["text"] = rl1 + rl2 + rl3 + rl4 + rl5
    
zmagicalbutton = Button(root, text="Show Z magikal word, say it and something will happen to somebody", command = rw)
zmagicalbutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)
wable.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()