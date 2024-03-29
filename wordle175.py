


class scrabbleDict:
    # This class is used to make a dictionary of words from a given file
    def __init__(self, size, filename):
        '''
        Object for a Dictionary 
        :param size: the size of word
        :param filename: the name of file
        '''
        self.size = size
        self.filename = filename
        self.newDict = {}
        with open(self.filename, 'r') as file :         # Open the file in reading mode
            for line in file:
                word = line[:size]                      # Get the word from the size 
                definition = line[size:]                # Rest of line is definition
                if len(word) == self.size :
                    self.newDict[word] = definition     # Add the definition to the word

    def check(self, word):
        '''
        Checking a word in the dictionary
        :param word: Enter the word to check in the dictionary
        :return: returns True if the word is in the dictioanry, else False
        '''
        return word in self.newDict.keys()
        
    def getSize(self):
        '''
        Total words in the dictionary
        :return: Total words in the dictionary
        '''
        return len(self.newDict.keys())
        

    def getWords(self, letter):
        '''
        Gives us a list of words starting with a specific letter
        :param: letter ---> the initial word
        :return: a list with all the words with that letter
        '''
        WordsForGivenLetter = []
        for every_key in self.newDict.keys():
            if every_key[0] == letter :                 # comparing the first letter of the key to the input letter
                WordsForGivenLetter.append(every_key)   # If they are same, append to the list

        WordsForGivenLetter.sort()                      # Sort the list
        return WordsForGivenLetter                      # Return the list

    def getWordSize(self):
        '''
        Returns the size of the letters
        '''
        return self.size

    def getMaskedWords(self,template):
        '''
        Gives all the possible words for a given template
        :param Template: a list with template having asterisk "*"
        :return: a list with all the possible words for the given template
        '''
        indexes = []                                            # initialising a list
        wordwithoutasterisk = ''                                # initialising a string
        for eachTemplate in template:
            for index, letter in enumerate(eachTemplate):       # getting the index and character of each word in the template by using enumerate
                if letter != '*':                   
                    wordwithoutasterisk += letter.lower()       # If the letter is sure, we add it to the empty string
                    indexes.append(index)                       # Add the index to the list
        
        possible_words = []                                     # initialising another list for the words
        for word in self.newDict.keys():                        
            dictword = ''
            for i in indexes:                   
                dictword += word[i].lower()                     # for every word in the dictionary, we add the characters from the same index to the string
            if wordwithoutasterisk == dictword:                 # If the string is same as the old string
                possible_words.append(word)                     # we append that word to the possible words list
        
        return possible_words                                   # Return that list
        

    def getConstrainedWords(self, template, letters):
        '''
        Gives hints for the word
        :param template: a list with template having asterisk "*"
        :param letters: letters which we want to put in the template
        :return : a list with all hints
        '''
        possible_words = self.getMaskedWords(template)          # getting all the possible words from getMaskedWords method
        hints = []                                              # intialising an empty list
        letters = list(''.join(letters).lower())                # converting all the letters into lower case
        for word in possible_words :
            count = 0                                           # intialising a count
            for eachtemplate in template:
                for i in range(len(eachtemplate)):  
                    if word[i] in letters and eachtemplate[i] == '*':   # if the current letter is in the list of letters we want and the it was marked by *
                        count += 1                                  # increase the count by 1
            
            if count >= len(letters):                           # check if all the characters are in the word, even if there are more it still is valid
                hints.append(word)                              # if they are, append it to the empty list

        return hints                                            # return the list
        
