# The program asks the user to guess a number between 1 and 20 in not more than 6 tries

import random #importing random library

guesses_taken = 0 #new variable created with 0 value assigned

print('Hello! What is your name?') #funcion print used with a string argument "Hello..."
myName = input() #function input used which assign an input value (for mkeyboard) to a newly created variable myName

number = random.randint(1, 20) #return value from function randint from random class, taking arguments 1,20, is assigned to a new vaiable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #function print with argument - a sum of strings and myName variable(type string)

while guesses_taken < 6: #while loop which is executed until g_t variables is below 6
    print('Take a guess.') #print function with string argument
    guess = input() #again input function is called and its return (input from keyboard) is assigned to new variable guess
    guess = int(guess) #the varaible guess is reassigned by the result of fuction int with argument guess (the return is change of fuess type form string to int)

    guesses_taken += 1 #inceremts g_t varaible by 1

    if guess < number: #if conditional which is executed is value of guess variable is lowet than value of numebr variable
        print('Your guess is too low.') #another print

    if guess > number: #again if conditional, but this will be executed if guess value is higher than numer value
        print('Your guess is too high.') #another print

    if guess == number: #if conditional which iwll be execute only if guess value is equal nu number value
        break #stops the while loop and starts to execute the part below while

if guess == number: #a confitional which is executed if guess value is equal to number value
    guesses_taken = str(guesses_taken) #to g_t variable is assigned a new value which is a result of function str on g_t argument (changing g_t to string)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #prints to screen string+myName sring+....

if guess != number: #another if conditional which is eecuted if guess value is different than number value
    number = str(number) #to number a result of str function over number is assigned (number changed to string)
    print('Nope. The number I was thinking of was ' + number) #another print - see above

