'''
pseudo code:

Create Bank Class
- define Users
# define Accounts
    add all accounts to the array

- define log in to user account

- create withdrow
Types of accounts:
    - Checking Account
    - Saving Account
'''
# --------------------- Bank Class ---------------------#
class Bank():
    account = []
    curr_user = None
    
    def __init__(self):
        pass

    def sign_in_account(self):
        while True:
            print("""
===========================================
                SIGN IN
===========================================""")
            user_id = input("Please Enter your ID: ")
            user_password = input("Please enter your password: ")
            user_data = data_controller.sign_in(user_id,user_password)
            if user_data and user_data[0] is True:
                return user_data
            else:
                print("Please provide correct Credintials")
                self.sign_in_account()
# --------------------- Bank Class End ---------------------#

def start_menu():
    while True:
        print(
            """
================================
🏦 Hello to you're Python Bank!
================================"""
        )

        print(
            """Please choose from below
1. Log in to your account
2. Quit"""
        )
        user_input = input("\nPlease Enter your choice as a number: ")
        match user_input:
            case "1":
                print("\n")
                result = bank.sign_in_account()
                if result:
                    print("User credinital is correct")
                    customer_menu()
            case "2":
                print("\n")
                break
            case _:
                print("Please enter a valid choice")
                continue
            
def customer_menu():
    print("User menu work!")