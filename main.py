import tkinter as tk
import query

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Empire")
        self.returnBtn = tk.Button()
        self.registerBtn = tk.Button()
        self.removeAccountBtn = tk.Button()
        self.changePasswordBtn = tk.Button()
        self.loginScreen()

    def loginCheck(self, username, password):
        self.userData = query.userData(username)
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
        self.window.configure(bg="grey")

        self.titlelbl = tk.Label(self.window, fg = "yellow", bg = "grey", text = "Empire", font = ("Arial", 32))
        self.titlelbl.pack(pady=75)

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2, 3, 4], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        usernameLbl = tk.Label(self.frame, text = "Username", fg = "white", bg = "grey", width = 20, height = 1, font = ("Arial", 16))
        usernameLbl.grid(row = 0, column = 0, pady = 10)
        usernameEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 20, font = ("Arial", 16))
        usernameEnt.grid(row = 1, column = 0, pady = 5)
        passwordLbl = tk.Label(self.frame, text = "Password", fg = "white", bg = "grey", width = 20, height = 1, font = ("Arial", 16))
        passwordLbl.grid(row = 2, column = 0, pady = 10)
        passwordEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 20, font = ("Arial", 16), show = "*")
        passwordEnt.grid(row = 3, column = 0, pady = 5)
        loginBtn = tk.Button(self.frame, text = "Login", fg = "white", bg = "blue", width = 10, height = 1, font = ("Arial", 16), command = lambda: self.loginCheck(usernameEnt.get(), passwordEnt.get()))
        loginBtn.grid(row = 4, column = 0, pady = 20)
        self.frame.pack()

        self.window.mainloop()

    def teacherScreen(self):
        self.returnBtn.destroy()
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        startGameBtn = tk.Button(self.frame, text = "Start Game", fg = "white", bg = "Green", width = 15, height = 1, font = ("Arial", 16), command = self.setPlayerNumScreen)
        startGameBtn.grid(row = 0, column = 0, pady = 10)
        leaderBoardBtn = tk.Button(self.frame, text = "Leader Board", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = self.teacherLeaderBoardScreen)
        leaderBoardBtn.grid(row = 1, column = 0, pady = 10)
        manageAccountsBtn = tk.Button(self.frame, text = "Manage Accounts", fg = "white", bg = "red", width = 15, height = 1, font = ("Arial", 16), command = self.manageAccountsScreen)
        manageAccountsBtn.grid(row = 2, column = 0, pady = 10)
        self.frame.pack()

    def teacherLeaderBoardScreen(self):
        self.frame.destroy()
        
        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.teacherScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT)

    def manageAccountsScreen(self):
        self.removeAccountBtn.destroy()
        self.registerBtn.destroy()
        self.returnBtn.destroy()
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        registerAccountBtn = tk.Button(self.frame, text = "Register Account", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = self.registerAccountScreen)
        registerAccountBtn.grid(row = 0, column = 0, pady = 10)
        removeAccountBtn = tk.Button(self.frame, text = "Remove Account", fg = "white", bg = "red", width = 15, height = 1, font = ("Arial", 16), command = self.removeAccountScreen)
        removeAccountBtn.grid(row = 1, column = 0, pady = 10)
        self.frame.pack()

        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.teacherScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT)

    def registerAccountScreen(self):
        self.returnBtn.destroy()
        self.frame.destroy()
        
        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2, 3], weight = 1)
        self.frame.columnconfigure([0, 1], weight = 1)
        
        firstNameLbl = tk.Label(self.frame, text = "First name", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        firstNameLbl.grid(row = 0, column = 0, pady = 10)
        firstNameEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        firstNameEnt.grid(row = 0, column = 1, pady = 10)
        lastNameLbl = tk.Label(self.frame, text = "Last name", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        lastNameLbl.grid(row = 1, column = 0, pady = 10)
        lastNameEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        lastNameEnt.grid(row = 1, column = 1, pady = 10)
        occupationLbl = tk.Label(self.frame, text = "Occupation", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        occupationLbl.grid(row = 2, column = 0, pady = 10)
        occupationEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        occupationEnt.grid(row = 2, column = 1, pady = 10)
        yearClassLbl = tk.Label(self.frame, text = "Year and class", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        yearClassLbl.grid(row = 3, column = 0, pady = 10)
        yearClassEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        yearClassEnt.grid(row = 3, column = 1, pady = 10)
        self.frame.pack()
        
        self.registerBtn = tk.Button(self.window, text = "Register", fg = "white", bg = "Red", width = 10, height = 1, font = ("Arial", 16), command = lambda: self.registerAccount(firstNameEnt.get(), lastNameEnt.get(), occupationEnt.get(), yearClassEnt.get()))
        self.registerBtn.pack(pady = 20)
        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.manageAccountsScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT)

    def removeAccountScreen(self):
        self.returnBtn.destroy()
        self.frame.destroy()
        
        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1], weight = 1)
        self.frame.columnconfigure(0, weight = 1)
        
        accountIDLbl = tk.Label(self.frame, text = "Account ID", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        accountIDLbl.grid(row = 0, column = 0, pady = 10)
        accountIDEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        accountIDEnt.grid(row = 1, column = 0, pady = 10)
        self.frame.pack()
        
        self.removeAccountBtn = tk.Button(self.window, text = "Remove", fg = "white", bg = "Red", width = 10, height = 1, font = ("Arial", 16), command = lambda: self.removeAccount(accountIDEnt.get()))
        self.removeAccountBtn.pack(pady = 20)
        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.manageAccountsScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT)

    def studentScreen(self):
        self.changePasswordBtn.destroy()
        self.returnBtn.destroy()
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        leaderBoardBtn = tk.Button(self.frame, text = "Leader Board", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = self.studentLeaderBoardScreen)
        leaderBoardBtn.grid(row = 0, column = 0, pady = 10)
        changeUsernameBtn = tk.Button(self.frame, text = "Change username", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = self.changeUsernameScreen)
        changeUsernameBtn.grid(row = 1, column = 0, pady = 10)
        changePasswordBtn = tk.Button(self.frame, text = "Change password", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = self.changePasswordScreen)
        changePasswordBtn.grid(row = 2, column = 0, pady = 10)
        self.frame.pack()

    def changeUsernameScreen(self):
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        newUsernameLbl = tk.Label(self.frame, text = "New username", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        newUsernameLbl.grid(row = 0, column = 0, pady = 10)
        newUsernameEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        newUsernameEnt.grid(row = 1, column = 0, pady = 10)
        changeUsernameBtn = tk.Button(self.frame, text = "Change username", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = lambda: self.changeUsername(newUsernameEnt.get()))
        changeUsernameBtn.grid(row = 2, column = 0, pady = 10)
        self.frame.pack()

        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.studentScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT) 

    def changePasswordScreen(self):
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1, 2], weight = 1)
        self.frame.columnconfigure([0, 1], weight = 1)

        oldPasswordLbl = tk.Label(self.frame, text = "Old password", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        oldPasswordLbl.grid(row = 0, column = 0, pady = 10)
        oldPasswordEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16), show = "*")
        oldPasswordEnt.grid(row = 0, column = 1, pady = 10)
        newPasswordLbl = tk.Label(self.frame, text = "New password", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        newPasswordLbl.grid(row = 1, column = 0, pady = 10)
        newPasswordEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16), show = "*")
        newPasswordEnt.grid(row = 1, column = 1, pady = 10)
        confirmPasswordLbl = tk.Label(self.frame, text = "Confirm password", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        confirmPasswordLbl.grid(row = 2, column = 0, pady = 10)
        confirmPasswordEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16), show = "*")
        confirmPasswordEnt.grid(row = 2, column = 1, pady = 10)
        self.frame.pack()

        self.changePasswordBtn = tk.Button(self.window, text = "Change password", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = lambda: self.changePassword(oldPasswordEnt.get(), newPasswordEnt.get(), confirmPasswordEnt.get()))
        self.changePasswordBtn.pack(pady = 20)
        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.studentScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT) 

    def studentLeaderBoardScreen(self):
        self.frame.destroy()

        self.returnBtn = tk.Button(self.window, text = "Return", fg = "white", bg = "blue", width = 5, height = 2, font = ("Arial", 16), command = self.studentScreen)
        self.returnBtn.pack(padx = 20, side = tk.RIGHT)

    def setPlayerNumScreen(self):
        self.frame.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.configure(bg = "grey")
        self.frame.rowconfigure([0, 1], weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        playerNumLbl = tk.Label(self.frame, text = "Number of players", fg = "white", bg = "grey", width = 15, height = 1, font = ("Arial", 16))
        playerNumLbl.grid(row = 0, column = 0, pady = 10)
        playerNumEnt = tk.Entry(self.frame, fg = "black", bg = "white", width = 15, font = ("Arial", 16))
        playerNumEnt.grid(row = 0, column = 1, pady = 10)
        nextBtn = tk.Button(self.frame, text = "Next", fg = "white", bg = "blue", width = 15, height = 1, font = ("Arial", 16), command = lambda: self.setPlayerNameScreen(playerNumEnt.get()))
        nextBtn.grid(row = 1, column = 0, pady = 10)
        self.frame.pack()

    def setPlayerNameScreen(self, playerNum):
        pass


if __name__ == "__main__":
    Window()