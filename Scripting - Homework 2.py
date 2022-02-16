"""
Programmer: Carl Hilliard
Intro to Scripting
Homework Assignment 2
February 5, 2022
"""

## Problem 1: Printing Patterns
## Part i)
print("Question 1: Printing Patterns")
print("Part i)")

print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")

##Part ii)
print("Part ii)")
print("        *")
print("      * *")
print("    * * *")
print("  * * * *")
print("* * * * *")






"""
## Problem 2: Factorials
## Print some white space between the problems
print()
print()
print("Problem 2: ")
## in order to solve a factorial, use a while loop. While x > 0, x*total, x--;
## output the user for some integers
## Part i) Getting input from the user 
n = input("Input an integer, n:")
r = input("Input an integer, r:")
n = int(n)
r = int(r)

## use a function to solve for factorial?
## call the function with the integer as an argument
def factorial(x):
    x = int(x)
    if (x < 0):
        print("The entered inputs cannot be less than 0.")
        return 0
    elif(x == 0):
        return 1
    elif(x == 1):
        return 1
    else:
        total = 1
        while(x > 1):
            total = total * x
            x = x-1
        return total

## numerator: solve for n factorial
numerator = 1 ## to make numerator an int variable
numerator = factorial(n)

## denominator: solve for r factorial, and then multiply by n - r factorial
difference = (n -r)
difference = int(difference)
denominator = 1

denominator = (factorial(r)*(factorial(difference)))

answer = int((numerator / denominator))

## Part ii) Returning ((n!)/(r!(n-r)!))
print("Part ii)")
print("The numerator is:", numerator)
print("The denominator is:", denominator)
print("The final answer is:", answer)

      
print()
## Part iii) REturning ((n!)/(n-r)!)
numerator2 = numerator
denominator2 = factorial(difference)
total2 = numerator2 / denominator2
total2 = int(total2)
print("Part iii)")
print("The numerator is:", numerator)
print("The denominator is:", denominator)
print("The Final answer is:", total2)

"""




## Problem 3: Sort a list
## insert some white space between problems
print()
print()
print("Problem 3: Sort a List")
oldList = [20,68,41,88,16,40,65,97,85]
newList = []
while oldList:
    min = oldList[0]
    for i in oldList:
        if i < min:
            min = i
    newList.append(min)
    oldList.remove(min)
print (newList)



## Problem 4: List operations
## Print some white space between the problems
print()
print()
print("Problem 4: ")
##Part i) Find the sum of all elements in a list
print("Part i) Find the sum of all the elements in a list")
list = [1,2,3,4,5,6,7,8,9]
## sum the list using a for loop
sum = 0
for temp in range(0,9):
    sum +=list[temp]
## display the sum to the user
print("The sum of the list is:", sum)
## Part ii) Create a new list which contain even numbers. Print the list. Find the sum of all elements in the list.
print()
print("Part ii) Create a new list which contain even numbers. Print the list. Find the sum of all elements in the list.")
evenList = [2,4,6,8,10]
## print the list
for temp in evenList:
    print(temp)
## sum the list
evenSum = 0
for temp in evenList:
    evenSum += temp
print("The sum of the even list is:", evenSum)
## Part iii) Create a new list which contains odd numbers. Print the list. Find the sum of all elements in the list.
print()
print("Part iii) Create a new list which contains odd numbers. Print the list. Find the sum of all elements in the list.")
oddList = [1,3,5,7,9]
## print the list
for temp in oddList:
    print(temp)
## sum the list
oddSum = 0
for temp in oddList:
    oddSum += temp
print("The sum of the odd list is:", oddSum)
    




## Problem 5: Prime Numbers
## Print some white space between the problems
print()
print()
print("Problem 5: ")
## Use a loop to find the prime numbers
for i in range(2,51):
    prime = True
    for j in range(2,i):
        if (i % j) == 0:
            prime = False
    if prime:
          print(i)
                



## Problem 6: More list operations
## Print some white space between the problems
print()
print()
print("Problem 6: ")
## PART I) PASS n AND r ARGUMENTS FOR PROBLEM2
## PROBLEM 2
n = input("Input an integer, n:")
r = input("Input an integer, r:")
n = int(n)
r = int(r)
## use a function to solve for factorial?
## call the function with the integer as an argument
def factorial(x):
    x = int(x)
    if (x < 0):
        print("The entered inputs cannot be less than 0.")
        return 0
    elif(x == 0):
        return 1
    elif(x == 1):
        return 1
    else:
        total = 1
        while(x > 1):
            total = total * x
            x = x-1
        return total

## numerator: solve for n factorial
numerator = 1 ## to make numerator an int variable
numerator = factorial(n)

## denominator: solve for r factorial, and then multiply by n - r factorial
difference = (n -r)
difference = int(difference)
denominator = 1

denominator = (factorial(r)*(factorial(difference)))

answer = int((numerator / denominator))

## Part ii) Returning ((n!)/(r!(n-r)!))
print("Part ii)")
print("The numerator is:", numerator)
print("The denominator is:", denominator)
print("The final answer is:", answer)

      
print()
## Part iii) REturning ((n!)/(n-r)!)
numerator2 = numerator
denominator2 = factorial(difference)
total2 = numerator2 / denominator2
total2 = int(total2)
print("Part iii)")
print("The numerator is:", numerator)
print("The denominator is:", denominator)
print("The Final answer is:", total2)


## PART II) PASS LIST AS ARGUMENT FOR PROBLEM 3
def sortList(oldList):
    newList = []
    while oldList:
        min = oldList[0]
        for i in oldList:
            if i < min:
                min = i
        newList.append(min)
        oldList.remove(min)
    print (newList)
    
oldList = [20,68,41,88,16,40,65,97,85]
print ("Unsorted List: \n")
print(oldList)
print("Sorted List: \n")
sortList(oldList)








## Problem 7: Armstrong Numbers
print()
print()
print()
print("Problem 7: Armstrong Numbers")
def armStrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an armstrong number")

num = int(input("Enter a number to check if it is an Armstrong number: "))
armStrong(num)
    



## Problem 8: Fibonacci Numbers
## Print some white space between the problems
print()
print()
print("Problem 8: Fibonacci Numbers")
## create a function to find the fibonacci number. It will take a user input as an argument and print the fibonacci number
## from the corresponding index
fib = int(input("Input an integer: "))

## define the function
def fibbonacci(fib):
    if(fib < 0):
        print("Invalid input")
    if fib == 0:
        return 0
    elif fib == 1 or fib == 2:
        return 1
    else:
        return fibbonacci(fib-1) + fibbonacci(fib-2)

print(fibbonacci(fib))



## Problem 9: Fix the code
## Print some white space between the problems
print()
print()
print("Problem 9: Fix the Code")
## ADD A DESCRIPTION
loopCounter = 1
while loopCounter <= 10:
    if loopCounter % 2 == 0:
        print(loopCounter)
    loopCounter += 1
      
































