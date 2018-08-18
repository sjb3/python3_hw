#H12_sung.py
# Random Number Guessing Game
import random

try:
    def guessing_game():
        ''' This will generate the random number and compare with the user's guessed number till
            the guess is right: for return) either the guessed number is lower or higher, the proper message will be displayed accordingly;
            however, the guess is right, generated hidden_num will be returned with compliment
        '''
        hidden_num = random.randint(1, 100)
        my_guess = int(input('Enter number to find out Computer\'s secret number > '))

        while hidden_num != my_guess:
            if hidden_num > my_guess:
                print('Too low, try again > ')
                # print(my_guess, hidden_num)
                my_guess = int(input('Enter number to find out Computer\'s secret number > '))

            else:
                print('“Too high, try again > ')
                # print(my_guess, hidden_num)
                my_guess = int(input('Enter number to find out Computer\'s secret number > '))

        return hidden_num

    def main():
        ''' returned hidden_num is displayed for final answer
            after calling guessing_game()
        '''
        hidden_num = guessing_game()
        print('Congrats! Your guess is right! <)))><~ The hidden number is: ', hidden_num, '!')

    main()

except Exception as err:
    print(err)
