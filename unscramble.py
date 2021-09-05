def main(a, letters):
    foundWords = []
    eng = open('words_alpha.txt', 'r')  #open the file in read mode
    file_content = eng.read()   # read the file
    word_list = file_content.split()    # split method turns it into a list
    necessary_words = []
    for i in word_list: # this loop traverses the list and creates a new list containing all words of length a
        if len(i) in range(a+1):
            necessary_words.append(i)
    # now the variable necessary_words contains a list of all words of length a.
    for j in necessary_words:
        if isin(j, letters):
            foundWords.append(j)

    return foundWords
        
def freql(w, lst): # used to find the frequency of a particular object in its iterable object 
    count = 0 # if it doesn't appear freql returns zero
    for i in lst: # tranverses the container
        if i == w:
            count += 1 # adds to the count frequency
    return count
	       
def isin(lily, ylil): # used to confirm if a word can be gotten from another word
    a = lily
    b = ylil
    for i in a: 
     if i not in ylil or freql(i, a) > freql(i, b): # first condition to confirm whether they have the same letters
      return False
    return True

if __name__ == '__main__':
    print(main(7, 'example'))