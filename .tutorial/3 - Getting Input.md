# Getting Input:

Getting Input is vital because the point of our calculator program is to take two numbers given by the user and calculate their wanted operation. 

In order to perform a calculation, we first have to take the two numbers and store them into a variable. But, the numbers that we want to get have to come from the user of the program, so we will use the "input" command and store the value that was inputted into an interger based variable.

## Example:
no1 = int(input('Input your first number here:' ))                     
no2 = int(input('Input your second number here'))

Explanation: Up above, you can see that there are 2 variables: 'no1' and 'no2'. Each variable listed above is storing what the user has inputted (when the program is executed) as an integer variable.

## How do you get input from the user?
Since we've seen the example above, let's go ahead and try to get input from the user!

### Let's try it ourselves:

1. In your main.py file, underneath your welcome/print statement, go ahead and type: no1 = int(input('Input your first number here:' ))
2. Understand: When the program is run, the user will see the words and characters "Input your first number here:" under your welcome/print statement in the console. On the right most of this text in the console, you will be able to see that you can input an integer number and press enter. This value is then stored into the no1 integer variable.
3. Next, underneath your first Input statment, go ahead and write a second Input statement: no2 = int(input('Input your second number here:' ))
4. Go ahead and run this program. Although they aren't doing anything other than storing the value in the variable, see how the input statements work and predict how we can use these variables and values to perform other tasks and functions.
5. Modifications: If you would like to create a custom variable name or want to make the user prompt appear differently, go ahead and change the program and have some fun!
6. Your program should look similar to <a href="https://github.com/testUser453/Build_A_Calculator_With_Python/blob/main/ForCreator(Don't_Edit!)/ExampleCode/2-ExGetInput.py">this
</a>

Great Job! You have completed the Getting Input chapter! Move on to the next chapter: What Operation?