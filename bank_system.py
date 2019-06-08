#link to other classes by importing
from person import *
from account import *
#import needed libaries
import pickle
import tkinter as tk
from tkinter import messagebox


class BankSystem(object):

    def __init__(self):
        self.customerList = []
        self.adminList = []
        self.loadBankData()     #used to received bank data when testing
        self.save()    #saves loadBankData into a file
        self.load()    #loads bank data from a file


    def save(self):
        #put customer and admin list into another list
        data1 = (self.adminList, self.customerList)
        #makes a file and writes bank data into it
        output = open('bankData.pkl', 'wb')
        pickle.dump(data1, output)
        output.close()


    def load(self):
        #loads bank data from another file, then closes that file
        pkl_file = open('bankData.pkl', 'rb')
        data = pickle.load(pkl_file)
        pkl_file.close()
        #set the admin and customer list
        self.adminList = data[0]
        self.customerList = data[1]


    def loadBankData(self):
        #create customers and add them to the cusomterList
        #create specific accounts for customers
        #used to reset data when testing
        customer_1 = Customer("amin", "1234", ["14", " Street2", "tabriz" , "hesabjari"])
        account_no = 90455673
        account_1 = hesabjari(account_no, "hesabjari", "1234", 5000)
        customer_1.openAccount(account_1)
        self.customerList.append(customer_1)


        customer_2 = Customer("Davood", "password", ["60", "Street1", "tehran" , "hesabboland"])
        account_no += 1
        account_2 = hesabjari(account_no, "hesabjari", "2601", 3200)
        account_no += 1
        account_3 = hesabboland(account_no, "hesabboland", "2601", 600)
        customer_2.openAccount(account_2)
        customer_2.openAccount(account_3)
        self.customerList.append(customer_2)


        customer_3 = Customer("Niloo", "moonlight", ["5", "Street3", "tabriz", "hesabkotah"])
        account_no += 1
        account_4 = hesabkotah(account_no, "hesabkotah", "1010", 18000)
        customer_3.openAccount(account_4)
        self.customerList.append(customer_3)


        customer_4 = Customer("Ali", "150A",["44", "nishan tashi", "istanbul", "hesabjari"])
        account_no+= 1
        account_5 = hesabjari(account_no, "hesabjari", "6666", 50)
        customer_4.openAccount(account_5)
        self.customerList.append(customer_4)


        #create admins and add them to admins_list
        admin_1 = Admin("ahora", "1441", True, ["12", "maqsodiye", "tehran" , ""])
        self.adminList.append(admin_1)


    def customerLogin(self, name, password):
        #check the data inputed
        foundCustomer = self.searchCustomersByName(name)
        if foundCustomer == None:
            return("The customer has not been found! \n")
        else:
        #make sure the correct password is entered
            if (foundCustomer.checkPassword(password) == True):
                self.runCustomerOptions(foundCustomer)
            else:
                 return("you have input a wrong password \n")


    def searchCustomersByName(self, customerName):
        #finds a customer from the customers_list and compares wuth inputted data
        foundCustomer = None
        for a in self.customerList:
            name = a.getName()
            if name == customerName:
                foundCustomer = a
                break
        if foundCustomer == None:
            print("The customer %s does not exist! Try again...\n" %customerName)
        #returns the found_customer to be used customer_login
        return foundCustomer


    def mainMenu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the EN Simple Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Customer login")
        print ("3) Quit")
        print (" ")
        while True:
            try:
                option = int(input("\nChoose your option: "))
                break
            except ValueError:
                print("Option not valid. Try again. \n")
        return option


    def runMainOption(self):
        #options when code first runs
        loop = 1
        while loop == 1:
            choice = self.mainMenu()

            if choice == 1:
                name = input("\nPlease input admin name: ")
                password = input("\nPlease input admin password: ")
                #calls admin_login to check the data inputted
                msg = self.adminLogin(name, password)
                print(msg)

            elif choice == 2:
                name = input("\nPlease input customer name: ")
                password = input("\nPlease input customer password: ")
                #calls customer_login to check data inputted
                msg = self.customerLogin(name, password)
                print(msg)

            elif choice == 3:
                #uses a GUI for a message box to confirm if the user wants to quit
                root = tk.Tk()
                if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
                    root.destroy()    #gets rid of blank GUI box the tkinter makes
                    self.save()    #saves all changes
                    loop = 0    #quits
            else:
                print("Option not valid \n")
        print ("Thank you for stopping by the bank! \n")


    def customerMenu(self, customerName):
        #print the options you have when logged in as a customer
         print (" ")
         print ("Welcome %s : Your transaction options are:" %customerName)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Account operations")
         print ("2) Profile settings")
         print ("3) Sign out")
         print (" ")
         while True:
             try:
                 option = int(input("\nChoose your option: "))
                 break
             except ValueError:
                 print("Option not valid. Try again.")
         return option


    def runCustomerOptions(self, customer):
        loop = 1
        while loop == 1:
            choice = self.customerMenu(customer.getName())

            if choice == 1:
                accName = input("\nPlease input name of account: ")
                account = customer.searchAccountByName(accName)
                if account == None:
                    print ("Account could not be found \n")
                else:
                    account.runAccountOptions(customer, self)

            elif choice == 2:
                customer.runProfileOptions()

            elif choice == 3:
                loop = 0
        print ("Exit account operations \n")


    def adminLogin(self, name, password):
        #checks admin login same as for customers
        foundAdmin = self.searchAdminByName(name)
        if foundAdmin== None:
            return("The admin has not been found! \n")
        else:
            if (foundAdmin.checkPassword(password) == True):
                self.runAdminOptions(foundAdmin)
            else:
                 return("you have input a wrong password \n")


    def searchAdminByName(self, adminName):
        #searchs for admins using admin list
        foundAdmin = None
        for a in self.adminList:
            name = a.getName()
            if name == adminName:
                foundAdmin = a
                break
        if foundAdmin == None:
            print("The admin %s does not exist! Try again...\n" %adminName)
        return foundAdmin


    def interest(self):
        #allows admins to manually apply interest to all accounts
        for customer in self.customerList:
            for account in customer.getAccountList():
                account.applyInterest()
                print("Interest applied to %s" %account.getAccountName()) #used for testing


    def overdueLoanCharge(self):
        #admins need check for overdue loans daily and charge each day
        for customer in self.customerList:
            for account in customer.getAccountList():
                for loan in account.getLoanList():
                    if loan.getTimeRemaining() < 0:
                        amount = 4 #charges £4 per day
                        account.loanCharge(amount)
                        print("%s loan charged £4 daily fee" %loan) #used for testing
                    else:
                        print("No overdue loans")


    def adminMenu(self, adminName):
        #print the options you have when logged in as an admin
         print (" ")
         print ("Welcome Admin %s : Available options are:" %adminName)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Customer account operations")
         print ("2) Customer profile settings")
         print ("3) Admin profile settings")
         print ("4) Delete customer")
         print ("5) Print all customers detail")
         print ("6) Print all admins detail")
         print ("7) Overdue loan charge")
         print ("8) Interest")
         print ("9) Sign out")
         print (" ")
         while True:
             try:
                 option = int(input ("\nChoose your option: "))
                 break
             except ValueError:
                 print("Option not valid. Try again. \n")
         return option


    def runAdminOptions(self, admin):
        #options for admin_menu
        loop = 1
        while loop == 1:
            choice = self.adminMenu(admin.getName())

            if choice == 1:
                #name the customer whose data your changing. Brings you to transaction options
                customerName = input("\nPlease input customer name: ")
                customer = self.searchCustomersByName(customerName)
                if customer != None:
                    accName = input("\nPlease input name of account: ")
                    account = customer.searchAccountByName(accName)
                    if account == None:
                        print ("Account could not be found \n")
                    else:
                        account.runAccountOptions(customer, self)

            elif choice == 2:
                #name customer whose data your changing. Uses run_profile_options from Person class for customer
                customerName = input("\nPlease input customer name: ")
                customer = self.searchCustomersByName(customerName)
                if customer != None:
                    customer.runProfileOptions()

            elif choice == 3:
                #uses run_profile_options from Person class for admin
                admin.runProfileOptions()

            elif choice == 4:
                #finds customer to delete if admin has rights. Else, prints a statement that the admin can't.
                if admin.hasFullAdminRight() == True:
                    customerName = input("\nPlease input customer name you want to delete : ")
                    customerAccount = self.searchCustomersByName(customerName)
                    if customerAccount != None:
                        #uses a GUI for a message box to confirm
                        root = tk.Tk()
                        if messagebox.askyesno("Delete User", "Are you sure?"):
                            root.destroy()    #gets rid of blank GUI box the tkinter makes
                            self.customerList.remove(customerAccount)
                            print("\n%s has been removed from the bank system." %customer_name)
                            print("All changes are saved when you quit the bank system.")
                else:
                    print("Only administrators with full admin rights can remove a customer from the bank system!\n")

            elif choice == 5:
                self.printAllCustomersDetails()

            elif choice == 6:
                if admin.hasFullAdminRight() == True:
                    self.printAllAdminsDetails()
                else:
                    print("Only administrators with full admin rights can view admin details!\n")

            elif choice == 7:
                self.overdueLoanCharge()

            elif choice == 8:
                self.interest()

            elif choice == 9:
                #leaves the loop and prints an exit statement
                loop = 0
        print ("Exit account operations \n")


    def printAllCustomersDetails(self):
            #list related operation
            i = 0
            for c in self.customerList:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.printDetails()
                print("------------------------")


    def printAllAdminsDetails(self):
            #list related operation
            i = 0
            for a in self.adminList:
                i+=1
                print('\n %d. ' %i, end = ' ')
                a.printDetails()
                print("------------------------")




#runs run_main_option from BankSystem class
app = BankSystem()
app.runMainOption()
