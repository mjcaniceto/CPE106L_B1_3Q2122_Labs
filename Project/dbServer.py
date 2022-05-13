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
 
#Get data from the database in descending order as to get a sorted list
def displayScore():
    db = sqlite3.connect("gameLeaderboards.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM gameLeaderboards ORDER BY userScore DESC LIMIT 9")
    values = cursor.fetchall()
    db.close()
    return values

#Delete the table from the database 
def delete():
    db = sqlite3.connect("gameLeaderboards.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS gameLeaderboards")
    db.close()
