def find_elf(filename):
    calories = 0
    best_elf = 0
    top_3 = list()

    print('Openen van file: ' + filename)
    with open(filename) as f:
        for line in f:
            l = line.strip()
            check_digitl = l.isdigit()
            if check_digitl:
                calories += int(l)
            else:
                top_3.append(calories)
                if calories > best_elf:
                    best_elf = calories
                calories = 0


    print('Beste Elf is: ' + str(best_elf))
    top_3.sort(reverse=True)
    print('Total calories of top 3 elves: ' + str(sum(top_3[:3])))


find_elf('input.txt')
