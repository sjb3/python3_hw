
# end_of_line = False
# number_file = open('numbers.txt', 'r')
# total = 0
# count = 0
#
# while not end_of_line:
#         number = number_file.readline()
#         if number == '':
#             end_of_line = True
#         else:
#             total += float(number)
#             count +=1
#
# print('There were ', count, 'numbers, totalling', total)
# number_file.close()

# end_of_line = False
# words_file = open('words.txt', 'r')
#
# blank_count = 0
# non_blank_count = 0
# # line_count = 0
# i = 0
#
# while not end_of_line:
#     count_line = words_file.readline()
#     # print(count_line)
#
#     if count_line == '':
#         # blank_count += 1
#         end_of_line = True
#         # i += 1
#         # print(count_line)
#     else:
#         # non_blank_count += 1
#         i += 1
#         # print(len(count_line))
#         if len(count_line) > 1:
#             non_blank_count += 1
#
# print('This file has', non_blank_count, 'non-blank lines out of a total of ', i, 'lines', end= '')
# words_file.close()

def main():
    end_of_line = False
    nouns_file = open('nouns.txt', 'r')

    vowels = 'aeiouAEIOU'

    while not end_of_line:
        read_noun = nouns_file.readline()
        if read_noun == '':
            end_of_line = True
        else:
            if read_noun[0] in vowels:
                print(read_noun, end='')

        # else:
        # for startswith() you can pass single char only, BUMMER!
        #     if read_noun.startswith('a'):
        #         print(read_noun, end='')
    nouns_file.close()

main()
