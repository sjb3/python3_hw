# simple iterating and adding SUM
# given_list = [1,10,100]
#
# def main(list):
#     sum = 0
#     i = 0
#
#     while i < len(list):
#         sum += list[i]
#         i += 1
#     print(sum)
#
# main(given_list)

# given_list = [1,12,123]
# sum = 0
# for i in given_list:
#     sum += i
# print(sum)

# FIZZ-BOZZ excercises(7/30)
# i = 1
# results = ''
#
# while i <= 50:
#     if i % 15 == 0:
#         results = 'fizz-bozz'
#     elif i % 3 == 0:
#         results = 'fiz'
#     elif i % 5 == 0:
#         results = 'boz'
#     else:
#         results = i
#     i += 1
#
#     print(results)

# REPLACE example with WHILE look(7/30)
# def replace(str, old, new):
#
#     if len(str) < 1 or old not in str or len(old) < 1:
#         return str
#
#     newStr = ''
#     i = 0
#     while i < len(str):
#         # build new strings character by character
#         # pass
#         curr = str[i]
#         if curr != old:
#             # do something
#             newStr += curr
#             # print(newStr)
#         else:
#             # do another
#             newStr += new
#             # print(newStr)
#         i += 1
#     return newStr
#
# def main():
#         str = input('Provide string(s) you wanna play with: ')
#         old = input('Provide string that you wanna replace: ')
#         new = input('How do you wanna change? ')
#
#         newStr = replace(str, old, new)
#         print(newStr)
#
# main()

# REVERSE function(7/30)
# def reverse(word):
#     if len(word) <= 1 :
#         return word
#
#     i = 0
#     newStr = ''
#
#     while i < len(word):
#         newStr += word[(len(word) - 1)-i]
#         i += 1
#         # print(newStr)
#     return newStr
#
# def main():
#     str = input('Enter for flipping! ')
#     newStr = reverse(str)
#     print(newStr, end=': ')
#
#
#     if str.lower() == newStr.lower():
#         print('Palindrome!')
#     else:
#         print('NAH')
#     # return results
#     # print(results)
# main()
#
# # Program 8-1 / p. 410
# counting T or t's

# def main():
#     user_input = input('Enter the string you wanna examine: ')
#
#     i = 0
#     count = 0
#     while i < len(user_input):
#         if user_input[i] == 'T' or user_input[i] == 't':
#             # print(i, user_input[i])
#             count += 1
#         i += 1
#
#     print('"T" or "t" occured ', count, 'times in given string')
#
# main()

# Program 8-6 / p. 425
# validating proper login name and valid password

# def get_longin_name(first, last, idnum):
#     first_set = first[: 3]
#     last_set = last[: 3]
#     id_set = idnum[-3 :]
#     longin = first_set + last_set + id_set
#
#     return login
#
# def valid_password(password):
#     """ results should be boolean
#         length should be at least 7,
#         should have at least one capital letter,
#         should have at least one lowercase letter,
#         should have at least one digit
#     """
#     correct_length = False
#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False
#
#     if len(password) >= 7:
#         correct_length = True
#
#         i = 0
#         while i < len(password):
#             if password[i].isupper():
#                 has_uppercase = True
#                 print('UPPER', has_uppercase)
#             if password[i].islower():
#                 has_lowercase = True
#                 print('lower', has_lowercase)
#             if password[i].isdigit():
#                 has_digit = True
#                 print('1234', has_digit)
#             i += 1
#
#     if correct_length and has_uppercase and has_lowercase and has_digit:
#         is_valid = True
#     else:
#         is_valid = False
#
#     return is_valid
#
# #
# def main():
#     password = input('password? ')
#
#     while not valid_password(password):
#         print('Worng password')
#
#         password = input('password? ')
#
#     print('At-sSA')
#
# main()

# Program 8-9, Splitting a String, p.429

# def main():
#     user_input = input('Enter your e mail addy. ')
#
#     results_list = user_input.split('@')
#     print(results_list[0])
#
# main()
# def main():
#     an_letters = 'aefhilmnorsxAEFHILMNORSX'
#
#     word = input('Enter a word ')
#     times = int(input('Enthusiasm Level: '))
#
#     i = 0
#     while i < len(word):
#         char = word[i]
#         if char in an_letters:
#             print('Give me an ' + char + ' ! ' + char + ' !')
#         else:
#             print('Give me a ' + char + ' ! ' + char + ' !')
#         i += 1
#     print('What does that spell?')
#
#     for i in range(times):
#         print(word, '!')
#
# main()
# approximate solution for cube questions
# def main():
#     cube = 10000
#     epsilon = 0.1
#     guess = 0.0
#     increment = 0.01
#     num_guesses = 0
#     while abs(guess**3 - cube) >= epsilon and guess <= cube:
#         # print('>>>>>>', guess)
#         guess += increment
#         num_guesses += 1
#     print('num guesses = ', num_guesses)
#
#     if abs(guess**3 - cube) >= epsilon:
#         print('Failed on cute root of', cube)
#     else:
#         print(guess, 'close enough cube', cube)
#
# main()

# def main():
#     is_continue = 'y'
#
#     while is_continue == 'y':
#         sales = float(input('Enter the sales figure:'))
#         rate = float(input("What's your commision rate? "))
#
#         sales_commision = sales * rate
#         print("The commision is ", sales_commision)
#         is_continue = input('If you wanna continue, please enter y ')
#
# main()

# def main():
#     num = int(input("Number "))
#     i = 0
#     sum = 0
#     while i <= num:
#         sum += i
#         print(sum)
#         i += 1
#     print('>>>', sum)
#     return sum
#
# main()

# Recursion
# always start with base case, like if n = 1
# in case of factorial problem
# def factorial(n):
#     # i = 0
#     # while i < n:
#     # base
#     if n == 1:
#         return 1
#     # Recursion
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

# Palindrome in Recursion
# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#
#     return isPal(toChars(s))
