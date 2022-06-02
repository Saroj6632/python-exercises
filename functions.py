#Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(input):
  return str(input) == "2"


#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(alphabet):
    if alphabet.lower() in ['a','e','i','o','u']:
        return True
    else:
        return False


#Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(alphabet):
    if is_vowel(alphabet)== True:
        print('the alphabet is vowel')
        return False
    else:
        print('It is Consonant')
        return True


#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_first_letter(string):
    if is_consonant(string[0]):
        return string.capitalize()
    return string

#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
#and return the amount to tip.

def calculate_tip(tip_percentage,bill):
    if tip_percentage > 0 and tip_percentage < 1:
        tip_amount = bill * tip_percentage
        return tip_amount
    
#Define a function named apply_discount. It should accept a original price, and 
#a discount percentage, and return the price after the discount is applied.


def apply_discount(price, discount_percent):
    discount_amount = ((discount_percent / 100) * price)
    final_price = price - discount_amount
    return final_price

# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, 
#and return a number as output.

def handle_commas(num):
    num = num.replace(",", "")
    return num


# Define a function named get_letter_grade. It should accept a number and return 
#the letter grade associated with that number (A-F).
  # function to get letter grade


def get_letter_grade(num):
    if num >= 93:
        grade = 'A'
    elif num >= 80:
        grade = 'B'
    elif num >= 60:
        grade = 'C'
    elif  num >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return grade

#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

vowels = ("a","e","i","o","u")
def remove_vowels(string):
    for x in string:
        if x in vowels:
            string = string.replace(x,"")
    return string


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

#this function replaces any special character
def remove_special_char(string):
    return ''.join(c for c in string if c.isalnum() or c == '')

def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return (special_char_removed.lower().strip().replace(" ","_"))



# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(lists):
    output =[]
    total = 0
    for num in lists:
        total = total + num
        output.append(total)
    return output
         