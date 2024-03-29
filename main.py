
import random
from wordle175 import scrabbleDict

def WordChecker(guessedWord, targetWord):
    '''
    This function is used to check the input and give out all 3 lists, namely RED, ORANGE and GREEN
    :param guessedWord: This is a string of input word
    :param targetWord: This is the string of word that we require
    :return: a formatted return statement with all 3 lists
    '''
    guessedWord = guessedWord.lower()                   # converting the word into lowercase letters
    guessd = {}                                         # intialising a dictioanry
    for char in guessedWord:
        guessd[char] = guessedWord.count(char)          # taking the character as key and storing its count as value
    

    guessl = []                                                                     # intialising a list
    for char in guessedWord:
        if guessd[char] == 1 and guessedWord.count(char) == 1:                      # if the current count is 1 and the intial count was 1 as well 
            guessl.append(char)                                                     # then we append that character to the list as it is
        else:                                                                       # otherwise, we change the format to add the count number
            guessl.append(f'{char}{guessedWord.count(char) - guessd[char] + 1}')    # append it to the list with characters
            guessd[char] -= 1                                                       # decrease the value of that character by 1 for the next value


    RedList = []                                    # intialising required lists
    OrangeList = []
    GreenList = []
    orangeguess = []
    targetWord = targetWord.lower()                 
    for i in range(len(guessedWord)) :
        if guessedWord[i] not in targetWord :       # if the letter is not in target word, append it to the RED list
            RedList.append(guessl[i].upper())
        else:
            if guessedWord[i] == targetWord[i]:       # if the letter is at the same position(index) as the target word
                targetWord = targetWord[:i] + '$' + targetWord[i+1:]
                GreenList.append(guessl[i].upper())     # add it to the green list
            else :
                orangeguess.append(guessl[i].upper())    # else add it to the orange guess list
            
    for c in orangeguess:                           # for every character in orange guess list
        c = c.lower()                               # convert it to lower
        if len(c) > 1:                              # if the character is alphanumeric
            if c[0] not in targetWord:              # we check only the alphabetical part of the word
                RedList.append(c.upper())           # if not in the target word, we add it to redlist
            else:
                OrangeList.append(c.upper())        # else we add it to orange list
        else:
            if c not in targetWord:                 # we check the same conditions for non alphanumeric words
                RedList.append(c.upper())
            else:
                OrangeList.append(c.upper())

    GreenList.sort()
    GreenList = ', '.join(GreenList)                # sorting and formatting the lists as required
    
    OrangeList.sort()
    OrangeList = ', '.join(OrangeList)
    
    RedList.sort()
    RedList = ', '.join(RedList)

    return (f'{guessedWord.upper()} GREEN={{{GreenList}}} - ORANGE={{{OrangeList}}} - RED={{{RedList}}}')   # returning the lists in required way
    
    

def game_continue(count):
    '''
    This is used to tell if the game should be continued or not
    :param count: the number of times the loop ran
    :return: A bool which should be true if the game should continue   
    '''
    if count == 7:
        gamenotOver = False
    else :
        gamenotOver = True
    
    return gamenotOver

def main():
    name_of_file = 'scrabble5.txt'
    size = 5
    haanvyiii = scrabbleDict(size, name_of_file)                    # making an object of the class scrabbleDict
    targetWord = random.choice(list(haanvyiii.newDict.items()))     # taking a random word from all the words available to us
    targetWord = targetWord[0]                                      # taking the word only
    
    counter = 1                                                     # intialising a counter
    attemptedWord = []                                              # intialising an empty list for the words which have been attempted
    results = []                                                    # intialising an empty list for results
    while game_continue(counter) and targetWord not in attemptedWord:
        guessedWord = input(f'Attempt {counter}: Please enter a 5 five letter word :')      # taking the input
        # Validating the input
        if len(guessedWord) > haanvyiii.getWordSize():                                      
            print(f'{guessedWord.upper()} is too long')
        elif len(guessedWord) < haanvyiii.getWordSize():
            print(f'{guessedWord.upper()} is too short')
        elif guessedWord in attemptedWord :
            print(f'{guessedWord.upper()} has already been tried')
        elif not scrabbleDict.check(haanvyiii, guessedWord):
            print(f'{guessedWord.upper()} is not a recognised word')
        else:
            attemptedWord.append(guessedWord)                       # if all the the checks are passed, we append the word to attempted words
            validity = WordChecker(guessedWord, targetWord)         # word checker is called to give all 3 lists
            results.append(validity)                                # append the results to results list
            print('\n'.join(results))                               # print all the results in the required waay
            counter += 1                                            # increasing the counter by 1
        
    if guessedWord == targetWord :                                  # if the guessed word is same as target word
        print(f'Found in {counter - 1} attempts. Well done. The word is {targetWord}.')     # print the required output
    else :
        print(f'Sorry you lose. The word is {targetWord}.')         # else print you lose

if __name__ == '__main__' :
    main()