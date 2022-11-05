# Performing Calculations

If you have been going through the chapters they way they were intended, you will see that we have all the information we need in order to calculate the operation wanted by the user. But, now it's time to actually perform and print the calculation. We will be using if/else and print statements to do so.

## Why are we using if, else, and elseif statements?:

Understand: The reason we are using if/else statements is to print the exact calculation wants to perform. For example, if the user wants to add and types in 'a' (the addition operation) in the if and else statement we wrote in the previous chapter ('what operation?'), then our program should go to the if statement where it will read if 'a', print (no1 + no2).

## Coding our if and else statements:

We will mainly be using 4 if and else statements: one for addition, one for subtraction, one for multiplication, and one for division. Add the following commands to your main.py file (underneath your previous code).

1. Lets start with the addition if and else statement. To write your addition if and else statement type in this command: if op == 'a': print(no1 + no2)
2. Understand: Since we have initialized our if and else statements with the 'if' part of the previous command (instruction line 1), the following operations can be done simply with the 'elseif' commnad instead of the 'if' command.
3. Next lets do our subtraction statement. To write your subtraction statement, type in this command: elseif op == 's': print(no1 - no2)
4. Now for our multiplication statement (type in this command): elseif op == 'm': print(no1 * no2)
5. Last but not least our division statement (type in this command): elseif op == 'd': print(no1 / no2)
6. Although it is not required, there is one more thing we can do to make our program nicer. We can add an error message just incase the user puts in a wrong operation (instead of a, s, m, and d). Can you guess how to do this? To be honest, the answer is very simple. We can just add an else statement at the end of all the if and elseif statements we have previously written. This is how the else statement would look like: else: print("You did not put an elgible operation symbol, rerun the program using an elgible symbol.")
7. 