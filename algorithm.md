# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

Notes:
- Make it so it gives an error when the user gives a negative number (maybe by searching for a negative sign in the string)

Algorithm:
1. Output the purpose of the program
2. Set the sentinel to 'E'
3. Set the initial balance to 1000
4. Output the initial balance
5. While choice is not equal to the sentinel:
   1. Prompt the user to input what they want to do
      1. Deposit, withdraw, view balance, or exit
      2. Store their choice as a variable such as 'choice'
   2. If the user chooses to deposit:
      1. Prompt the user to input how much they wish to deposit
      2. Add the amount deposited to initial balance and assign the result to 'current balance'
      3. Output the current balance
   3. Otherwise if the user chooses to withdraw:
      1. Prompt the user to input how much they wish to withdraw
      2. Subtract the amount withdrawn from initial balance and assign the result to 'current balance'
      3. If the current balance is negative:
         1. Warn the user that they will be charged 5% interest
      4. Output the current balance
   4. Otherwise if the user chooses to view balance:
      1. Output current balance
   5. Otherwise
      1. Output that the input was invalid