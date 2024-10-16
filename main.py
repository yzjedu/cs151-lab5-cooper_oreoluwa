# Programmers: Cooper Nazar, Oreoluwa Adebusoye
# Course: CS151, Zelalem Yalew
# Due Date: 10/16/2024
# Lab Assignment: 5
# Problem Statement/Purpose: This program is designed to simulate an ATM, where a user can view their balance, deposit money, and withdraw money
# Data In: Amount of money to deposit or withdraw
# Data Out: Balance
# Credits: None

# Output the purpose of the program.
print('This program is meant to simulate an ATM.\n')
print("Welcome to the ATM!")
print("You can perform the following actions:")
print("\tD - Deposit")
print("\tW - Withdraw")
print("\tV - View Balance")
print("\tE - Exit")

# Set the sentinel to 'E' and the initial balance to 1000
SENTINEL = 'E'
balance = 1000

# Set choice to a random value
choice = 'G'

# Output initial balance
print(f"Your current balance is: ${balance:.2f}")

# Start the loop
while choice != SENTINEL:
    # Prompt the user to enter whether they want to deposit, withdraw, view balance, or exit
    choice = input('\nDo you want to (D) deposit, (W) withdraw, (V) view balance, or (E) exit? ')
    # Convert choice to uppercase
    choice = choice.strip().upper()
    # If the user chooses to deposit, prompt them to input how much they wish to deposit
    if choice == 'D':
        deposit_amount = float(input('\nHow much money do you want to deposit? '))
        # Make sure the user can't input a negative number
        if deposit_amount < 0:
            print('\nError: You cannot deposit a negative amount. Please try again.')
            deposit_amount = 0
        # Add the amount deposited to the balance
        balance += deposit_amount
        # Output new balance
        print(f"\nYour current balance is: ${balance:.2f}")
    # Otherwise if the user chooses to withdraw, prompt them to input how much they wish to withdraw
    elif choice == 'W':
        withdraw_amount = float(input('\nHow much money do you want to withdraw? '))
        # Make sure the user can't input a negative number
        if withdraw_amount < 0:
            print("\nError: You cannot withdraw a negative amount. Please try again.")
            withdraw_amount = 0
        # Subtract the withdrawal amount from the balance
        balance -= withdraw_amount
        if balance < 0:
            # Warn the user that they will be charged 5% interest if their balance is negative
            print("\nWarning: Your balance is negative! You will be charged 5% interest.")
        # Output new balance
        print(f"\nYour current balance is: ${balance:.2f}")
    # Otherwise if the user chooses to view their balance, output balance
    elif choice == 'V':
        print(f"\nYour current balance is: ${balance:.2f}")
    # Otherwise print that the output was invalid.
    elif choice == 'E':
        print("\nExiting the ATM. Thank you!")
    else:
        print("\nError: Invalid input. Please enter D, W, V, or E.")