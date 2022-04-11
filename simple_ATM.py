from data import *


class ATM:
    def __init__(self, customer_data):
        self.customer_data = customer_data

    def insert_card(self, card_num):
        pin_num = input("Input your pin number......\n")
        info = self.check_pin_number(card_num, pin_num)
        if info == None:
            return

        self.select_account(info)

    def check_pin_number(self, card_num, pin_number):
        info = [
            customer
            for customer in self.customer_data
            if customer.card_number == card_num
        ]
        if len(info) == 0:
            print(f"It's wrong card number")
            result = None
        elif info[0].pin_number == pin_number:
            print("Success.")
            result = info[0]
        else:
            print("Wrong PIN number")
            result = None

        return result

    def select_account(self, info):
        task = input("Please select 1:Balance 2:Deposit 3:Withdraw\n")
        if task == "1":
            print(info.account)
        elif task == "2":
            money = input("Input deposit money......\n")
            info.account.deposit(money)
            print("After deposit...")
            print(info.account)
        elif task == "3":
            money = input("Input withdraw money......\n")
            info.account.withdraw(money)
            print("After withdraw...")
            print(info.account)

        yes_or_no = input(
            "If you have another thing to do, pleas input Y.\nIf you don't have nothing to do, please input any button.\n"
        )
        if yes_or_no == "Y":
            self.select_account(info)
        else:
            print("thank you")
            return
