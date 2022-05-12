#CPE106L - Project (2048 game)
#Server and database functions used in CPE106L Project Sprint 3

import sqlite3

#Connect to the database
def connect():
    db = sqlite3.connect("gameLeaderboards.db")
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS gameLeaderboards ( 
    user TEXT NOT NULL, userScore INT NOT NULL); """)
    db.commit()
    db.close()
    
#Input usernames and scores to the database
def submitScore(aUserName, aScore):
    db = sqlite3.connect("gameLeaderboards.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO gameLeaderboards (user, userScore) VALUES (?,?)", (aUserName, aScore))
    db.commit()
