import tkinter as tk
import random
import gameColors as color

class Game(tk.Frame):
   
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game")
 
        self.mainGrid = tk.Frame(
            self, bg = color.board_color, bd = 3, width = 600, height = 600
        )
        self.mainGrid.grid(pady = (110,0))
 
        self.GUI()
        self.startGame()
 
        self.mainloop()
  
  
  

def main():
    Game()

if __name__ == "__main__":
    main()
