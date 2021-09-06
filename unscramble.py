def main(a, letters):
    foundWords = []
    eng = open('words_alpha.txt', 'r') 
    file_content = eng.read()  
    word_list = file_content.split()   
    for i in word_list: 
        if len(i) <= a and isin(i, letters):
            foundWords.append(i)
    return foundWords

def isin(lily, ylil):
    for i in lily: 
        if i not in ylil or lily.count(i) > ylil.count(i):
            return False
    #all([False for i in lily if i not in ylil or lily.count(i) > ylil.count(i)])
    return all

if __name__ == '__main__':
    print(main(7, 'example'))