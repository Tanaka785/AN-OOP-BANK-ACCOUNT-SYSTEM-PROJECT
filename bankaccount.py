# A BANK ACCOUNT SYSTEM

# Progress: 5. Transfer

import sys
import random


class Account:
    def __init__(self):
        self.balance = 0
        self.options1 = ["1. Create Account", "2. Quit"]
        self.options3 = [
            "1. Create Account",
            "2. Deposit money",
            "3. Withdraw money",
            "4. Check Balance",
            "5. Transfer money",
            "6. General statement",
            "7. Quit",
        ]
        self.options2 = ["1. Savings", "2. Checkings", "3. Credit", "4. Quit"]
        self.transfer_options = ["1. Savings", "2. Checkings"]

    # the method that prints the object.
    def __str__(self):
        return f"Account balance: ${self.balance:.2f}"

    # a method that returns the user to initially create an account
    def initial_options(self):
        while True:
            print("Main Menu")
            self.option = self.choose_option(self.options1)
            if self.option >= 1 and self.option < 3:
                return self.option
            elif self.option == False:
                pass
            else:
                print("Invalid option! Choose either '1' or '2'")

    # a method that prompts the user with the various options in the system e.g depositing money and returns the chosen option
    def second_options(self):
        while True:
            self.option = self.choose_option(self.options3)
            if self.option >= 1 and self.option < 8:
                return self.option
            elif self.option == False:
                pass
            else:
                print("Invalid option! Choose option in the range given![1 - 7]")

    # a method that prompts the user to choose which exact account they want to create.
    def third_options(self):
        while True:
            self.option = self.choose_option(self.options2)
            if self.option >= 1 and self.option < 5:
                return self.option
            elif self.option == False:
                pass
            else:
                print("Invalid option! Choose option in the range given![1 - 4]")

    # a method to validate and allow users to choose an option
    def choose_option(self, options):
        self.options = options
        print()
        for option in self.options:
            print(option)
        print()
        try:
            self.option = int(input("CHOOSE AN OPTION: ").strip())
            return self.option
        except ValueError:
            print("Please enter a valid integer value for the option!")
            return False

    # a method for allowing the user to deposit money into their account
    def deposit(self):
        while True:
            try:
                self.amount_to_deposit = float(
                    input("HOW MUCH DO YOU WANT TO DEPOSIT: ").strip()
                )
            except ValueError:
                print("Please enter a valid amount to deposit!")
            else:
                if self.amount_to_deposit < 1:
                    print("Deposit is only allowed from $1.00 and above! Try again..")
                else:
                    self.balance += self.amount_to_deposit
                    return self.balance

    # a method that allows users to withdraw money from their account
    def withdraw(self):
        while True:
            try:
                self.amount_to_withdraw = float(
                    input("HOW MUCH DO YOU WANT TO WITHDRAW: ").strip()
                )
            except ValueError:
                print("Please enter a valid amount to withdraw!")
            else:
                if self.amount_to_withdraw > self.balance:
                    print(
                        "Withdraw failed! Make sure you have enough funds in your account."
                    )
                else:
                    self.balance -= self.amount_to_withdraw
                    return self.balance
                
                
    # a method that allows the user to check their respective account balance
    def check_balance(self):
        return self.balance


    # a method that allows the transfer of money between the savings account and checkings account
    def get_transfer_details(self):
        while True:
            self.source_account = self.get_source_account()
            try:
                self.amount_to_transfer = float(
                    input("ENTER AMOUNT YOU WANT TO TRANSFER: ").strip()
                )
            except ValueError:
                print("Please enter a valid amount!")
            else:
                if (
                    self.amount_to_transfer > 0
                    and (self.balance) > self.amount_to_transfer
                ):
                    self.transfer_money(self.source_account, self.amount_to_transfer)
                    break
                else:
                    print(
                        "Please enter a value greater than $0.00. And also make sure you have sufficient funds in your account!"
                    )


    def transfer_money(self, source, amount):
        self.source_account = source 
        self.amount = amount 
        if self.source_account == 1:
            checkings.balance += self.amount
            savings.balance -= self.amount
            print(f"${self.amount:.2f} transfered successfuly from 'savings' to 'checkings'")
        elif self.source_account == 2:
            savings.balance += self.amount
            checkings.balance -= self.amount
            print(f"${self.amount:.2f} transferred successfully from 'checkings' to 'savings'")
        print()
        print("New balances: ")
        print(f"Savings: ${savings.balance:.2f}")
        print(f"Checkings: ${checkings.balance:.2f}")


    def choose_transfer_option(self):
        while True:
            print()
            for option in self.transfer_options:
                print(option)
            try:
                self.option = int(input("CHOOSE AN OPTION: "))
            except ValueError:
                print("Please enter a valid integer value for the option!")
            else:
                return (self.option)
        

    # a method to get the source account from the user
    def get_source_account(self):
        while True:
            print("CHOOSE THE SOURCE ACCOUNT TO TRANSFER MONEY FROM")
            self.source_account = self.choose_transfer_option()
            if self.validate_source_and_destination(self.source_account):
                return self.source_account

            
    # a method that validates the user's selected account to transfer/send money to.
    def validate_source_and_destination(self, choice):
        self.choice = choice
        if (self.choice) > 0 and (self.choice) < 3:
            return True
        else:
            print("Enter either '1' or '2'.")
            return False

    # a method to generate a general statement of the user's transactionss
    def general_statement(): ...

    
    def exit_program(self):
        sys.exit("Goodbye!👋")


class Savings_account(Account):
    def __init__(self):
        super().__init__()
        super().__str__()


class Checkings_account(Account):
    def __init__(self):
        super().__init__()
        super().__str__()


class Credit_account(Account):
    def __init__(self):
        super().__init__()
        super().__str__()

    def borrow_money(self):
        while True:
            try:
                self.amount_to_borrow = float(
                    input("HOW MUCH DO YOU WANT TO BORROW: ").strip()
                )
            except ValueError:
                print("Please enter a valid amount to borrow!")
            else:
                if self.amount_to_borrow < 1:
                    print("Borrowing is only allowed from $1.00 and above! Try again..")
                else:
                    self.balance += self.amount_to_borrow
                    return self.balance

    def payback_money(self): ...
    def check_credit_limit(self): ...
    def check_payment_due_date(self): ...


account = Account()
savings = Savings_account()
checkings = Checkings_account()
credit = Credit_account()


def main():
    options_1()


def options_1():
    # account = Account()
    option1 = account.initial_options()
    if option1 == 1:
        options_3(account)
    elif option1 == 2:
        account.exit_program()


def options_2(account):
    while True:
        option2 = account.second_options()
        if option2 == 1:
            options_3(account)
        elif option2 == 2:
            account.deposit()
            print("Deposit successful!")
            print(account)
        elif option2 == 3:
            account.withdraw()
            print("Withdraw successful!")
            print(account)
        elif option2 == 4:
            account.check_balance()
            print(account)
        elif option2 == 5:
            account.get_transfer_details()
        elif option2 == 6:
            ...
        elif option2 == 7:
            account.exit_program()


def options_3(account):
    option3 = account.third_options()
    if option3 == 1:
        print(savings)
        options_2(savings)
    elif option3 == 2:
        print(checkings)
        options_2(checkings)
    elif options_2 == 3:
        print(credit)
        ...
    elif option3 == 4:
        account.exit_program()


if __name__ == "__main__":
    main()
