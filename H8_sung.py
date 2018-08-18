# H8_sung.py
# Check for Palindrome

def get_prompt(prompt):
    """
        set prompting function separately to embrace the fx decompositioning
        Return: after prompting, string will be returned
    """
    data = input(prompt)
    return float(data)

def isPalindrome(word):
    """
        Adopting the function above for prompting,
        Results:
        TRUE if the passed-in argument is a palindrome, FALSE otherwise.
        !!! CASE SENSITIVE !!! it should be, hence no need to use upper or lower() to make the string uniform
    """
    i = 0
    result = True

    while i < len(word):
        if word[i] != word[(len(word) - 1) - i]:
            # print('BEFORE', word[i], word[(len(word)-1)-1])
            result = False
            # print('AFTER', word[i], word[(len(word)-1)-1])

        i += 1

    return result

def main():
    """
        aggregate above functions along with final reports for end users to display the boolean value of it
    """
    str = input("Type a word to see if it's palidrome or not: ")
    result = isPalindrome(str)
    print(result)

if __name__ == '__main__':
    main()
