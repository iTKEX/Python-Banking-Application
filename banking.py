"""
TABLE OF CONTENT:
- IMPORTS
- CONSTANTS
- Customer Class
- Bank Class
- Transactions Class
- init()
"""

# --------------------- IMPORTS ---------------------#
import csv

# --------------------- CONSTANTS ---------------------#
welcome = """
===================================
🏦 Hello to you're Python Bank! 🐍
==================================="""

sign_in = """
===========================================
                SIGN IN 🔑
==========================================="""

sign_up = """
===========================================
                SIGN UP 📝
==========================================="""

transactions = """
===========================================
                TRANSACTIONS 💱
==========================================="""

transfer = """
===========================================
           ⬇️ TRANSFER MONEY ⬆️
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

# --------------------- Customer Class ---------------------#
class Customer:
    '''
    Customer class if for init each customer in Bank
    '''
    def __init__(
        self,
        id,
        first_name,
        last_name,
        password,
        checking=False,
        savings=False,
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
    '''
    Handle Bank accounts proccess and information
    '''
    accounts = []
    current_user = None
    csv_file_path = "assets/bank.csv"

    # load accounts from csv file to list
    def load_accounts():
        with open(Bank.csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            accounts = [row for row in reader]
        Bank.accounts = accounts

    #create new account and add it to csv
    def sign_up_account():
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

        # create new id for new account
        ids = []
        for account in Bank.accounts:
            id = account["id"]
            ids.append(int(id))
        ids = max(ids)
        new_id = ids + 1

        new_account = Customer(new_id, user_first_name, user_last_name, user_password)

        # write new user information to the csv file
        with open(Bank.csv_file_path, "a") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(vars(new_account))
        Bank.load_accounts()

    # sign in user by asking for credintals
    def sign_in_account():
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
    # check the user credintals
    def check_sign_in_credintals(id, password):
        for account in Bank.accounts:
            if account["id"] == id and account["password"] == password:
                Bank.current_user = account
                return True
        return False
    
    # save the changes on account to the csv file
    def save_accounts():
        with open(Bank.csv_file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in Bank.accounts:
                writer.writerow(account)

    # log out current user account
    def log_out():
        Bank.current_user = None
        return None


# --------------------- Transactions Class ---------------------#
class Transactions:
    '''
    Handle all porject transactions
    '''
    account_type = None

    def __init__(self):
        pass

    def transactions_menu(customer):
        user_options = ["1", "2", "3","4", "5","6"]
        user_input = None
        user_choise = None
        while user_input not in user_options:
            print("\n\n", transactions)
            print(f"Hello {customer['first_name']} {customer['last_name']}")
            result = Transactions.check_user_accounts(customer)
            if result == "select_account_menu":
                Transactions.select_account_menu(customer)
            elif result == "transactions_menu":
                while user_choise != "6":
                    print(transactions)
                    print("1. Check your account balance \n2. Add money\n3. Withdraw money\n4. Transfer money\n5. Change account\n6. log out")
                    user_choise = input("Please choose what you need\t")
                    match user_choise:
                        case "1":
                            Transactions.check_balance(customer)
                        case "2":
                            Transactions.add_money(customer)
                        case "3":
                            Transactions.check_balance(customer)
                            Transactions.withdraw_money(customer)
                            Transactions.is_active(customer)
                        case "4":
                            Transactions.transfer_money_menu(customer)
                        case "5":
                            Transactions.check_user_accounts(customer)
                            Transactions.select_account_menu(customer)
                        case "6":
                            Bank.log_out()
                            return None
    # menu to make user choose which account he want to deal with
    def select_account_menu(customer):
        user_options = ["1", "2", "3"]
        user_input = None
        while user_input not in user_options:
            print(transactions)
            print("Which Account you want to access")
            print("1. Saving account \n2. Checking account\n3. log out")
            user_input = input("Which account you want to access \t")
            match user_input:
                case "1":
                    Transactions.account_type = "savings"
                    return "transactions_menu"
                case "2":
                    Transactions.account_type = "checking"
                    return "transactions_menu"
                case "3":
                    Bank.log_out()
                    return None

    # check user account types
    def check_user_accounts(customer):
        user_options = ["1", "2", "3"]
        user_input = None
        if customer["checking"] == "False" and customer["savings"] == "False":
            while user_input not in user_options:
                print("You don't have any account")
                print("You can create checking, saving or Both")
                print("1. For both\n2. For Checking\n3. For Saving")
                user_input = input("Which account you want to create Please Choose\t")
                match user_input:
                    case "1":
                        customer["checking"] = 0
                        customer["savings"] = 0
                        Bank.save_accounts()
                        return "transactions_menu"
                    case "2":
                        customer["checking"] = 0
                        Bank.save_accounts()
                        return "transactions_menu"
                    case "3":
                        customer["savings"] = 0
                        Bank.save_accounts()
                        return "transactions_menu"
        elif customer["checking"] != "False" and customer["savings"] == "False":
            while user_input not in user_options:
                print(
                    "You have only checking account You want access it or create Saving account?"
                )
                print(
                    "1. Access Checking account \n2. Create saving account and access it\n3. log out"
                )
                user_input = input("Please enter your choice \t")
                match user_input:
                    case "1":
                        Transactions.account_type = "checking"
                        return "transactions_menu"
                    case "2":
                        customer["savings"] = 0
                        Bank.save_accounts()
                        Transactions.account_type = "savings"
                        return "transactions_menu"
                    case "3":
                        Bank.log_out()
                        return None
        elif customer["savings"] != "False" and customer["checking"] == "False":
            while user_input not in user_options:
                print(
                    "You have only Saving account You want access it or create Checking account?"
                )
                print(
                    "1. Access Saving account \n2. Create Checking account and access it\n3. log out"
                )
                user_input = input("Please Choose option \t")
                match user_input:
                    case "1":
                        Transactions.account_type = "savings"
                        return "transactions_menu"
                    case "2":
                        customer["checking"] = 0
                        Bank.save_accounts()
                        Transactions.account_type = 'checking'
                        return "transactions_menu"
                    case "3":
                        Bank.log_out()
                        return None
        else:
            return "transactions_menu"
        
    # check for user current balance
    def check_balance(customer):
        print(f"Your current balance is : {customer[Transactions.account_type]}$")
        if int(customer['overdraft_count']) == 2:
                customer['active'] = "False"
                Bank.save_accounts()
                return None
    
    # add money to user account 
    def add_money(customer):
        print(f"You want to add money to {Transactions.account_type}")
        amount_of_money = input("Please Enter the amount of money you want to add it\t")
        customer[Transactions.account_type] = float(customer[Transactions.account_type]) + float(amount_of_money)
        print(f"Add money successfully, Your current balance is : {customer[Transactions.account_type]}$")
        Bank.save_accounts()
        return None
    
    # deposite money from user account
    def withdraw_money(customer):
        if customer['active'] == "False":
            return
        print(f"You want to withdraw money from {Transactions.account_type}")
        amount_of_money = 0
        while float(amount_of_money) == 0 or float(amount_of_money) >= 101:
            amount_of_money = input("Please Enter the amount of money you want to withdraw it (Your maximux is 100$)\t")
            if float(amount_of_money) > 100:
                print("That's above maximum")
                print("Please enter valid number")
            elif float(amount_of_money) > 0 and float(amount_of_money) <101:
                customer[Transactions.account_type] = float(customer[Transactions.account_type]) - float(amount_of_money)
                fee = 35
                if float(customer[Transactions.account_type]) <= 0 and int(customer['overdraft_count']) < 2:
                    customer[Transactions.account_type] = float(customer[Transactions.account_type]) - fee
                    customer['overdraft_count'] = int(customer['overdraft_count']) + 1
                    if int(customer['overdraft_count']) == 2:
                        customer['active'] = "False"
                print(f"Withdraw successful, Your Current Balance is: {customer[Transactions.account_type]}$")
                Bank.save_accounts()
                return None
            else:
                print("Please enter valid number")
                
    # check the status of user account
    def is_active(customer):
        if customer['active'] == "False" and int(customer[Transactions.account_type]) < 0:
            print("Your account is deactivated. \nYou must settle your outstanding overdraft fees to reactivate it.")
            Bank.save_accounts()
            return None
        elif customer['active'] == "False" and int(customer[Transactions.account_type])> 0:
            customer['active'] = True
            customer['overdraft_count'] = 0
            Bank.save_accounts()
            return None
    
    def transfer_money_menu(customer):
        user_options = ["1","2","3"]
        user_input = None
        while user_input not in user_options:
            print("\n\n", transfer)
            print("Select choice from below\n1. Transfer money between your accounts\n2. Transfer money to other person account\n3. Back to transactions menu")
            user_input = input("Please Choose option\t")
            match user_input:
                case "1":
                    Transactions.transfer_between_accounts(customer)
                case "2":
                    Transactions.is_active(customer)
                    Transactions.transfer_to_person_account(customer)
                case "3":
                    return None
    
    # transfer money between customer accounts
    def transfer_between_accounts(customer):
        if customer["checking"] == "False" or customer["savings"] == "False":
            print("You must have BOTH accounts to transfer between them.")
            return None

        Transactions.is_active(customer)
        if customer["active"] == "False":
            print("Your account is deactivated. Settle overdrafts before transferring.")
            return None

        source = Transactions.account_type
        destination = "savings" if source == "checking" else "checking"

        src_balance = float(customer[source])
        if src_balance <= 0:
            print(f"Cannot transfer: your {source} balance is {src_balance}$ (must be > 0).")
            return None
        user_amount = None
        
        while user_amount is None:
            amount = input(f"Enter amount to transfer from {source} to {destination}: or 'C' for Cancel\t")
            if amount.lower() == "c":
                return None
            try:
                amount = float(amount)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            if amount > src_balance:
                print("Insufficient funds in the source account (no overdrafts allowed).")
                continue
            user_amount = amount

        customer[source] = src_balance - user_amount
        customer[destination] = float(customer[destination]) + user_amount

        print("Transfer successful.")
        print(f"New balances -> Checking: {customer['checking']}$, Savings: {customer['savings']}$")
        Bank.save_accounts()
        return None

    # transfer money from current customer to other customer
    def transfer_to_person_account(customer):
        Transactions.is_active(customer)
        if customer["active"] == "False":
            return None
        
        source = Transactions.account_type
        src_balance = float(customer[source])
        if src_balance <= 0:
            print(f"Cannot transfer: your {source} balance is {src_balance}$ (must be > 0).")
            return None

        receiver_id = input("Enter recipient customer ID (or 'C' to cancel)\t")
        if receiver_id.lower() == "c":
            return None

        target = None
        for account in Bank.accounts:
            if account["id"] == receiver_id:
                target = account
                break
        if target is None:
            print("Recipient not found.")
            return None
        if target is customer:
            print("You cannot transfer to yourself here. Use 'Transfer between your accounts'.")
            return None

        receiver_accounts = []
        if target["savings"] != "False":
            receiver_accounts.append("savings")
        if target["checking"] != "False":
            receiver_accounts.append("checking")

        if not receiver_accounts:
            print("Recipient has no accounts to receive money.")
            return None
        elif len(receiver_accounts) == 1:
            destination = receiver_accounts[0]
            print(f"Recipient has only {destination}; will deposit there.")
        else:
            dest_choice = None
            while dest_choice not in ("1", "2", "3"):
                print("Send to:\n1. Recipient Savings\n2. Recipient Checking\n3. Cancel")
                dest_choice = input("Choose option\t")
                if dest_choice == "3":
                    return None
            destination = "savings" if dest_choice == "1" else "checking"

        user_amount = None
        while user_amount is None:
            amt = input(f"Enter amount to send from your {source} to recipient {destination} (or 'C' to cancel)\t")
            if amt.lower() == "c":
                return None
            try:
                amt = float(amt)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if amt <= 0:
                print("Amount must be greater than 0.")
                continue
            if amt > src_balance:
                print("Insufficient funds (no overdrafts allowed).")
                continue
            user_amount = amt

        customer[source] = src_balance - user_amount
        target[destination] = float(target[destination]) + user_amount

        print("Transfer successful.")
        print(f"Your new balances -> Checking: {customer['checking']}$, Savings: {customer['savings']}$")
        Bank.save_accounts()
        return None

# --------------------- FUNCTIONS ---------------------#
def init():
    '''
    Entry point of Project
    '''
    # load all accounts before project start
    Bank.load_accounts()
    # shows the project main menu
    session = True
    while session:
        print(welcome)
        print(
            "Please choose from below.\n1. SIGN UP\n2. Log in to your account.\n3. Quit"
        )
        user_input = input("\nPlease Enter your choice as a number: \t")
        match user_input:
            case "1":
                print("\n")
                result = Bank.sign_up_account()
                if result:
                    session = Transactions.transactions_menu(Bank.current_user)
            case "2":
                print("\n")
                result = Bank.sign_in_account()
                if result:
                    session = Transactions.transactions_menu(Bank.current_user)
            case "3":
                print("\n")
                session = None
            case _:
                print("Please enter a valid choice")
                continue


init()