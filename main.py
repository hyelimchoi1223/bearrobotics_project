from data import *
from simple_ATM import ATM

if __name__ == "__main__":
    # 1: make user data
    data = []
    data.append(UserData("CAAA", "111", AccountData("A111", 100000)))
    data.append(UserData("CBBB", "222", AccountData("B111", 500000000)))

    # 2: make ATM
    atm = ATM(data)
    # 3: insert card to ATM
    card = input("Please insert card......\n")
    atm.insert_card(card)
