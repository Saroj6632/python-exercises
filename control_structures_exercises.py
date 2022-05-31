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
pay_check = (no_of_hours) * (hourly_rate)
if no_of_hours > 40:
   print(pay_check * 1.5) 
else:
    print(pay_check)


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
num_entered = input("Enter an odd number between 1 and 50: ")
while True:
    if num_entered.isdigit() and int(num_entered) % 2 == 1 and int(num_entered) in list(range(1, 50)):
        break
    num_entered = input("Try again!! Enter ODD number: ")

for n in range (1,50):
    if n == int(num_entered):
        print("Yikes, skipping the", n)
        continue
    if n % 2 == 0:
        continue
    else:
        print("Here is an odd number", n)





# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_number = input("Please enter a number: ")
while True:
    if user_number.isdigit() and int(user_number) > 0:
        break
    user_number = input("Please enter a positive number: ")
for n in range(0, int(user_number)):
    print(n)
        
#Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
user_number = input("Please enter a number: ")
while True:
    if user_number.isdigit() and int(user_number) > 0:
        break
    user_number = input("Please enter a positive number: ")
for n in range(int(user_number), 0, -1):
    print(n)

#Fizzbuzz
# Write a program that prints the numbers from 1 to 100.
for n in range(1,101):
    print(n)

# For multiples of three print "Fizz" instead of the number
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    else:
        print(n)

# For the multiples of five print "Buzz".
for n in range(1, 101):
    if n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    else:
        print(n)

#Different mathod
for n in range (1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)


# # Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
user_number = input(" enter a number")
while True:
    if user_number.isdigit() and int(user_number):
        break
    user_number = input("enter a valid integer: ")

for n in range (1, int(user_number)):
    print("n, n**2, n**3)

#Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 -0
user_number = input("Enter a numericaluser_number grade: ")
while True:
    if float(user_number) > 0 and float(user_number)< 100:
        user_number = float(user_number)
       
        if (user_number) <=100 and (user_number) >= 88:
            print("A", (user_number))
        elif (user_number) >= 87:
            print("B", (user_number))
        elif  (user_number) >= 67:
            print("C", (user_number))
        elif (user_number) >= 60:
            print("D", (user_number))
        else:
            print("F", (user_number))
        more_results = input("Would you like to continue? Y/N ")
        if more_results == 'N':
            break
        else:
            user_number = input("Enter a numerical user_number grade: ")
                
    else:
        print("incalid input")
        user_number = input("Enter a numericaluser_number grade: ")
            

#Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
books = [{'title':'harry potter', 'author':'J.K Rowling','genre':'fiction'},
         {'title':'Muna Madan','author':'Laxmi Prasad Devkota','genre':'Love and Romance'}]
user_genre = input("Please write a genre name: ")
for book in books:
    if user_genre == book['genre']:
        print(book['title'])




 


