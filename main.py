# PUT THE INTRO COMMENTS HERE

# Output the purpose of the program.

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
        # Add the amount deposited to the balance
        balance += deposit_amount
        # Output new balance
        print('Your balance is: ', balance)
    # Otherwise if the user chooses to withdraw, prompt them to input how much they wish to withdraw
    elif choice == 'W':
        withdraw_amount = int(input('How much money do you want to withdraw? '))
        # Subtract the withdrawal amount from the balance
        balance -= withdraw_amount
        # Output new balance
        print('Your balance is: ', balance)
        # If balance is negative, warn the user that they will be charged 5% interest
    # Otherwise if the user chooses to view their balance, output balance
    elif choice == 'V':
        print('Your balance is: ', balance)
    # Otherwise print that the output was invalid
    else:
        print('Invalid choice.')