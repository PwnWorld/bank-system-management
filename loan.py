#datetime imported for loans to be repaid within a set time
from datetime import datetime, timedelta
from account import *

class Loan:

    def __init__(self, account, value, name):
        self.account = account
        self.loanValue = value
        #from current time, user has 30 days to repay the loan
        self.loanDueDate = datetime.now() + timedelta(days=30)
        self.amountToRepay = value
        self.loanName = name
        self.account.deposit(value)


    def getLoanValue(self):
        return self.loanValue


    def getLoanName(self):
        return self.loanName


    def getDueDate(self):
        return self.loanDueDate


    def getAmountToRepay(self):
        return self.amountToRepay

    def getTimeRemaining(self):
        #if the loan is due, calcuation for how long left is not
        if self.loanDueDate == 0:
            return 0
        else:
            return (self.loanDueDate - datetime.now()).total_seconds()


    def loanReport(self):
        #prints amount left to pay
        remaining = self.amountToRepay
        print("\n$%.2f remaining" %remaining)

        #prints how many days are left
        if self.loanDueDate == 0:
            print("Loan repaid")
        else:
            #converts to seconds and does a calculation with this
            secondsRemaining = (self.loanDueDate - datetime.now()).total_seconds()
            #sec * min * hour = 60*60*24 = 86400
            daysRemaining = secondsRemaining / 86400
            print("\n%.0f days remaining" %daysRemaining)


    def repayLoan(self, amount, cardPin, account):
        #withdraw money from users account to pay loan
        if self.amountToRepay >= amount and account.checkCardPin(cardPin) == True:
            account.withdraw(amount, cardPin)
            self.amountToRepay -= amount
            if self.getAmountToRepay() == 0:
                self.loanDueDate = 0


    def loanMenu(self):
        #print the options you have
        print()
        print ("Your loan options are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) View loan report")
        print ("2) Pay loan")
        print ("3) Quit")
        print (" ")
        while True:
            try:
                option = int(input("\nChoose your option: "))
                break
            except ValueError:
                print("Option not valid. Try again. \n")
        return option

    def runLoanOptions(self, account):
        loop = 1
        while loop == 1:
            choice = self.loanMenu()

            if choice == 1:
                self.loanReport()

            if choice == 2:
                try:
                    amount = float(input("\nEnter amount to be repaid: "))
                    cardPin = input("\nEnter card pin: ")
                    self.repayLoan(amount, cardPin, account)
                except ValueError:
                    print("Option not valid. Try again. \n")

            if choice == 3:
                loop = 0

        print("Exit loan operations \n")
