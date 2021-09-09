def isin(lily, ylil):
    counter = 0
    while counter < len(lily):
        i = lily[counter]
        if i not in ylil or lily.count(i) > ylil.count(i): return False
        counter += 1
    return True
main = lambda a, letters: (i for i in open('words_alpha.txt', 'r').read().split() if len(i) <= a and isin(i, letters))
if __name__ == '__main__': print(main(7, 'example'))