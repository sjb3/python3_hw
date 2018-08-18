#
# def sum_sqr(list):
#     results = 0
#     for i in list:
#         results += i **2
#         # print(results)
#     return results
#
# def main():
#     given = [1,3,5]
#     results = sum_sqr(given)
#     print(results)
# main()
#
# try:
#     def incrementBy2():
#         my_list = [5,8,14,22]
#         for i in range(len(my_list)):
#             my_list[i] += + 2
#         return my_list
#
#     def main():
#         my_list = incrementBy2()
#         print(my_list)
#     main()
#
# except Exception as err:
#     print(err)

def getLargest(list):
    if len(list) == 0:
        return list

    largest = list[0]
    idxLargest = 0
    for idx in range(len(list)):
        current = list[idx]

        if current > largest:
            largest = current
            idxLargest = idx

    return largest, idxLargest

def main():
    given = [45, 16, 3, -20, 9, 26, 35, -11, 14, 4]
    largest, idxLargest = getLargest(given)
    print(largest, end=', ')
    print(idxLargest)
main()

# def start_p(list):
#     new_list = []
#     for el in list:
#         if el.startswith('p') or el.startswith('P'):
#             new_list.append(el)
#             or new_list += [el]
#         else:
#             pass
#
#     return new_list
#
# def main():
#     a = ['alpha', 'popo', '', '', 'beta', 'gamma', 'pi']
#     new_list = start_p(a)
#
#     print(new_list)
#
# main()

# Kai's approach
# def start_p(list):
#     new_list = []
#     for el in list:
#         if len(el) > 0 and list[0] == 'p':
#
#             or new_list += [el]

#
