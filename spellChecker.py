from difflib import SequenceMatcher


def binarySearch(dictionary, word):
    """finds a word in a dictionary, using binary search"""

    if len(dictionary) == 0:
        return False
    else:
        mid = len(dictionary) // 2

        if dictionary[mid] == word:
            return True

        elif dictionary[mid] > word:
            return binarySearch(dictionary[:mid], word)

        elif dictionary[mid] < word:
            return binarySearch(dictionary[mid + 1:], word)


def findSuggestions(alist):
    """ Get the best matches and put them in the first of the dictionary """
    bestList = ['', '', '']
    n = len(alist)
    for i in range(3):
        maxValue = alist[0]
        maxPosition = 0
        for j in range(1, n):
            if alist[j] > maxValue:
                maxValue = alist[j]
                maxPosition = j

        # Swap the ratio numbers
        alist[maxPosition] = -1
        # Swap the words
        bestList[i] = dictionary[maxPosition]

    return bestList


def readFile(fileName):
    """ reads words from text file into list """
    fileDictionary = open(fileName, 'r').read()
    dictionaryList = fileDictionary.split('\n')
    return dictionaryList


def displayError(suggestions, wrongWord):
    """Display the errors ..."""

    print("\n", wrongWord, "is WRONG, Do you mean: ")
    for i in range(len(suggestions)):
        print("_", suggestions[i])
    print('_' * 30)


def skipPunctuation(word):
    """ skip punctuation in word """
    if "'" in word:
        split = word.split("'")
        word = split[0]

    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # remove punctuation from the string
    wordWithoutPunctuation = ""
    for char in word:
        if char not in punctuations:
            wordWithoutPunctuation = wordWithoutPunctuation + char

    # display the un-punctuated string
    return wordWithoutPunctuation


if __name__ == "__main__":
    # Read all words in the file and put them in list
    print("when you want to stop, please press enter two consecutive enters")
    dictionary = readFile('Dictionary.txt')
    phrase = []
    print("Please enter your statements:")
    while True:
        # user input
        phrases = input()
        if len(phrases) == 0:
            break
        phrase.append(phrases)

    for phraseInPhraseList in phrase:
        phraseInPhraseList = phraseInPhraseList.split(' ')

        for word in phraseInPhraseList:
            word = skipPunctuation(word)
            # Check if the entered word is correct or not
            if binarySearch(dictionary, word):
                print(word, end=' ')

            else:
                # Get similarity ratio of the words and put them in list
                ratio = [SequenceMatcher(None, word, wordInDictionary).ratio() for wordInDictionary in dictionary]
                # put the best three matches in the first of the list
                best = findSuggestions(ratio)
                # display error
                displayError(best, word)
