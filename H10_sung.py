#H10_sung.py

# def calc_salary(filename):
#     read_file = open(filename, 'r')
#     line = read_file.readline()
#     end_of_line = False
#     new_line = line.splitlines()
#     while new_line != '':
#         if new_line == '':
#             print(new_line, type(new_line))
#         else:
#             end_of_line = True
def calc_salary(filename):
    ''' This function will create the basic format for print-out's
        From the file given, this function will read each line and assign to name and salary var's
        and eventually, calculate the average each iteration
    '''
    try:
        read_file = open(filename, 'r')
        end_of_line = False
        name = read_file.readline()
        salary = int(read_file.readline())
        sum = int(salary)
        i = 1
        length = i + 1
        avg_salary = sum
        print('\t|*******************************************************************|\n')
        print('\t\tEmployee\'s name', end='')
        print('\t', '|\tSalary', end='')
        print('\t', '|\tAverage Salary')
        print('\t|*******************************************************************|\n')

        print('\t\t', name.rstrip(), end='')
        print('\t\t', salary, end='')
        print('\t\t', avg_salary)

        while not end_of_line:
            if name == '' or salary =='':
                end_of_line = True
            else:
                name = read_file.readline()
                salary = int(read_file.readline())
                sum += salary
                length = i + 1
                avg_salary = int(sum/length)

                print('\t\t', name.rstrip(), end='')
                print('\t\t', salary, end='')
                print('\t\t', avg_salary)
                i += 1
        return avg_salary
        read_file.close()

    except Exception as err:
        print(err)

def main():
    ''' This will prompt user to enter the file to work on
        After prompting, calc_salary function will be called and return the average
    '''
    working_file = input("Enter the name of the file you wanna work: ")
    avg_salary = calc_salary(working_file)
    # print(type(avg_salary))
    # print('>>>>>', name)

main()
