def find_elf(filename):
    calories = 0
    bestElf = 0
    print('Openen van file: ' + filename);
    with open(filename) as f:
        for line in f:
            l = line.strip()
            checkDigitl = l.isdigit()
            if checkDigitl:
                calories += int(l)
            else:
                if calories > bestElf:
                    bestElf = calories

                print('Current Calories: ' + str(calories))
                print('Current bestElf: ' + str(bestElf))
                calories = 0

    print('Beste Elf is: ' + str(bestElf))

find_elf('input.txt')