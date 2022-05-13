from functools import partial
from tkinter import *
import tkinter as tk
import random
from tkinter import Y, Toplevel, messagebox
import gameColors as color
import dbServer as db


global board, userName

def start_game(game_board):
    global userName
    game_board.destroy()
    game_board = Tk()
    game_board.title("2048 Game")

    userWin = tk.Toplevel()
    userWin.title('Input Username')
    userWin.geometry("300x100")
    userWin.design = tk.Frame(
            userWin, bg = color.board_color, bd = 3, width = 600, height = 600, takefocus = True
        )
    userWin.resizable(False, False)
    userWin_frameL = tk.Frame(userWin, borderwidth = 1)
    userWin_frameL.place(relx = 0.5, rely = 0.6, anchor = "center")
    tk.Label(
        userWin,
        text = " Enter username: ",
        bg = color.youLose_bg,
        fg = color.gameOver_fontColor,
        font = color.userEntry_font
    ).pack()

    userEntry = Entry(userWin, width = 35, bd = 4)
    userEntry.pack()

    def getUserName():
        global userName
        if userEntry.get() == "":
            messagebox.showwarning("Input Invalid", "Please input a username")
        else:
            userName = userEntry.get()
            userWin.destroy()    

    userButton = Button(userWin, text = "Submit", command = getUserName, bd = 4)
    userButton.pack()

    class Game(tk.Frame):
        global mainGrid, scoreFrame, score
        def __init__(self):
            global mainGrid
            tk.Frame.__init__(self)
            self.grid()
            self.master.title("2048 Game")
        
            self.mainGrid = tk.Frame(
                self, bg = color.board_color, bd = 3, width = 600, height = 600
            )
            self.master.resizable(False, False)
            self.mainGrid.grid(pady = (110,0))
    
            self.GUI()
            self.startGame()
            
            self.master.bind("<Left>", self.left)
            self.master.bind("<Right>", self.right)
            self.master.bind("<Up>", self.up)
            self.master.bind("<Down>", self.down)
            self.master.bind("<a>", self.left)
            self.master.bind("<d>", self.right)
            self.master.bind("<w>", self.up)
            self.master.bind("<s>", self.down)

            db.connect()

            self.mainloop()

        def GUI(self):
            global scoreFrame, scoreLabel
            #Construct board
            self.tiles = []
            for i in range(4):
                row = []
                for j in range(4):
                    tileFrame = tk.Frame(
                        self.mainGrid,
                        bg = color.emptyTile_color,
                        width = 160,
                        height = 160
                    )
                    tileFrame.grid(row = i, column = j, padx = 5, pady = 5)
                    tileNum = tk.Label(self.mainGrid, bg = color.emptyTile_color)
                    tileData = {"frame":tileFrame, "number": tileNum}

                    tileNum.grid(row = i, column = j)
                    row.append(tileData)
                self.tiles.append(row)

            self.scoreFrame = tk.Frame(self)
            self.scoreFrame.place(relx=0.5, y = 60, anchor="center")
            tk.Label(
                self.scoreFrame,
                text = "SCORE",
                font = color.scoreLabel_font
            ).grid(row = 0)
            self.scoreLabel = tk.Label(self.scoreFrame, text = "0", font = color.score_font)
            self.scoreLabel.grid(row = 1)

        def startGame(self):
            #Initiate 4x4 matrix
            self.matrix = [[0] * 4 for _ in range(4)]

            #Summon 2 random-valued (2 or 4) tiles
            row = random.randint(0,3)
            col = random.randint(0,3)
            self.matrix[row][col] = 2
            self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
            self.tiles[row][col]["number"].configure(
                bg = color.tile_color[2],
                fg = color.tileNum_color[2],
                font = color.tileNum_font[2],
                text = "2"
            )
            while(self.matrix[row][col] != 0):
                row = random.randint(0,3)
                col = random.randint(0,3)
            self.matrix[row][col] = 2
            self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
            self.tiles[row][col]["number"].configure(
                bg = color.tile_color[2],
                fg = color.tileNum_color[2],
                font = color.tileNum_font[2],
                text = "2"
            )

            self.score = 0
        
        def merge(self):
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] != 0 and self.matrix[i][j] == self .matrix[i][j + 1]:
                        self.matrix[i][j] *= 2
                        self.matrix[i][j + 1] = 0
                        self.score += self.matrix[i][j]

        def shift(self):
            Matrix_1 = []
            for i in range(4):
                Matrix_1.append([])
                for j in range(4):
                    Matrix_1[i].append(self.matrix[i][3-j])
            self.matrix = Matrix_1
        
        def stack(self):
            Matrix_1 = [[0] * 4 for _ in range(4)]
            for i in range(4):
                fillPosition = 0
                for j in range(4):
                    if self.matrix[i][j] != 0:
                        Matrix_1[i][fillPosition] = self.matrix[i][j]
                        fillPosition += 1
            self.matrix = Matrix_1

        def transpose(self):
            Matrix_1 = [[0] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    Matrix_1[i][j] = self.matrix[j][i]
            self.matrix = Matrix_1

        def addRandomTile(self):
            tileOccupied = 0
            for i in range(4):
                for j in range(4):
                    tileValue = self.matrix[i][j]
                    if tileValue != 0:
                        tileOccupied += 1
            if tileOccupied != 16:
                row = random.randint(0,3)
                col = random.randint(0,3)
                while(self.matrix[row][col] != 0):
                    row = random.randint(0,3)
                    col = random.randint(0,3)
                self.matrix[row][col] = random.choice([2,4])
            else:
                messagebox.showinfo("Move Invalid", "Whoops! Try another!")

        def updateGUI(self):
            for i in range(4):
                for j in range(4):
                    tileValue = self.matrix[i][j]
                    if tileValue == 0:
                        self.tiles[i][j]["frame"].configure(bg = color.emptyTile_color)
                        self.tiles[i][j]["number"].configure(bg = color.emptyTile_color, text="")
                    else:
                        self.tiles[i][j]["frame"].configure(bg = color.tile_color[tileValue])
                        self.tiles[i][j]["number"].configure(
                            bg = color.tile_color[tileValue],
                            fg = color.tileNum_color[tileValue],
                            font = color.tileNum_font[tileValue],
                            text = str(tileValue)
                        )
            self.scoreLabel.configure(text = self.score)
            self.update_idletasks()
        
        def left(self, event):
            self.stack()
            self.merge()
            self.stack()
            self.addRandomTile()
            self.updateGUI()
            self.gameOver()

        def right(self, event):
            self.shift()
            self.stack()
            self.merge()
            self.stack()
            self.shift()
            self.addRandomTile()
            self.updateGUI()
            self.gameOver()

        def up(self, event):
            self.transpose()
            self.stack()
            self.merge()
            self.stack()
            self.transpose()
            self.addRandomTile()
            self.updateGUI()
            self.gameOver()

        def down(self, event):
            self.transpose()
            self.shift()
            self.stack()
            self.merge()      
            self.stack()
            self.shift()
            self.transpose()
            self.addRandomTile()
            self.updateGUI()
            self.gameOver()
        
        def possible_horizontalMove(self):
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        return True
            return False

        def possible_verticalMove(self):
            for i in range(3):
                for j in range(4):
                    if self.matrix[i][j] == self.matrix[i + 1][j]:
                        return True
            return False

        global gameOver_frame, gameOver_frameL

        def gameOver(self):
            global userName
            if any(2048 in row for row in self.matrix):
                global gameOver_frame, userName
                gameOver_frame = tk.Frame(self.mainGrid, borderwidth=2)
                gameOver_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
                tk.Label(
                    gameOver_frame,
                    text = "YOU WIN!! \n Check your progress 'L'",
                    bg = color.youWin_bg,
                    fg = color.gameOver_fontColor,
                    font = color.gameOver_font
                ).pack()
            elif not any(0 in row for row in self. matrix) and not self.possible_horizontalMove() and not self.possible_verticalMove():
                global gameOver_frameL
                gameOver_frame = tk.Frame(self.mainGrid, borderwidth =2)
                gameOver_frame.place(relx = 0.5, rely = 0.35, anchor = "center")
                tk.Label(
                    gameOver_frame,
                    text = " YOU LOSE!!! \n 'R' to try again ",
                    bg = color.youLose_bg,
                    fg = color.gameOver_fontColor,
                    font = color.gameOver_font
                ).pack()
                gameOver_frameL = tk.Frame(self.mainGrid, borderwidth = 2)
                gameOver_frameL.place(relx = 0.5, rely = 0.6, anchor = "center")
                tk.Label(
                    gameOver_frameL,
                    text = "   'L' to open \n Leaderboards   ",
                    bg = color.youLose_bg,
                    fg = color.gameOver_fontColor,
                    font = color.gameOver_font
                ).pack()
                db.submitScore(userName, self.score)
                self.master.bind("<r>", self.tryAgain)
                self.master.bind("<l>", self.leaderboards)
       
        def tryAgain(self, *args, **kwargs):
            self.matrix = [[0] * 4 for _ in range(4)]
            self.updateGUI()
            gameOver_frame.destroy()
            gameOver_frameL.destroy()
            
            #Summon 2 random-valued (2 or 4) tiles
            row = random.randint(0,3)
            col = random.randint(0,3)
            self.matrix[row][col] = 2
            self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
            self.tiles[row][col]["number"].configure(
                bg = color.tile_color[2],
                fg = color.tileNum_color[2],
                font = color.tileNum_font[2],
                text = "2"
            )
            while(self.matrix[row][col] != 0):
                row = random.randint(0,3)
                col = random.randint(0,3)
            self.matrix[row][col] = 2
            self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
            self.tiles[row][col]["number"].configure(
                bg = color.tile_color[2],
                fg = color.tileNum_color[2],
                font = color.tileNum_font[2],
                text = "2"
            )

            self.score = 0

            def showLeaderboards(self):
            leadList = db.displayScore()
            rankNum = 1
            yValue = 250
            for item in leadList:
                leadRank = tk.Label(self, text = rankNum, font = color.leaderItem_font)
                leadRank.place(relx = 0.15, y = yValue, anchor = "center")

                leadUser = tk.Label(self, text = item[0], font = color.leaderItem_font)
                leadUser.place(relx = 0.5, y = yValue, anchor = "center")

                leadScore = tk.Label(self, text = item[1], font = color.leaderItem_font)
                leadScore.place(relx = 0.85, y = yValue, anchor = "center")
                rankNum = rankNum + 1
                yValue = yValue + 60

        def leaderboards(self, *args):
            global score
            self.mainGrid.destroy()
            self.scoreLabel.destroy()
            self.grid()
            self.master.title("2048 Game")
            self.mainGrid = tk.Frame(
                self, bg = color.board_color, bd = 3, width = 600, height = 600
            )
            self.master.resizable(False, False)
            self.mainGrid.grid(pady = (110,0))
            scoreFrame = tk.Frame(self)
            scoreFrame.place(relx=0.5, y = 45, anchor="center")
            tk.Label(
                scoreFrame,
                text = "",
                font = color.scoreLabel_font
            ).grid(row = 0)
            self.scoreLabel = tk.Label(scoreFrame, text = 'LEADERBOARDS', font = color.leaderboard_font)
            self.scoreLabel.grid(row = 1)
            for i in range(250, 800, 90):
                leadItem_frame = tk.Frame(
                    self, bg = color.gameOver_fontColor, bd = 3, width = 600, height = 90)
                leadItem_frame.place(relx = 0.5, y = i, anchor = "center")
            for j in range(250, 745, 60):
                leadItem_frame = tk.Frame(
                    self, bg = color.emptyTile_color, bd = 3, width = 590, height = 50)
                leadItem_frame.place(relx = 0.5, y = j, anchor = "center")
            rankLabel = tk.Label(text = "Rank")
            rankLabel.place(x = 18, y = 120)
            rankLabel.config(font = color.leaderTitle_font, padx = 0)
            userLabel = tk.Label(text = "Username")
            userLabel.place(x = 155, y = 120)
            userLabel.config(font = color.leaderTitle_font, padx = 0)
            scoreLabel = tk.Label(text = "Score")
            scoreLabel.place(x = 420, y = 120)
            scoreLabel.config(font = color.leaderTitle_font, padx = 0)
            self.showLeaderboards()          
        
    def main():
        Game()

    if _name_ == "_main_":
        main()

def about():
    def openText():
        textFile = open("About.txt", 'r')
        text = textFile.read()

        aboutText.insert(END, text)
        textFile.close()

    aboutWin = tk.Toplevel()
    aboutWin.title("About")
    aboutWin.geometry("600x600")

    aboutText = tk.Text(aboutWin, fg = color.board_color, bg = "#fcefe6", width = 50, height = 50, font = color.userEntry_font, padx = 2, pady = 2)
    aboutText.pack()
    openText()


def main_screen():

    screen = Tk()
    screen.geometry("600x750")
    screen.configure(bg = "#fcefe6")
    start = partial(start_game, screen)

    #icon
    image_icon = PhotoImage(file="icon.png")
    screen.iconphoto(False,image_icon)
    screen.title("2048 Game")
    screen.resizable(False,False)

    lbltitle = Label(text = "2048 Game", font = color.gameOver_font, fg ='#695c57', bg = "#fcefe6")
    lbltitle.place(x = 90, y = 130)

    
    Button(screen, text = "Start", font = color.userEntry_font, height = 5, width = 20, bg = "#b8afa9", fg = "white", bd = 0, command = start).place(x = 187, y = 300)
    Button(screen, text = "About", font = color.userEntry_font, height = 5, width = 20, bg = "#b8afa9", fg = "white", bd = 0, command = about).place(x = 187, y = 440)


    screen.mainloop()

    
main_screen()
