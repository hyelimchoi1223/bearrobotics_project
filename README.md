# bearrobotics_project
Implement a simple ATM controller

## Data class
Data class is in [data.py](https://github.com/hyelimchoi1223/bearrobotics_project/blob/main/data.py)
There is two data class.
1. Account Data class
      - Function
        * check balance
        * deposit
        * withdraw
2. User Data class

## ATM class
[simple_ATM.py](https://github.com/hyelimchoi1223/bearrobotics_project/blob/main/simple_ATM.py) is actual functional class.
- Function
  * Insert card
  * Check PIN number
  * Select Account

This class can use only using only "Insert card" function. Another functions operate internally.

## How to use
1. You have to define user data.
```python
data = []
data.append(UserData("CAAA", "111", AccountData("A111", 100000)))
data.append(UserData("CBBB", "222", AccountData("B111", 500000000)))
```
2. Make ATM and insert user data.
```python
atm = ATM(data)
```
3. Insert card number to ATM
```python
card = input("Please insert card......\n")
atm.insert_card(card)
```
