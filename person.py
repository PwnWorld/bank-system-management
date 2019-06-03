from account import *


class Person:
    #base to create people (admins and customers)

    def __init__(self, name, password, address = [None, None, None, None]):
        self.name = name
        self.password = password
        self.address = address

    def getAddress(self):
        return self.address

    def updateAddress(self, address):
        #used to update addresss by storing address list
        self.address = address

    def getName(self):
        return self.name

    def updateName(self, name):
        self.name = name

    def printDetails(self):
        print("Name %s:" %self.name)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])
        print()


    def checkPassword(self, password):
        if self.password == password:
            return True
        return False #else returns false


    def profileSettingsMenu(self):
        #print the options you have
         print ()
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Update address")
         print ("3) Print details")
         print ("4) Back")
         print ()
         while True:
             try:
                 option = int(input ("\nChoose your option: "))
                 break
             except ValueError:
                 print("Option not valid. Try again. \n")
         return option


    def runProfileOptions(self):
        loop = 1
        while loop == 1:
            choice = self.profileSettingsMenu()

            if choice == 1:
                #updates name
                while True:
                    try:
                        name = str(input("\nEnter new name: "))
                        break
                    except ValueError:
                        print("Names must include letters only. Try again. \n")
                self.updateName(name)

            elif choice == 2:
                #change address by inputing new 1 in each line
                address = self.address
                self.address[0] = input("\nPlease enter new address:\n        ")
                self.address[1] = input("        ")
                self.address[2] = input("        ")
                self.address[3] = input("        ")
                self.updateAddress(address) #uses update_address function with data inputted

            elif choice == 3:
                #prints a customers details
                self.printDetails()

            elif choice == 4:
                loop = 0





class Customer(Person):

    def __init__(self, name, password, address = [None, None, None, None]):
        #gets name, password and address from Person class
        super().__init__(name, password, address)
        self.account = []


    def openAccount(self, account):
    #creating customer accounts as a list to allow customers to have multiple accounts
        self.account.append(account)


    def getAccountList(self):
        return self.account


    def searchAccountByName(self, accountName):
        foundAccount = None
        #goes through accounts_list to check the data inputed matches
        for a in self.account:
            name = a.getAccountName()
            if name == accountName:
                foundAccount = a
                break
        if foundAccount == None:
            print("The account %s does not exist! Try again...\n" %accountName)
        return foundAccount



class Admin(Person):

    def __init__(self, name, password, fullRights, address = [None, None, None, None]):
        super().__init__(name, password, address)
        self.fullAdminRights = fullRights

    def hasFullAdminRight(self):
        return self.fullAdminRights
