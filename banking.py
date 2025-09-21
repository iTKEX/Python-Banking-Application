"""
pseudo code:

Create Bank Class
- define Users
# define Accounts
    add all accounts to the array

- define log in to user account

- create withdrow
Types of accounts:
    - Checking Account
    - Saving Account"""

# --------------------- IMPORTS ---------------------#
import csv


# --------------------- Bank Class ---------------------#
class Bank:
    accounts = []
    current_user = None

    def __init__(self):
        pass

    def load_accounts():
        csv_file_path = "assets/bank.csv"
        with open(csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            accounts = [row for row in reader]
        Bank.accounts = accounts

    def sign_in_account(self):
        while True:
            print(
                """
===========================================
                SIGN IN
==========================================="""
            )
            print("Please Enter your credintals:\n if you want to back enter 'q'")
            user_id = input("Please Enter your ID: ")
            if user_id == "q":
                return False
            user_password = input("Please enter your password: ")
            result = Bank.check_sign_in_credintals(user_id, user_password)
            if result is not False:
                return True
            else:
                print("Please Enter valid credintals")
            

    def check_sign_in_credintals(id, password):
        for account in Bank.accounts:
            if account.get("id") == id and account.get("password") == password:
                Bank.current_user = account
                return True
        return False


# ------------------------- VARIABLES ------------------------#
bank = Bank()


# --------------------- FUNCTIONS ---------------------#


def start_menu():
    while True:
        print(
            """
================================
🏦 Hello to you're Python Bank!
================================"""
        )

        print("Please choose from below.\n1. Log in to your account.\n2. Quit")
        user_input = input("\nPlease Enter your choice as a number: ")
        match user_input:
            case "1":
                print("\n")
                result = bank.sign_in_account()
                if result:
                    customer_menu()
            case "2":
                print("\n")
                break
            case _:
                print("Please enter a valid choice")
                continue


def customer_menu():
    while True:
        print(f'\n\nHello {Bank.current_user.get("first_name")} {Bank.current_user.get("last_name")}'
        )

        print("Please choose from below.\n1. Withdraw Money.\n2. Deposite Money\n3. Log out")
        user_input = input("\nPlease Enter your choice as a number: ")
        match user_input:
            case "1":
                print("\n")
                print("\n")
                break
            case "3":
                Bank.current_user = None
                break
            case _:
                print("Please enter a valid choice")
                continue


def init():
    # this is the entry point
    Bank.load_accounts()
    start_menu()


init()
