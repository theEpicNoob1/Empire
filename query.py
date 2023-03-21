import sqlite3

def userData(username):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("SELECT * FROM Account WHERE Username=?", username)
        userData = cursor.fetchone()
        return userData
    
def registerAccount(accountData):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("INSERT INTO Account(Username, Password, Firstname, Lastname, Occupation, YearClass, Score, GamesPlayed, GamesWon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", accountData)
        db.commit()

def removeAccount(accountID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("DELETE FROM Account WHERE AccountID=?", accountID)
        db.commit()

def changeUsername(userData):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("UPDATE Account SET Username=? WHERE AccountID=?", userData)
        db.commit()

def changePassword(userData):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("UPDATE Account SET Password=? WHERE AccountID=?", userData)
        db.commit()

def initialiseGame(hostID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("INSERT INTO Games(HostID) VALUES (?)", hostID)
        db.commit()

def gameData(hostID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("SELECT * FROM Games WHERE HostID=?", hostID)
        gameData = cursor.fetchone()
        return gameData
    
def initialiseEmpire(usernames, gameID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        for username in usernames:
            cursor.execute("INSERT INTO Empires(EmpireName, GameID) VALUES (?, ?)", (username, gameID))
            db.commit()

def empireData(gameID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("SELECT * FROM Empires WHERE GameID=?", gameID)
        empireData = cursor.fetchall()
        return empireData

def initialisePlayers(usernames, fakeNames, gameID, empireID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        for i in range(len(usernames)):
            cursor.execute("INSERT INTO Players(PlayerName, FakeName, Score, GameID, EmpireID) VALUES (?, ?, ?, ?, ?)", (usernames[i], fakeNames[i], 0, gameID, empireID[i]))
            db.commit()

def playerData(gameID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("SELECT * FROM Players WHERE GameID=?", gameID)
        playerData = cursor.fetchall()
        return playerData

def removeGame(gameID):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("DELETE FROM Games WHERE GameID=?", gameID)
        db.commit()

def createGamesTable():
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = """CREATE TABLE Games
            (GameID integer,
            HostID integer,
            primary key(GameID))"""
        cursor.execute(sql)
        db.commit()

def createEmpiresTable():
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = """CREATE TABLE Empires
            (EmpireID integer,
            EmpireName text,
            GameID integer,
            primary key(EmpireID),
            foreign key(GameID) references Games(GameID)
            on update cascade on delete cascade)"""
        cursor.execute(sql)
        db.commit()

def createPlayersTable():
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = """CREATE TABLE Players
            (PlayerID integer,
            PlayerName text,
            FakeName text,
            Score integer,
            GameID integer,
            EmpireID integer,
            primary key(PlayerID),
            foreign key(EmpireID) references Empires(EmpireID)
            on update cascade on delete cascade)"""
        cursor.execute(sql)
        db.commit()

if __name__ == "__main__":
    #data = ("NoobMaster69", 12345, "Paul", "Jennings", "Teacher", "Teacher", 0, 0, 0)
    #registerAccount(data)
    #createGamesTable()
    #createEmpiresTable()
    #createPlayersTable()
    #removeGame((1, ))
    pass