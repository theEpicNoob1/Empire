import random
from tkinter import * 
from PIL import ImageTk, Image
import query

class Window():
    def __init__(self):
        self.grey = "#474747"
        self.gold = "#D4AF37"
        self.mainFont = ("Arial", 16)
        self.bigMainFont = ("Arial", 24)
        self.screeSize = (800, 600)
        self.playerNum = 0
        self.empireIDs = []
        self.round = 0
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("Empire")
        self.window.resizable(False,False)
        self.titleBackgroundImg = ImageTk.PhotoImage(Image.open("Images/titleScreen.png").resize(self.screeSize))
        self.manageAccountBackgroundImg = ImageTk.PhotoImage(Image.open("Images/manageAccount.png").resize(self.screeSize))
        self.modifyAccountBackgroundImg = ImageTk.PhotoImage(Image.open("Images/modifyAccount.png").resize(self.screeSize))
        self.teacherLeaderBoardImg = ImageTk.PhotoImage(Image.open("Images/teacherLeaderBoard.png").resize(self.screeSize))
        self.studentLeaderBoardImg = ImageTk.PhotoImage(Image.open("Images/studentLeaderBoard.png").resize(self.screeSize))
        self.addPlayerBackgroundImg = ImageTk.PhotoImage(Image.open("Images/addPlayers.png").resize(self.screeSize))
        self.playerTurnBackgroundImg = ImageTk.PhotoImage(Image.open("Images/playerTurn.png").resize(self.screeSize))
        self.empireListBackgroundImg = ImageTk.PhotoImage(Image.open("Images/empireList.png").resize(self.screeSize))
        self.winBackgroundImg = ImageTk.PhotoImage(Image.open("Images/win.png").resize(self.screeSize))
        self.backImg = ImageTk.PhotoImage(Image.open("Images/back.png").resize((300, 100)))
        self.loginScreen()

    def loginCheck(self, username, password):
        self.userData = query.userData((username, ))
        print(self.userData)
        if self.userData == None:
            print("Login failed, username does not exist")
        elif self.userData[2] == password:
            if self.userData[5] == "Student":
                self.studentScreen()
            else:
                self.teacherScreen()
        else:
            print("Login failed, username or password incorrect")

    def registerAccount(self, firstName, lastName, occupation, yearClass):
        query.registerAccount((firstName + " " + lastName, "12345678", firstName, lastName, occupation, yearClass, 0))
        print("Account registered")

    def removeAccount(self, accountID):
        query.removeAccount((accountID, ))
        print("Account removed")

    def changeUsername(self, newUsername):
        query.changeUsername((newUsername, self.userData[0]))
        print("Username changed")

    def changePassword(self, oldPassword, newPassword, confirmPassword):
        if oldPassword == self.userData[2]:
            if newPassword == confirmPassword:
                query.changePassword((newPassword, self.userData[0]))
                print("Password changed")
            else:
                print("New passwords do not match")
        else:
            print("Old password incorrect")

    def loginScreen(self):
        self.frame = Frame(self.window)
        
        backgroundImg = Label(self.frame, image = self.titleBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")
        
        usernameEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = self.mainFont)
        usernameEnt.place(x = 280, y = 360, anchor = CENTER)
        
        passwordEnt = Entry(self.frame, fg = "white", bg = "#474747", width = 15, font = self.mainFont, show = "*")
        passwordEnt.place(x = 520, y = 360, anchor = CENTER)

        loginBtn = Button(self.frame, text = "Login", fg = "white", bg = self.gold, width = 15, height = 1, font = self.bigMainFont, command = lambda: self.loginCheck(usernameEnt.get(), passwordEnt.get()))
        loginBtn.place(x = 400, y = 475, anchor = CENTER)
        
        self.frame.pack()

        self.window.mainloop()

    def teacherScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.teacherLeaderBoardImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        startGameBtn = Button(self.frame, text = "Start Game", fg = "white", bg = self.gold, width = 15, height = 1, font = self.mainFont, command = self.setPlayerNumScreen)
        startGameBtn.place(x = 200, y = 525, anchor = CENTER)

        manageAccountsBtn = Button(self.frame, text = "Manage Accounts", fg = "white", bg = self.gold, width = 15, height = 1, font = self.mainFont, command = self.manageAccountsScreen)
        manageAccountsBtn.place(x = 600, y = 525, anchor = CENTER)

        usernameBtn = Button(self.frame, text = self.userData[1], fg = self.gold, bg = "white", width = 15, height = 1, font = self.mainFont, command = self.modifyAccount)
        usernameBtn.place(x = 500, y = 50, anchor = CENTER)

        self.frame.pack()

    def studentScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.studentLeaderBoardImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        usernameBtn = Button(self.frame, text = self.userData[1], fg = self.gold, bg = "white", width = 15, height = 1, font = self.mainFont, command = self.modifyAccount)
        usernameBtn.place(x = 500, y = 50, anchor = CENTER)

        self.frame.pack()

    def modifyAccount(self):
        self.frame.destroy()

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.modifyAccountBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        oldPasswordEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont, show = "*")
        oldPasswordEnt.place(x = 325, y = 260, anchor = CENTER)

        newPasswordEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16), show = "*")
        newPasswordEnt.place(x = 325, y = 320, anchor = CENTER)

        confirmPasswordEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16), show = "*")
        confirmPasswordEnt.place(x = 325, y = 395, anchor = CENTER)

        changePasswordBtn = Button(self.frame, text = "Change password", fg = "white", bg = self.gold, width = 15, height = 1, font = ("Arial", 16), command = lambda: self.changePassword(oldPasswordEnt.get(), newPasswordEnt.get(), confirmPasswordEnt.get()))
        changePasswordBtn.place(x = 225, y = 475, anchor = CENTER)

        newUsernameEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = ("Arial", 16))
        newUsernameEnt.place(x = 615, y = 325, anchor = CENTER)

        changeUsernameBtn = Button(self.frame, text = "Change username", fg = "white", bg = self.gold, width = 15, height = 1, font = ("Arial", 16), command = lambda: self.changeUsername(newUsernameEnt.get()))
        changeUsernameBtn.place(x = 615, y = 400, anchor = CENTER)

        if self.userData[5] == "Student":
            backBtn = Button(self.frame, text = "Back", fg = "white", bg = "white", width = 325, height = 100, font = self.mainFont, image = self.backImg, command = self.studentScreen)
            backBtn.place(x = 625, y = 525, anchor = CENTER)
        else:
            backBtn = Button(self.frame, text = "Back", fg = "white", bg = "white", width = 325, height = 100, font = self.mainFont, image = self.backImg, command = self.teacherScreen)
            backBtn.place(x = 625, y = 525, anchor = CENTER)

        self.frame.pack()

    def manageAccountsScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window)
        
        backgroundImg = Label(self.frame, image = self.manageAccountBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        firstNameEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = self.mainFont)
        firstNameEnt.place(x = 320, y = 260, anchor = CENTER)

        lastNameEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = self.mainFont)
        lastNameEnt.place(x = 320, y = 315, anchor = CENTER)

        occupationEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = self.mainFont)
        occupationEnt.place(x = 320, y = 370, anchor = CENTER)

        yearClassEnt = Entry(self.frame, fg = "white", bg = self.grey, width = 15, font = self.mainFont)
        yearClassEnt.place(x = 320, y = 425, anchor = CENTER)

        registerBtn = Button(self.frame, text = "Register", fg = "white", bg = self.gold, width = 10, height = 1, font = self.mainFont, command = lambda: self.registerAccount(firstNameEnt.get(), lastNameEnt.get(), occupationEnt.get(), yearClassEnt.get()))
        registerBtn.place(x = 225, y = 525, anchor = CENTER)

        accountIDEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
        accountIDEnt.place(x = 615, y = 325, anchor = CENTER)

        removeAccountBtn = Button(self.frame, text = "Remove", fg = "white", bg = self.gold, width = 10, height = 1, font = self.mainFont, command = lambda: self.removeAccount(accountIDEnt.get()))
        removeAccountBtn.place(x = 615, y = 400, anchor = CENTER)

        backBtn = Button(self.frame, text = "Return", fg = "white", bg = "white", width = 325, height = 100, font = self.mainFont, image = self.backImg, command = self.teacherScreen)
        backBtn.place(x = 625, y = 525, anchor = CENTER)

        self.frame.pack()

    def setPlayerNumScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.addPlayerBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        playerNumLbl = Label(self.frame, text = "Number of players(5-9)", fg = self.gold, bg = self.grey, width = 20, height = 1, font = self.mainFont)
        playerNumLbl.place(x = 400, y = 300, anchor = CENTER)

        playerNumEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
        playerNumEnt.place(x = 400, y = 375, anchor = CENTER)

        nextBtn = Button(self.frame, text = "Next", fg = "white", bg = self.gold, width = 15, height = 1, font = self.mainFont, command = lambda: self.setPlayerNameScreen(playerNumEnt.get()))
        nextBtn.place(x = 400, y = 450, anchor = CENTER)

        self.frame.pack()

    def setPlayerNameScreen(self, playerNum):
        self.playerNum = int(playerNum)
        self.frame.destroy()

        usernameEntList = []
        fakeNameEntList = []

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.addPlayerBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        for i in range(self.playerNum):
            playerNumLbl = Label(self.frame, text = f"Player {i+1} username", fg = "white", bg = self.grey, width = 15, height = 1, font = self.mainFont)
            playerNumLbl.place(x = 200, y = i * 32 + 190, anchor = CENTER)

        for i in range(self.playerNum):
            playerNumEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
            playerNumEnt.place(x = 400, y = i * 32 + 190, anchor = CENTER)
            usernameEntList.append(playerNumEnt)

        for i in range(self.playerNum):
            fakeNameEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
            fakeNameEnt.place(x = 600, y = i * 32 + 190, anchor = CENTER)
            fakeNameEntList.append(fakeNameEnt)

        redHerringLbl = Label(self.frame, text = "Red herring", fg = "white", bg = self.grey, width = 15, height = 1, font = self.mainFont)
        redHerringLbl.place(x = 200, y = self.playerNum * 32 + 190, anchor = CENTER)

        redHerringEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
        redHerringEnt.place(x = 600, y = self.playerNum * 32 + 190, anchor = CENTER)
        fakeNameEntList.append(redHerringEnt)

        nextBtn = Button(self.frame, text = "Next", fg = "white", bg = self.gold, width = 15, height = 1, font = self.mainFont, command = lambda: self.initialisation(usernameEntList, fakeNameEntList))
        nextBtn.place(x = 400, y = 540, anchor = CENTER)

        self.frame.pack()

    def initialisation(self, usernameList, fakeNameList):
        self.usernameList = []
        for i in usernameList:
            self.usernameList.append(i.get())
        self.fakeNameList = []
        for i in fakeNameList:
            self.fakeNameList.append(i.get())
        random.shuffle(self.fakeNameList)

        query.initialiseGame((self.userData[0], ))
        self.gameData = query.gameData((self.userData[0], ))
        query.initialiseEmpire(self.usernameList, self.gameData[0])
        self.empireData = query.empireData((self.gameData[0], ))
        for i in self.empireData:
            self.empireIDs.append(i[0])
        query.initialisePlayers(self.usernameList, self.fakeNameList, self.gameData[0], self.empireIDs)
        self.playerData = query.playerData((self.gameData[0], ))

        self.displayFakeNamesScreen()

    def displayFakeNamesScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window, width = 800, height = 600, bg = self.grey)

        Label(self.frame, text = "Fake names", fg = self.gold, bg = self.grey, width = 15, height = 1, font = ("Arial", 24)).place(x = 400, y = 50, anchor = CENTER)

        for i in range(len(self.fakeNameList)):
            fakeNameLbl = Label(self.frame, text = f"{self.fakeNameList[i]}", fg = "white", bg = self.grey, width = 15, height = 1, font = self.mainFont)
            fakeNameLbl.place(x = 400, y = i * 45 + 100, anchor = CENTER)

        nextBtn = Button(self.frame, text = "Next", fg = "white", bg = self.gold, width = 15, height = 1, font = self.mainFont, command = self.playerTurnScreen)
        nextBtn.place(x = 400, y = 550, anchor = CENTER)

        self.frame.pack()

    def playerTurnScreen(self):
        self.round += 1

        self.frame.destroy()

        self.frame = Frame(self.window)

        if self.round == 1:
            self.playerGuessing = random.choice(self.usernameList)  

        backgroundImg = Label(self.frame, image = self.playerTurnBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        Label(self.frame, text = f"{self.playerGuessing}", fg = self.gold, bg = self.grey, width = 15, height = 1, font = ("Arial", 30)).place(x = 400, y = 125, anchor = CENTER)

        usernameGuessEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
        usernameGuessEnt.place(x = 500, y = 210, anchor = CENTER)

        fakeNameGuessEnt = Entry(self.frame, fg = "black", bg = "white", width = 15, font = self.mainFont)
        fakeNameGuessEnt.place(x = 500, y = 310, anchor = CENTER)

        submitBtn = Button(self.frame, text = "Submit", fg = "white", bg = self.gold, width = 16, height = 2, font = self.bigMainFont, command = lambda: self.guessResultScreen(usernameGuessEnt.get(), fakeNameGuessEnt.get()))
        submitBtn.place(x = 400, y = 525, anchor = CENTER)

        self.frame.pack()

    def guessResultScreen(self, usernameGuess, fakeNameGuess):
        self.frame.destroy()

        self.frame = Frame(self.window, width = 800, height = 600, bg = self.grey)

        fakeName = query.checkGuess(usernameGuess)[0]
        if fakeName == fakeNameGuess:
            self.guessResult = True
        else:
            self.guessResult = False

        if self.guessResult:
            Label(self.frame, text = "CORRECT", fg = self.gold, bg = self.grey, width = 15, height = 1, font = ("Arial", 30)).place(x = 400, y = 250, anchor = CENTER)
            empireID = query.empireID((self.playerGuessing, ))[0]
            query.updateEmpires(empireID, usernameGuess)
            query.removeEmpire((usernameGuess, ))
        else:
            Label(self.frame, text = "INCORRECT", fg = self.gold, bg = self.grey, width = 15, height = 1, font = ("Arial", 30)).place(x = 400, y = 250, anchor = CENTER)
            self.playerGuessing = usernameGuess

        nextBtn = Button(self.frame, text = "Next", fg = "white", bg = self.gold, width = 15, height = 1, font = self.bigMainFont, command = self.empireListScreen)
        nextBtn.place(x = 400, y = 500, anchor = CENTER)

        self.frame.pack()

    def empireListScreen(self):
        self.frame.destroy()

        self.frame = Frame(self.window)

        backgroundImg = Label(self.frame, image = self.empireListBackgroundImg)
        backgroundImg.pack(side = "bottom", fill = "both", expand = "yes")

        empireData = query.empireData((self.gameData[0], ))
        print(empireData)
        for i in range(len(empireData)):
            empireName = query.empireName((empireData[i][0], ))
            playersInEmpire = query.playersInEmpire((empireData[i][0], ))
            Label(self.frame, text = f"{empireName[0]}", fg = self.gold, bg = self.grey, width = 15, height = 1, font = self.mainFont).place(x = 100, y = i * 35 + 150, anchor = CENTER)
            Label(self.frame, text = f"{playersInEmpire}", fg = "white", bg = self.grey, width = 30, height = 1, font = self.mainFont).place(x = 200, y = i * 35 + 150, anchor = W)
            print(empireName)
            print(playersInEmpire)

        nextBtn = Button(self.frame, text = "Next", fg = "white", bg = self.gold, width = 15, height = 1, font = self.bigMainFont, command = self.playerTurnScreen)
        nextBtn.place(x = 400, y = 500, anchor = CENTER)

        self.frame.pack()


if __name__ == "__main__":
    Window()