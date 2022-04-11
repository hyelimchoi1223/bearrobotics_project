class AccountData:
    """
    Account data class
    attr:
        name: account name
        balance: current balance in account
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def deposit(self, money):
        self.balance += int(money)

    def withdraw(self, money):
        self.balance -= int(money)

    def __repr__(self):
        return f"Account balance :{self.balance}"


class UserData:
    """
    User data class
    attr:
        card_number: card info
        pin_number: pin info
        account: account connected with card
    """

    def __init__(self, card, pin, account):
        self.card_number = card
        self.pin_number = pin
        self.account = account

    def __repr__(self):
        text = f"Card number: {self.card_number},"
        text += f"Pin number: {self.pin_number},"
        return text
