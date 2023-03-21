import sqlite3

def createTable(name, tableName, sql):
    with sqlite3.connect(name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE name=?", (tableName,))
        result = cursor.fetchall()
        keepTable = True

        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(tableName))

            if response == "y":
                keepTable = False
                print("The {0} table will be recreated - all existing data will be lost".format(tableName))
                cursor.execute("Drop table if exists {0}".format(tableName))
                db.commit()
            else:
                print("The existing table was kept")

        else:
            keepTable = False
        
        if not keepTable:
            cursor.execute(sql)
            db.commit()

def createAccountTable():
    sql = """CREATE TABLE Account
            (AccountID integer,
            Username text,
            Password text,
            Firstname text,
            Lastname text,
            Occupation text,
            YearClass text,
            Score integer,
            GamesPlayed integer,
            GamesWon integer,
            primary key(AccountID))"""
    createTable(db_name, "Account", sql)

if __name__ == "__main__":
    db_name = "empire.db"
    createAccountTable()