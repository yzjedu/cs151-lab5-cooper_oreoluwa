# Programmers: Cooper Nazar, Oreoluwa Adebusoye
# Course:  CS151, Zelalem Yalew
# Due Date: 10/16/2024
# Lab Assignment: 5
# Problem Statement: This program is designed to simulate an ATM, where a user can view their balance, deposit money, and withdraw money
# Data In: Amount of money to deposit or withdraw
# Data Out: Balance
# Credits: None

# Output the purpose of the program.
print('This program is meant to simulate an ATM.')

# Set the sentinel to 'E' and the initial balance to 1000
SENTINEL = 'E'
balance = 1000
# Set choice to a random value
choice = 'G'

# Output initial balance
print('Your balance is: ', balance)

#Start the loop
while choice != SENTINEL:
    # Prompt the user to enter whether they want to deposit, withdraw, view balance, or exit
    choice = input('Do you want to (D) deposit, (W) withdraw, (V) view balance, or (E) exit?')
    # Convert choice to uppercase
    choice = choice.strip().upper()
    # If the user chooses to deposit, prompt them to input how much they wish to deposit
    if choice == 'D':
        deposit_amount = int(input('How much money do you want to deposit? '))
        # Make sure the user can't input a negative number
        while deposit_amount < 0:
            print('Invalid amount.')
            deposit_amount = 0
        # Add the amount deposited to the balance
        balance += deposit_amount
        # Output new balance
        print('Your balance is: ', balance)
    # Otherwise if the user chooses to withdraw, prompt them to input how much they wish to withdraw
    elif choice == 'W':
        withdraw_amount = int(input('How much money do you want to withdraw? '))
        # Make sure the user can't input a negative number
        while withdraw_amount < 0:
            print('Invalid amount.')
            withdraw_amount = 0
        # Subtract the withdrawal amount from the balance
        balance -= withdraw_amount
        # Output new balance
        print('Your balance is: ', balance)
    # Otherwise if the user chooses to view their balance, output balance
    elif choice == 'V':
        print('Your balance is: ', balance)
    # Otherwise print that the output was invalid.
    elif choice != 'E':
        print('Invalid choice.')
    else:
        print('Thank you for using this program.')
    # Warn the user that they will be charged 5% interest if their balance is negative
    if balance < 0:
        print('Negative balance. You will be charged 5% interest!')