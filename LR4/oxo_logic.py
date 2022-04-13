import os, random
import oxo_data 

class game():
    def __init__(player):
        player.board = list(" " * 9)
    
    def newGame(player):
        ' return new empty game '
        return list(" " * 9)

    def saveGame(player, play):
        ' save game to disk '
        oxo_data.saveGame(player.board)

    def restore(player):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            player.board = oxo_data.restoregame()
            if len(player.board) != 9:
                player.board = list(" " * 9)
            return player.board
        except IOError:
            player.board = list(" " * 9)
            return player.board

    def _generateMove(player):
        ''' generate a random cell from those available.
        If all cells are used return -1'''
        options = [i for i in range(len(player.board)) if player.board[i] == " "]
        if options:
            return random.choice(options)
        else: return -1

    def _isWinningMove(player):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
        game = player.board
        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(player,cell):
        if player.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            player.board[cell] = 'X'
        if player._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(player):
        cell = player._generateMove()
        if cell == -1:
            return 'D'
        player.board[cell] = 'O'
        if player._isWinningMove():
            return 'O'
        else:
            return ""

def test():
    result = ""
    play = game()
    while not result:
        print(play.board)
        try:
            result = play.userMove(play._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = play.computerMove()
        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
    print(play.board)
        
if __name__ == "__main__":
    test()