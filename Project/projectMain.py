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
        
