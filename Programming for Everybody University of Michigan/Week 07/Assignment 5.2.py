# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
import sys

largest = 0
smallest = sys.maxsize -1
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        print ('Invalid input')
        break
    else :
        try:
            value = int(num)
            if value > largest :
                largest = value
            elif value < smallest :
                smallest = value
        except:
            continue

print("Maximum is", largest)
print("Minimum is", smallest)
