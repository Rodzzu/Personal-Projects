import random

class BankAccount:
    def __init__(self, first_name, last_name, password, acc_num, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.accnum = acc_num
        self.balance = balance

    def account(self):
        return self.accnum

    def deposit(self, amount, password):
        if password == self.password:
            self.balance += amount
            print(f"Deposited {amount} into account {self.accnum}\nCurrent Balance: {self.balance}")
        else:
            print("Incorrect password. Deposit operation failed.")

    def withdraw(self, amount, password):
        if password == self.password:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.accnum}\nCurrent Balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect password. Withdrawal operation failed.")

    def check_balance(self, password):
        if password == self.password:
            print(f"Account number: {self.accnum}\nBalance: {self.balance}")
        else:
            print("Incorrect password. Balance inquiry failed.")

    def change_password(self, current_password, new_password):
        if current_password == self.password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect current password. Password change failed.")

def main():
    acc_list = []
    while True:
        print("Welcome to the Artuz Bank!")
        print("What is your inquiry?")
        print("Open an Account [1]")
        print("Deposit [2]")
        print("Withdraw [3]")
        print("Balance Inquiry [4]")
        print("Change Password [5]")
        print("Exit [6]")

        choice = input("Enter your choice: ")

        if choice == '1':
            fn = input("Enter your first name: ")
            ln = input("Enter your last name: ")
            pw = input("Enter the password you'd like to use: ")
            accnum = random.randint(1000, 10000)
            account = BankAccount(fn, ln, pw, accnum)
            acc_list.append(account)
            print(f"Account opened successfully!\nYour Account Number is: {accnum}")
        elif choice == '2':
            accnum = int(input("Enter your account number: "))
            amount = int(input("Enter the amount to deposit: "))
            password = input("Enter your password: ")
            for acc in acc_list:
                if accnum == acc.accnum:
                    acc.deposit(amount, password)
                    break
            else:
                print("Account Number does not exist!")
        elif choice == '3':
            accnum = int(input("Enter your account number: "))
            amount = int(input("Enter the amount to withdraw: "))
            password = input("Enter your password: ")
            for acc in acc_list:
                if accnum == acc.accnum:
                    acc.withdraw(amount, password)
                    break
            else:
                print("Account Number does not exist!")
        elif choice == '4':
            accnum = int(input("Enter your account number: "))
            password = input("Enter your password: ")
            for acc in acc_list:
                if accnum == acc.accnum:
                    acc.check_balance(password)
                    break
            else:
                print("Account Number does not exist!")
        elif choice == '5':
            accnum = int(input("Enter your account number: "))
            current_password = input("Enter your current password: ")
            new_password = input("Enter your new password: ")
            for acc in acc_list:
                if accnum == acc.accnum:
                    acc.change_password(current_password, new_password)
                    break
            else:
                print("Account Number does not exist!")
        elif choice == '6':
            print("Exiting the program, Goodbye!")
            break

main()
