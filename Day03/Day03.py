import string


def get_alfabet_index(input_char):
    if input_char.isupper():
        return 1 + 26 + string.ascii_uppercase.index(input_char)
    else:
        return 1 + string.ascii_lowercase.index(input_char)
#
# print(get_alfabet_index('a'))
# print(get_alfabet_index('A'))


score = 0
# Read and proces inputfile
with open('input_day03.txt') as f:
    for content in f:
        contentLength = int(len(content) / 2)
        first_compartment = content[:contentLength]
        second_compartment = content[contentLength:]
        print(first_compartment)
        print(second_compartment)
        # Create a list for all items in the first compartment and make the items unique
        first_list = []
        for x in first_compartment:
            first_list.append(x)
        uq_first_list = set(first_list)

        for x in uq_first_list:
            if second_compartment.find(x) >= 0:
                score += get_alfabet_index(x)
                print(score)


print(score)
