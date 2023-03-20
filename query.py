import sqlite3

def userData(record):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("SELECT * FROM Account WHERE Username=?", (record,))
        product = cursor.fetchone()
        return product
    
def registerAccount(record):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("INSERT INTO Account(Username, Password, Firstname, Lastname, Occupation, YearClass, Score) VALUES (?, ?, ?, ?, ?, ?, ?)", record)
        db.commit()

def removeAccount(record):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("DELETE FROM Account WHERE AccountID=?", record)
        db.commit()

def changeUsername(record):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("UPDATE Account SET Username=? WHERE AccountID=?", record)
        db.commit()

def changePassword(record):
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("UPDATE Account SET Password=? WHERE AccountID=?", record)
        db.commit()

def createEmpiresTable():
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = """CREATE TABLE Empires
            (EmpireID integer,
            EmpireName text,
            primary key(EmpireID))"""
        cursor.execute(sql)
        db.commit()

def createPlayersTable():
    with sqlite3.connect("empire.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = """CREATE TABLE Players
            (PlayerID integer,
            PlayerName text,
            Score integer,
            EmpireID integer,
            primary key(PlayerID),
            foreign key(EmpireID) references Empires(EmpireID)
            on update cascade on delete set null)"""
        cursor.execute(sql)
        db.commit()
        

if __name__ == "__main__":
    createEmpiresTable()
    createPlayersTable()