from person import *
from loan import *
import random

class Account:
#superclass account used as base to create different accounts

    def __init__(self, accNum, accName, cardPin):
        #account name and account number needed to set up account
        self.accountNumber = accNum
        self.accountName = accName
        #starts with no money and 0 interest rate
        self.balance = 0
        self.interestRate = 0
        #security system to use 4 digit pin
        self.cardPin = cardPin
        self.loanList = []


    def getBalance(self):
        return self.balance

    def getInterestRate(self):
        return self.interestRate

    def getAccountName(self):
        return self.accountName

    def getLoanList(self):
        return self.loanList

    def applyInterest(self):
        #used for admins to manually apply the interest each day
        #simple interest = total * interest rate * years
        #1 day in years = 0.00273973
        interest = (self.getBalance() * self.getInterestRate()) * 0.002
        amountWithInterest = self.deposit(interest)


    def deposit(self, amount):
        #allows user to deposit money
        if amount > 0:
            print("$ %.2f deposited \n" %amount)
            self.balance += amount
        else:
            print("Deposit more than $0.00 only \n")


    def loanCharge(self, amount):
        #special case of withdraw used for admins to force loan payment
        self.balance -= amount


    def withdraw(self, amount, cardPin):
        #checks pin and if account has enough money before withdrawing money
        if amount < self.balance and self.checkCardPin(cardPin) == True:
            self.balance -= amount
            print("$ %.2f withdrawn \n" %amount)
        else:
            print("Invalid pin number or insufficent funds \n")


    def checkCardPin(self, cardPin):
        #checks if card pin entered matches from the accounts list
        if self.cardPin == cardPin:
            return True
        return False #else returns false


    def transferMoney(self, customer):
        #used to transfer money both between users and accounts
        #asks for amount user wants to transfer
        while True:
            try:
                amount = float(input("\nEnter amount to be transfered: "))
                break
            except ValueError:
                print("Option not valid. Try again. \n")
        #asks for account to transfer to then withdraws from account logged in
        #and deposits into the transfer to account
        transferTo = input("\nAccount name you want to send to: ")
        account = customer.searchAccountByName(transferTo)
        if account == None:
            print ("Account could not be found \n")
        else:
            #checks card pin to confirm payment
            cardPin = input("\nEnter card pin: ")
            self.withdraw(amount, cardPin)
            account.deposit(amount)
            print("You have transfered %.2f \n" %amount)


    def requestLoan(self, value):
        #used for requesting a loan under £10,000 with a 30% chance to get the loan
        if value > 10000:
            print("You can only request up to $10,000 \n")    #checks amount is less than £10,000
        else:
            #calculates the probability and gives a loan if its less than or equal to 0.3
            probability = random.random()
            if probability <= 0.3:
                #create loan
                name = input("\nName of loan: ")
                self.loanList.append(Loan(self, value, name))
            else:
                print("Sorry, your loan request has been refused")


    def searchLoansByName(self, loanName):
        #finds a loan from the loanList and compares with inputted data
        foundLoan = None
        for a in self.loanList:
            name = a.getLoanName()
            if name == loanName:
                foundLoan = a
                break
        if foundLoan == None:
            print("The loan %s does not exist! Try again...\n" %loanName)
        #returns the found_loan
        return foundLoan


    def accountMenu(self):
        #print the options you have
        print (" ")
        print ("Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Transfer money")
        print ("5) Apply for loan")
        print ("6) Loan Options")
        print ("7) Back")
        print (" ")
        while True:
            try:
                option = int(input ("\nChoose your option: "))
                break
            except ValueError:
                print("Option not valid. Try again. \n")
        return option


    def runAccountOptions(self, customer, bank_sys):
        loop = 1
        while loop == 1:
            choice = self.accountMenu()

            if choice == 1:
                #makes sure only floats are entered as straings cannot be deposited
                try:
                    amount = float(input("\nEnter amount to be deposited: "))
                    deposit = self.deposit(amount)
                except ValueError:
                    print("Option not valid. Try again. \n")

            elif choice == 2:
                #input pin and amount for withdraw function
                try:
                    amount = float(input("\nEnter amount to be withdrawn: "))
                    cardPin = input("\nEnter pin: ")
                    withdraw = self.withdraw(amount, cardPin)
                except ValueError:
                    print("Option not valid. Try again. \n")

            elif choice == 3:
                #prints the balance
                balance = self.getBalance()
                print("balance: %.2f \n" %balance)

            elif choice == 4:
                #checks name entered is a customer in the customer_list
                #then runs the transferMoney function
                transferName = input("\nEnter name of person to transfer to: ")
                name = bank_sys.searchCustomersByName(transferName)
                if name == None:
                    print ("User could not be found \n")
                else:
                    self.transferMoney(name)

            elif choice == 5:
                try:    #asks for amount to be loaned
                    value = float(input("\nEnter amount to be loaned: "))
                    self.requestLoan(value)
                except ValueError:
                    print("Option not valid. Try again. \n")

            elif choice == 6:
                loanName = input("\nName of loan: ")
                loanSearch = self.searchLoansByName(loanName)
                if loanSearch == None:
                    print ("Loan could not be found \n")
                else:
                    loanSearch.runLoanOptions(self)

            elif choice == 7:
                loop = 0

        print("Exit account operations \n")



class hesabjari(Account):
#main account type.

    def __init__(self, accNum, accName, cardPin, setupBalance = 0):
        super().__init__(accNum, accName, cardPin)
        self.accountType = "Current Account"     #name of account fixed variable
        self.balance = setupBalance  #used if amount stated. Otherwise default of 0.
        self.interestRate = 0.04


class hesabboland(Account):
#account for saving so higher interest rate

    def __init__(self, accNum, accName, cardPin, setupBalance = 0):
        super().__init__(accNum, accName, cardPin) #takes account number and account name from superclass
        self.accountType = "Savings"
        self.balance = setupBalance #default balance of 0
        self.interestRate = 0.06     #high interest rate as it is for saving


class hesabkotah(hesabjari):
#subclass of current account. Higher interest and recive a starting
#amount of money to get more users to use this account

    def __init__(self, accNum, accName, cardPin, setupBalance = 0):
        super().__init__(accNum, accName, cardPin, setupBalance)
        self.accountType = "Student"
        self.interestRate = 0.04
        self.balance += 100         #reward users with 100 starting money
