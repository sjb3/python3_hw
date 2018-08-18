# H11_sung.py
# short summery: parsing the given string from reading file and return the average of the value

def decipher(filename):
    ''' This function will read file, provided, transform to string and split them by comma(s); sequentially
        Above procedure will RETURN the list then loop it through: empty string will be ignored but non-empty string
        will be changed to integer and saved to new array after stripping
    '''
    line = open(filename, 'r')
    # print(line, type(line))
    new_line = ''.join(line)
    # print(new_line, type(new_line))
    after_split = new_line.split(',')
    # print(after_split, type(after_split))
    new_array = []
    new_el = ''

    for i in range(len(after_split)):
        if after_split[i] == '':
            pass
        else:
            new_el = int(after_split[i].rstrip())
            new_array.append(new_el)

    sum = 0
    for idx in new_array:
        sum += idx
        avg = sum/len(new_array)
        # print(sum, avg)
    return avg

def main():
    ''' First off, this will prompt user(s) to enter the filename;
        subsequently, decipher() will be called and file will be passed to the decipher() function.
        From here, the new array will be iterated to calculate the sum and average for RETURN values
    '''
    user_array = 'H11_Decipher_Sample.txt'
    avg = decipher(user_array)

    print('The average of the given file is: ', avg)

main()
