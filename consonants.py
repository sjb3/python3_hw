# Test for consonants
# def all_consonants(word):
#     if len(word) < 1:
#         return False
#
#     # i = 0
#     # result = True
#     # vowels = 'aeiou'
#     #
#     # while i < len(word):
#     #
#     #     char = word[i].lower()
#     #     if char in vowels:
#     #         result = False
#     #     i += 1
#     #
#     # return result
#     ### using for loop instead
#     vowels = 'aeiou'
#     result = True
#
#     for char in word:
#         if char.lower() in vowels:
#             result = False
#             break
#     return result


# def main():
#     str = input("Enter to see if it's all Consonants! ")
#     result = all_consonants(str)
#     print(result)
#
#     # str = input('Enter: ')
#     # testTwoSame(str)
# main()

# TEST for TWO Consecutive Char's
def testTwoSame(word):
    """
        This function accepts a string as arg and returns True
        if the passes in string is non-empty and contains 2 consecutive same characters:
        FALSE, otherwise
    """
    # if len(word) < 2:
    #     return False
    #
    # i = 0
    # result = False
    #
    # while i < len(word)-1:
    #     curr = word[i]
    #     next = word[i + 1]
    #     # print(prev, curr)
    #     if curr == next:
    #         # print(i, curr, next, result)
    #
    #         result = True
    #         print(i, curr, next, result)
    #     i += 1
    #
    # return result

    ### use for loop instead
    if len(word) < 2:
        return False

    result = False

    for i in range(len(word)-1):
        curr = word[i]
        next = word[i +1]
        if curr == next:
            result = True
            break
    return result

def main():
    """
        Service consumer that take advantage of testTwoSame functions
        and returns with simeple print function with corresponding results
    """
    str = input('Enter the string that you wanna examine: ')
    result = testTwoSame(str)
    print(result)

main()
