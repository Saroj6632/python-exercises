# list comprehension
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

#1
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

#2
capitalized_fruits = [fruit.capitalize()for fruit in fruits]
print(capitalized_fruits)

#3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (fruit.count('a') + fruit.count('e') + fruit.count('i') + fruit.count('o') + fruit.count('u')) > 2]
print(fruits_with_more_than_two_vowels)

#4.make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if (fruit.count('a') + fruit.count('e') + fruit.count('i') + fruit.count('o') + fruit.count('u')) == 2]
fruits_with_only_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters
[fruit for fruit in fruits if len(fruit) > 5]


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit)== 5]



# Exercise 7 - Make a list that contains fruits that have less than 5 characters

[fruit for fruit in fruits if len(fruit) < 5]


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
[len(fruit)for fruit in fruits]


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [ fruit for fruit in fruits if "a" in fruit ]
fruits_with_letter_a


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 ==0]
print(even_numbers)



# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)



# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers =[number for number in numbers if number >0]
print(positive_numbers)


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number <0]
print(negative_numbers)


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more = [number for number in numbers if len(str(abs(number)))>=2]
print(two_or_more)



# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number*number for number in numbers]
print(numbers_squared)


#16 Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number %2 != 0 and number < 0]
print(odd_negative_numbers )



#17
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
number_plus_5 = [number + 5 for number in numbers]
print(number_plus_5)
