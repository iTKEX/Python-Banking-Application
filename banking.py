# --------------------- IMPORTS ---------------------#
import csv

# --------------------- CONSTANTS ---------------------#
welcome = """
================================
🏦 Hello to you're Python Bank!
================================"""

sign_in = """
===========================================
                SIGN IN
==========================================="""

sign_up = """
===========================================
                SIGN UP
==========================================="""

transactions = """
===========================================
                TRANSACTIONS
==========================================="""

fieldnames = [
    "id",
    "first_name",
    "last_name",
    "password",
    "checking",
    "savings",
    "active",
    "overdraft_count",
]

# --------------------- TO DO --------------------- #
"""
Customer can add money:
    - Customer can add money to saving
    - Customer can add money to checking

"""

# --------------------- Checker FUNCTIONS ---------------------#


# --------------------- Menus ---------------------#
def start_menu():
    session = True
    while session:
        print(welcome)
        print(
            "Please choose from below.\n1. SIGN UP\n2. Log in to your account.\n3. Quit"
        )
        user_input = input("\nPlease Enter your choice as a number: ")
        match user_input:
            case "1":
                print("\n")
                result = bank.sign_up_account()
                if result:
                    session = Transactions.transactions_menu()
            case "2":
                print("\n")
                result = bank.sign_in_account()
                if result:
                    Transactions.transactions_menu()
            case "3":
                print("\n")
                session = None
            case _:
                print("Please enter a valid choice")
                continue


def check_user_accounts(customer):
    user_options = ["1", "2", "3"]
    user_input = None
    if customer.checking == "False" and customer.savings == "False":
        while user_input not in user_options:
            print("You don't have any account")
            print("You can create checking, saving or Both")
            print("1. For both\n2. For Checking\n3. For Saving")
            user_input = input("You Want account Please Choice")
            match user_input:
                case "1":
                    customer.checking = 0
                    customer.savings = 0
                    return "transactions_menu"
                case "2":
                    customer.checking = 0
                    return "transactions_menu"
                case "3":
                    customer.savings = 0
                    return "transactions_menu"
    elif customer.checking == "False":
        while user_input not in user_options:
            print("")
            print("You can create checking, saving or Both")
            print("1. For both\n2. For Checking\n3. For Saving")
            user_input = input("You Want account Please Choice")
            match user_input:
                case "1":
                    customer.checking = 0
                    customer.savings = 0
                    return "transactions_menu"
                case "2":
                    customer.checking = 0
                    return Transactions.transactions_menu()
                case "3":
                    customer.savings = 0
                    return Transactions.transactions_menu()
    elif customer.savings == "False":
        pass


def transactions_menu():
    customer = Customer(**Bank.current_user)
    user_options = ["1", "2", "3", "q"]
    user_input = None
    while user_input not in user_options:
        print("\n\n", transactions)
        print(f"Hello {customer.first_name} {customer.last_name}")
        result = customer.check_user_accounts()
        if result == "transactions_menu":
            print(
                "Which Account you want to access.\n\n1. Checking account.\n2. Saving account\n3. Log out"
            )

            user_input = input("\nPlease Enter your choice as a number: ")

            if user_input not in user_options:
                print("Please enter a valid choice")

            match user_input:
                case "1":
                    break  # run function return withdraw()
                case "2":
                    break
                case "3":
                    Bank.current_user = None
                    return "main"


# --------------------- Customer Class ---------------------#
class Customer:

    def __init__(
        self,
        id,
        first_name,
        last_name,
        password,
        savings=False,
        checking=False,
        active=True,
        overdraft_count=0,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = checking
        self.savings = savings
        self.active = active
        self.overdraft_count = overdraft_count


# --------------------- Bank Class ---------------------#
class Bank:
    accounts = []
    current_user = None
    csv_file_path = "assets/bank.csv"

    def __init__(self):
        pass

    def load_accounts():
        with open(Bank.csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            accounts = [row for row in reader]
            # if current_user:
        Bank.accounts = accounts

    def sign_up_account(self):
        user_first_name = user_last_name = user_password = None
        while not user_first_name or not user_last_name or not user_password:
            print(sign_up)
            print("Please Enter your credintals:\n or quit: 'q'")
            user_first_name = input("Please Enter your first name: ").strip()
            if user_first_name.lower() == "q":
                return
            user_last_name = input("Please Enter your last name: ").strip()
            if user_last_name.lower() == "q":
                return
            user_password = input("Please Enter your password: ").strip()
            if user_password.lower() == "q":
                return
            if not user_first_name or not user_last_name or not user_password:
                print("All fields are required. Try again.\n")

        ids = []
        for account in Bank.accounts:
            id = account.get("id")
            ids.append(int(id))
        ids = max(ids)
        new_id = ids + 1

        new_account = Customer(new_id, user_first_name, user_last_name, user_password)

        with open(Bank.csv_file_path, "a") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(vars(new_account))
        Bank.load_accounts()

    def sign_in_account(self):
        while True:
            print(sign_in)
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


# --------------------- Transactions Class ---------------------#
class Transactions:
    # customer = Customer(**Bank.current_user)
    def __init__(self):
        pass


# ------------------------- VARIABLES ------------------------#
bank = Bank()


# --------------------- FUNCTIONS ---------------------#
def init():
    # this is the entry point
    Bank.load_accounts()
    start_menu()


init()
