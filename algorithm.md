# Algorithm Document

## Algorithm for ATM Simulation
1. Output the purpose of the program.
2. Set the sentinel value to 'E'.
3. Set the initial balance to $1000.
4. Initialize a variable choice to an empty string (or any value that is not equal to the sentinel).
5. Output the initial balance.
6. As long as choice is not equal to the sentinel:
   1. Prompt the user to input an option (D for Deposit, W for Withdraw, V for View Balance, E for Exit). 
   2. Convert the input to uppercase for case-insensitivity. 
   3. If the user chooses to deposit (D):
      1. Prompt the user to input the amount they wish to deposit. 
      2. Check if the amount is a negative value:
         - If yes, output an error message and prompt to try again. 
      3. Add the amount deposited to the initial balance and assign the result to 'current balance'
      4. Output the current balance.
   4. Otherwise, if the user chooses to withdraw (W):
      1. Prompt the user to input the amount they wish to withdraw. 
      2. Check if the amount is negative:
         - If yes, output an error message and prompt to try again.
      3. Subtract the amount withdrawn from initial balance and assign the result to 'current balance'
      4. If the resulting balance is negative:
         1. Output a warning that they will be charged 5% interest.
      5. Output the current balance.
   5. Otherwise, if the user chooses to view balance (V):
      1. Output the current balance.
   6. Otherwise, if the user chooses to exit (E):
      1. Output 'Exiting the ATM. Thank you!'
   7. Otherwise:
      1. Output an error message indicating that the input was invalid.
