# H13_sung.py
# creating multiplication table: when it's prompted, the user enter the number to tabulate
# and the results will be returned as a table on terminal

try:
    def multiplication_tab(N):
        ''' This function will offer proper header(see below)
            after that, by using the nested loop, you create and return
            n x n, the multiplication table
        '''
        print('\t|***********************************|\n')
        print('\t\tMULTIPLICATION TABLE', end='\n\n')
        print('\t|***********************************|\n')

        corrected_num = N + 1
        for i in range(1, corrected_num):
            print('i=', '{:2d}'.format(i), '|', end='')
            for j in range(1, corrected_num):
                # print('{:4d}'.format(i*1), end='')
                print('{:4d}'.format(i*j), end='')
            print()

    def main():
        ''' Simple service consumer function that prompt users enter the digit
            however, if the number is out of range(scope), it will display
            error message and loop it through to provide the proper number for execution
            For return, the multiplication_tab() will be called and the results will be displayed as tabulated form
        '''
        num = int(input('Enter the number>_'))

        while num >= 17 or num < 1:
            print('By premise, this table serves upto 16, from 1')
            num = int(input('Enter the number>_'))

        multiplication_tab(num)

    main()

except Exception as err:
    print(err)
