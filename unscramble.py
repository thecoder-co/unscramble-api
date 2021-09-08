def isin(lily, ylil):
    count = 0
    while count < len(lily):
        i = lily[count]
        if i not in ylil or lily.count(i) > ylil.count(i): return False
        count += 1
    return True
main = lambda a, letters: (i for i in open('words_alpha.txt', 'r').read().split() if len(i) <= a and isin(i, letters))
if __name__ == '__main__': print(main(7, 'example'))