# conditional basics
#prompt the user for a day of the week, print out whether the day is Monday or not

day = int(input("Enter the number 1-7:  "))
if day == 2:
    print (" It is Monday")
else:
    print("It is not  Monday")

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = int(input("Enter the number between 1 and 7: "))
if day == 1:
    print(day,"It's a weekend")
elif day == 7:
    print(day, "Its a weekend")
else:
    print(day," It is weekday")

#create variables and make up values for

#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hourly_rate = float(input("Standard hourly pay: "))
no_of_hours = float(input("hours this week: "))
paycheck = (no_of_hours)*(hourly_rate)
if no_of_hours > 40:
   print(paycheck *1.5) 
else:
    print(paycheck)


#Q.no 2 Loop basics
#While Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print (i)
    i -=5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000
i = 2
while i < 1000000:
    print(i)
    i = i**2

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -=5

# for loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num_entered = int(input("please enter a number of your choice: "))
for i in range (1, 11):
    print(num_entered, "X", i , "=" num_entered * i )

#Create a for loop that uses print to create the output shown below.
for num in range(1,10):
    print(str(num)*num)

# Break and continue
#Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
num = int(input("Enter an odd number between 1 and 50: "))
