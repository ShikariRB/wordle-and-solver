
from wordle175 import scrabbleDict


def counter(instanceofclass):
    '''
    This function is used to count the number of characters in the whole dictionary
    :param instanceofclass: An instance of the scrabbleDict class is used to access the dictionary
    :return: A dictionary with all the letters as keys and their count as values
    '''
    dict = {}                                       # initalising a  dictionary
    for word in instanceofclass.newDict.keys():     
        for char in word:
            if char in dict.keys():                 # if the character is in the alphabets
                dict[char] += 1                     # we increment it by 1
            else:
                dict[char] = 1                      # else we keep it as it is

    dict = sorted(dict.items())                     # sort the dictionary
    return dict


def inputValidator(instanceofclass): 
    '''
    This function is used to validate the input from the user
    :param instanceofclass: An instance of the scrabbleDict class is used to access the dictionary
    :return: None
    '''
    invalidInput = False
    while not invalidInput:
        temp = []                                                                   # Initalising an empty list for input  
        totalWildcards = 0                                                          # Counter for wildcards
        inputTemplate = input('Please Enter your Template: for words that you are not sure about, enter "*" : ')    # taking the input
        for star in inputTemplate:
                        if star == '*':
                            totalWildcards += 1             # counting the number of wildcards
        temp.append(inputTemplate)                          # appending the input into the list
        if len(inputTemplate) != instanceofclass.getWordSize():
            print('This Template is invalid. Please input a valid Template.')           # validating the input
        else:
            invalidInputAdditional = False
            while not invalidInputAdditional:       
                letters = input('Please Enter any additional letters for more help. If you wish to skip this, press Enter: ')   # asking for letters
                if len(letters) == 0:
                    possibleWords = instanceofclass.getMaskedWords(temp)        # if there is no letter inputed
                    print('\n'.join(possibleWords))                             # we print all the possible solutions
                    invalidInput = True
                    invalidInputAdditional = True
                else:   
                    if len(letters) > totalWildcards:                           # validating the input of letters
                        print('Not Enough Wildcards. Please try again!')
                        invalidInputAdditional = False
                    else:
                        hints = scrabbleDict.getConstrainedWords(instanceofclass, temp, letters)    # if the input is valid
                        print('\n'.join(hints))                                                     # print all the hints
                        invalidInputAdditional = True
                        invalidInput = True


def main():
    filename = 'scrabble5.txt'
    size = 5
    instanceofclass = scrabbleDict(size, filename)          # making an instance of the class

    inputValidator(instanceofclass)                         # calling input validator method
    
if __name__ == '__main__':
    main()


