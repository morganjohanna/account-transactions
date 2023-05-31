current_balance = 250
amount = int(input("How much would you like to withdraw? "))

def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

if (current_balance >= amount):
    current_balance = withdraw_money(current_balance, amount)
    if (current_balance <= 50):
        print("Your balance is now")
        print(current_balance)
        print("You should probably make a deposit.")
    else:
        print("Thanks! Your balance is now ")
        print(current_balance)

else:
    print("I can't do that, Dave. Insufficient funds.")