#H7_sung.py
#GreatestNon-Trivial Factor

def user_input(prompt):
    """
        simple prompting only function to apply modularization patter
    """

    data = input(prompt)
    return data

def greatest_nontrivial_factor(num):
    """
        my approach is, if the given number is divisible, the quotients will be collected separately in list as in order
        and for the answer, return the very last element will be displayed ( the number itself isn't answer FYI)
        Also, if it's not divisible by any numbers, 'NONE' will be displayed
    """

    ##########
    div = 1
    while div < num:
        if num % div == 0:
            # print(div)
            answer = div
        div +=1
    print(answer)
    return answer
    # print(div)
    ##########
    # factor_list = []
    # div = 1
    #
    # while div <= num:
    #     if num % div == 0:
    #         # print(div)
    #         factor_list.append(div)
    #         # print(factor_list)
    #         div += 1
    #     else:
    #         div += 1
    #
    # if len(factor_list) <= 2:
    #     # return None
    #     def greatest_nontrivial_factor(num) : pass
    #     x = greatest_nontrivial_factor(num)
    #     print (x)
    #     return None
    # else:
    #     print('The greatest non-trivial factor of given number is ', factor_list[-2])

def main():
    """
        adopting prompting function in main()
        Return: after prompting, greatest_nontrivial_factor function will be called and display the greatest nontrivial factor will be displayed
    """

    nat_number = int(user_input('Enter any number to see the greatest non trivial number: '))
    greatest_nontrivial_factor(nat_number)

if __name__ == '__main__':
    main()
