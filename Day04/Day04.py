def expand_section(section):
    i = section.index('-')
    pair_from = int(section[0:i])
    pair_to = int(section[i+1:])
    p = int(pair_from)
    while p >= pair_from and p <= pair_to:
        print(p)
        p += 1


def section_min(section):
    i = section.index('-')
    return int(section[0:i])


def section_max(section):
    i = section.index('-')
    return int(section[i+1:])


def ranges_overlap(pair):
    section1 = pair[0:pair.index(',')]
    section2 = pair[pair.index(',')+1:]
    s1_start = section_min(section1)
    s1_end = section_max(section1)
    s2_start = section_min(section2)
    s2_end = section_max(section2)

    if (s1_start <= s2_start and s1_end >= s2_end) or (s2_start <= s1_start and s2_end >= s1_end):
        return 1
    else:
        return 0


def camp_cleanup_part_1(filename):
    score = 0
    with open(filename) as f:
        for line in f:
            l = line.strip()
            score += ranges_overlap(l)
    print('Total assignment pairs where one range fully contain the other? Answer: ' + str(score))
    return score

camp_cleanup_part_1('input_day04.txt')