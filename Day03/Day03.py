import string


def get_alfabet_index(input_char):
    if input_char.isupper():
        return 1 + 26 + string.ascii_uppercase.index(input_char)
    else:
        return 1 + string.ascii_lowercase.index(input_char)


# score = 0
# # Read and proces inputfile
# with open('input_day03.txt') as f:
#     for content in f:
#         contentLength = int(len(content) / 2)
#         first_compartment = content[:contentLength]
#         second_compartment = content[contentLength:]
#         print(first_compartment)
#         print(second_compartment)
#         # Create a list for all items in the first compartment and make the items unique
#         first_list = []
#         for x in first_compartment:
#             first_list.append(x)
#         uq_first_list = set(first_list)
#
#         for x in uq_first_list:
#             if second_compartment.find(x) >= 0:
#                 score += get_alfabet_index(x)
#                 print(score)
#
#
# print(score)
def get_group_badge(filename):
    linenumber = 0
    score = 0
    with open(filename) as f:
        for line in f:
            linenumber += 1
            if linenumber % 3 == 1:
                a = line.strip()
            elif linenumber % 3 == 2:
                b = line.strip()
            elif linenumber % 3 == 0:
                c = line.strip()
                print('C is gevonden')
                print(c)
                # Group is complete, start comparison
                list_a = []
                list_b = []
                list_c = []
                for x in a:
                    if x not in list_a:
                        list_a.append(x)
                for y in b:
                    if y not in list_b:
                        list_b.append(y)
                for z in c:
                    if z not in list_c:
                        list_c.append(z)
                for x in list_a:
                    try:
                        index_b = list_b.index(x)
                    except ValueError:
                        index_b = -1
                    try:
                        index_c = list_c.index(x)
                    except ValueError:
                        index_c = -1

                    if index_b >= 0 and index_c >= 0:
                        score += get_alfabet_index(x)
                        print(get_alfabet_index(x))
                        print(score)
    return score

get_group_badge('input_day03.txt')
