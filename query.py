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

if __name__ == "__main__":
    data = ("Jennings", "1234", "Paul", "Jennings", "Teacher", "Teacher", 0)
    registerAccount(data)