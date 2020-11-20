
from tkinter import *
from tkinter import messagebox

class Game:
    def __init__(self):
        self.v = 0
        self.name = 'Player'
        self.score = 0
        self.i = 0
        self.L = (
        "MBUN", "WOPER", "RMIEC", "BHATI", "TONRF", "SUMIC", "EPACH", "DGNRI", "SILBS", "AMSPW", "SATCLE", "VENICO",
        "INANCOMN", "SSURUPIO", "CCEENNNIIOV")
        self.c = (
        "NUMB", "POWER", "CRIME", "HABIT", "FRONT", "MUSIC", "PEACH", "GRIND", "BLISS", "SWAMP", "CASTLE", "NOVICE",
        "CINNAMON", "SPURIOUS", "CONVINIENCE")
        self.hint = (
        "INSENSIBLE", "STRENGTH", "VIOLATION OF LAW", "ACTION PERFORMED", "SYNONYM OF FORE", "PLEASANT SOUND",
        "A FRUIT", " TO CRUSH", "HAPPINESS", "TYPE OF WETLAND", "A MANSION", "A BEGINNER", "A SPICE", "NOT AUTHENTIC",
        "PERTAINING TO BE EASY")
        self.setupUI()

    def setupUI(self):
        self.root = Tk()
        self.root.title("Word Cookie")

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(fill=BOTH, expand=1)
        label = Label(self.mainFrame, text="WORD COOKIE", font="fangsongti 32 bold")
        label.grid(row=0, column=0)

        button = Button(self.mainFrame, text='GET SET GO -->', font="bold", command=self.menu)
        button.grid(row=4, column=1)

    def menu(self):
        self.mainFrame.destroy()
        self.menuFrame = Frame(self.root)
        self.menuFrame.pack(fill=BOTH, expand=1)

        label = Label(self.menuFrame, text="MENU:", font="fangsongti 32 bold")
        label.grid(row=0, column=1)

        play = Button(self.menuFrame, text="Register", font="fangsongti 22 bold", command=self.register)
        play.grid(row=2, column=0)

        score = Button(self.menuFrame, text="Scoreboard", font="fangsongti 22 bold", command=self.scoreboard)
        score.grid(row=2, column=2)

        quit = Button(self.menuFrame, text="Quit", font="fangsongti 22 bold", command=self.root.quit)
        quit.grid(row=4, column=1)

    def register(self):
        self.menuFrame.destroy()
        self.registerFrame = Frame(self.root)
        self.registerFrame.pack(fill=BOTH, expand=1)

        label = Label(self.registerFrame, text='REGISTRATION:', font="fangsongti  32 bold")
        label.grid(row=0)

        nameLabel = Label(self.registerFrame, text="Enter Name", font="fangsongti 15 bold")
        nameLabel.grid(row=1, column=0)

        self.nameentry = Entry(self.registerFrame, font="fangsongti 15 bold")
        self.nameentry.grid(row=1, column=1)

        okbutton = Button(self.registerFrame, text="OK", font="fangsongti 22 bold", command=self.playFunc)
        okbutton.grid(row=5, column=0)

    def playFunc(self):
        self.name = self.nameentry.get()
        self.registerFrame.destroy()

        self.playFrame = Frame(self.root)
        self.playFrame.pack(fill=BOTH, expand=1)

        self.level = Label(self.playFrame, text="Level 1", font="fangsongti  32 bold")
        self.level.grid(row=0, column=0, columnspan=1)

        jumbleLabel = Label(self.playFrame, text="Jumble Word", font="fangsongti 15 bold")
        jumbleLabel.grid(row=1, column=0)

        self.jumblewordLabel = Label(self.playFrame, text=self.L[self.i], font="fangsongti 15 bold")
        self.jumblewordLabel.grid(row=1, column=1)

        label = Label(self.playFrame, text="Correct Word", font="fangsongti 15 bold")
        label.grid(row=2, column=0)

        self.wordEntry = Entry(self.playFrame, font="fangsongti 15 bold")
        self.wordEntry.grid(row=2, column=1)

        self.hintbutton = Button(self.playFrame, text="Hint", font="fangsongti 22 bold", command=self.updateHint)
        self.hintbutton.grid(row=3, column=0)

        self.okbutton = Button(self.playFrame, text="OK", font="fangsongti 22 bold", command=self.updateScore)
        self.okbutton.grid(row=3, column=1)

    def scoreboard(self):
        file = open('./score.txt', 'r')
        text1 = ""
        j = file.readlines()
        file.close()
        print(j)
        for i in j:
            text1 += str(i)
        print(text1)
        self.menuFrame.destroy()
        self.scoreframe = Frame(self.root)
        self.scoreframe.pack(fill=BOTH, expand=1)
        label = Label(self.scoreframe, text="SCOREBOARD:", font="fangsongti  32 bold")
        label.pack()
        label1 = Label(self.scoreframe, text=str(text1), font="fangsongti 15 bold")
        label1.pack()
        button = Button(self.scoreframe, text="Back", font="fangsongti 22 bold", command=self.back)
        button.pack()

    def back(self):
        self.root.destroy()
        self.setupUI()

    def updateHint(self):
        self.score -= 5
        self.v = 1
        messagebox.showinfo("HINT", self.hint[self.i])

    def updateScore(self):
        if self.i <= 14:
            if self.v == 1 and self.wordEntry.get() == self.c[self.i]:
                messagebox.showinfo("RESULT", "YOU GUESSED IT!!!\nYOU NEEDED HELP\n+5 POINTS")
                self.v = 0
            elif self.v == 0 and self.wordEntry.get() == self.c[self.i]:
                messagebox.showinfo("RESULT",
                                    "YOU GUESSED IT!!!\nYOU NEEDED NO HELP\n+10 POINTS\nhere's a cookie: NOM! NOM! NOM! COOKIE!")
            else:
                messagebox.showinfo("RESULT", "OOPS!!!\nYOU GUESSED IT WRONG")
        if self.wordEntry.get() == self.c[self.i]:
            self.score += 10
            print(self.score)
            self.i += 1
            if self.i == 15:
                res = messagebox.showinfo('SCORE', 'Your Score : ' + str(self.score))
                exit()
            self.level['text'] = 'Level ' + str(self.i + 1)
            self.jumblewordLabel['text'] = self.L[self.i]
            self.wordEntry.delete(0, 'end')

        else:
            file = open('./score.txt', 'a')
            file.write(self.name + " : " + str(self.score) + '\n')
            res = messagebox.askquestion('SCORE', 'Your Score : ' + str(self.score) + "\n Play again?")
            if res == 'yes':
                self.root.destroy()
                self.setupUI()
            else:
                exit()
                file.close()


if __name__ == '__main__':
    g = Game()
    mainloop()
