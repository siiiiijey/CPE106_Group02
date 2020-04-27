from breezypythongui import EasyFrame
from bank import Bank, createBank

class ATM(EasyFrame):

    def __init__(self, bank):

        EasyFrame.__init__(self, title = "ATM")
        self.bank = bank
        self.account = None
        self.nameLabel = self.addLabel(row = 0, column = 0,
                                       text = "Name")
        self.pinLabel = self.addLabel(row = 1, column = 0,
                                      text = "PIN")
        self.amountLabel = self.addLabel(row = 2, column = 0,
                                         text = "Amount")
        self.statusLabel = self.addLabel(row = 3, column = 0,
                                         text = "Status")
        self.nameField = self.addTextField(row = 0, column = 1,
                                           text = "")
        self.pinField = self.addTextField(row = 1, column = 1,
                                          text = "")
        self.amountField = self.addFloatField(row = 2, column = 1,
                                              value = 0.0)
        self.statusField = self.addTextField(row = 3, column = 1,
                                             text = "Welcome to the Bank!",
                                             state = "readonly")
        self.balanceButton = self.addButton(row = 0, column = 2,
                                            text = "Balance",
                                            command = self.getBalance,
                                            state = "disabled")
        self.depositButton = self.addButton(row = 1, column = 2,
                                            text = "Deposit",
                                            command = self.deposit,
                                            state = "disabled")
        self.withdrawButton = self.addButton(row = 2, column = 2,
                                             text = "Withdraw",
                                             command = self.withdraw,
                                             state = "disabled")
        self.loginButton = self.addButton(row = 3, column = 2,
                                          text = "Login",
                                          command = self.login)
 
    def login(self):
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.account:
            self.statusField.setText("Hello, " + name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.loginButton["text"] = "Logout"
            self.loginButton["command"] = self.logout
        else:
            self.statusField.setText("Name and pin not found!")
            
    def logout(self):
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Welcome to the Bank!")
        self.balanceButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.loginButton["text"] = "Login"
        self.loginButton["command"] = self.login

    def getBalance(self):
        text = "Balance = $" + str(self.account.getBalance())
        self.statusField.setText(text)

    def deposit(self):
        amount = self.amountField.getNumber()
        message = self.account.deposit(amount)
        if not message:
            self.statusField.setText("Deposit successful")
        else:
           self.statusField.setText(message)
        
    def withdraw(self):
        amount = self.amountField.getNumber()
        message = self.account.withdraw(amount)
        if not message:
            self.statusField.setText("Withdrawal successful")
        else:
           self.statusField.setText(message)
        
def main(fileName = None):
    if not fileName:
        bank = createBank(5)
    else:
        bank = Bank(fileName)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == "__main__":
    main()
