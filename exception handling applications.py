#exception handling applications
#project: withdraw money from bank
#-balance in bank should not be less than 1000
#-user account will be blocked for an hour if user put 3 times wrong pin
import time
class BalanceException(Exception):
    pass
class AttemptExceptionError(Exception):
    pass
attempt = 1
def withdraw():
    global attempt
    saved_pin = 1234 #hardcoded
    balance = 10000 #hardcoded
    pin = int(input("enter the pin:"))
    if pin == saved_pin:
        try:
            amt = float(input("enter amount to withdraw:"))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceException("Insufficient balance")
            balance = balance - amt
            print("Remained balance is:",balance)
        except Exception as var:
            print(var)
    else:
        ans = input("do you want to continue again:(y/n):")
        if ans.lower() == 'y':
            attempt += 1
            try:
                if attempt == 4:
                    raise AttemptExceptionError("to many attempts,your account is block for an hour")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you!")
            return

withdraw()
