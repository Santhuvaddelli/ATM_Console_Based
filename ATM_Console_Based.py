import time , sys
class Customer:
    d = {}
    def __init__(self , name = '' , pin = '' , balance = 0):
        self.name = name
        self.balance = balance
        self.pin = pin
    
    def Account_Creation(self):
        self.name = input("Enter your name : ")
        self.pin = input("Set your pin : ")
        print("Please wait we will create your account : ")
        time.sleep(2)
        d[self.name] = self.pin
        print("Your account successfully created ")
    
    def Account_Deletion(self, name , pin):
        if len(d) != 0:
            print("Please wait we will delete your account")
            self.pin = input("Enter your pin to delete your account : ")
            if self.name in d:
                if d.get(self.name) == self.pin:
                    d.pop(self.name)
                    print("Account deleted successfully")
        else:
            print("First Create One after That you Delete")
            time.sleep(2)
    
    def Deposit(self , pin):
        if len(d) != 0:
            authenticate = input("Enter your pin : ")
            amt = float(input("Enter amount to Deposit : "))
            if d.get(self.name) == authenticate:
                self.balance = self.balance + amt
                print("Amount successfully deposited")
            else:
                print("Pin is incorrect")
                sys.exit()
        else:
            print("Create an Account First")
            time.sleep(2)

    def Withdraw(self , pin , balance):
        if len(d) != 0:
            if self.balance != 0:
                authenticate = input("Enter your pin : ")
                amt = float(input("Enter amount to Withdraw : "))
                if d.get(self.name) == authenticate:
                    if amt > self.balance:
                        print("Insufficient Funds")
                        sys.exit()
                    elif amt <= self.balance:
                        self.balance = self.balance - amt
                        print("Please wait transaction is in process")
                        time.sleep(3)
                        print("Money withdraw successfully")
                    else:
                        print("Please check once what you enter")
                else:
                    print("Pin is incorrect")
            else:
                print("First deposit some money to withdraw")
        else:
            print("Create a new account first")
            time.sleep(2)
            
    def Pin_Change(self , name , pin):
        if len(d) != 0:
            new_pin = input("Enter your new pin : ")
            if self.pin == d.get(self.name):
                d[self.name] = new_pin
                print("Pin Changed Successfully")
            else:
                print("Enter your old pin correctly")
        else:
            print("Create an Account First")
            time.sleep(2)
        
    def Balance_Enquiry(self , balance):
        if len(d) != 0:
            print("Wait we proceessing your transaction")
            time.sleep(3)
            print("Your current balance is : " , self.balance)
        else:
            print("Create an Account First")
            time.sleep(2)

def main():
    print("---------*Enter to World Bank*---------")
    c = Customer()
    while True:
        time.sleep(2)
        print("1. Account Creation")
        print("2. Account Deletion")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Pin Change")
        print("6. Balance Enquiry")
        print("7. Exit")
        option = int(input("Enter your option : "))
        if option == 1:
            print("Welcome to Our Bank")
            c.Account_Creation()
        elif option == 2:
            c.Account_Deletion(c.name , c.pin)
        elif option == 3:
            c.Deposit(c.pin)
        elif option == 4:
            c.Withdraw(c.pin , c.balance)
        elif option == 5:
            c.Pin_Change(c.name , c.pin)
        elif option == 6:
            c.Balance_Enquiry(c.balance)
        elif option == 7:
            print("Thanks for visiting our Bank")
            break
        else:
            print("Please Enter correct option")

if __name__ == '__main__':
    main()