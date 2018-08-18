#
# def main():
#     for i in range(6):
#         print(i, end='')
#
#         for j in range(i):
#             print('*', end='')
#         print('#')
#     # for i in range(6):
#     #     line = '#'
#     #     for j in range(i):
#     #         line += ',' + '3'
#     #     print(line)
# main()


def print_magic_lines(Nlines):
    for i in range(Nlines):
    # prepare a line to print
        line = ''
    # populate line to contain desired pattern
        for j in range(10):
            line += str(j)*(i+1)
            # print(line)
    # print the prepared line
        print()
        print(line)

def main():
    # print('Print magic lines(3)')
    # print_magic_lines(3)
    print('Print magic lines(3)')
    print_magic_lines(3)

main()

# def print_equations(Nlines):
#     for i in range(1, Nlines+1):
#         line = ''
#         total = 0
#         line_total = ''
#         for j in range(1, i+1):
#             term = j**2
#             total += term
#             line = (str(term) + ' + ')
#             # each_line = line[:-2]
#             # new_line = line[:-2]
#             # print(type(line))
#             print(line, end='')
#             # print('>>>', total)
#             # print(new_line)
#         # print('>>>>', line[:-2])
#         # print()
#             # num += str(new_j)
#         line_total += ' = ' + str(total)
#         print(line_total)
#         # print(total, end='/')
#         # print(num)
# def main():
#     print_equations(4)
# main()
