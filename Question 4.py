wordList = ['apple', 'mango', 'apple', 'orange', 'orange', 'apple', 'guava', 'mango','mango']

def findWordsWithFrequency(N,wordList):
    
    freq = N
    set_wordList = set(wordList)
    counts = {item:wordList.count(item) for item in set_wordList}
    for item in counts:
        if counts[item] == freq:
            print(item)

            
findWordsWithFrequency(3,wordList)
