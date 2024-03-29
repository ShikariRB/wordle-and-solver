#----------------------------------------------------
# WORDLE
# 
# Author       - Rakshit .
# CCID         - rakshit2
#----------------------------------------------------


words = []                                                  # Initialise a list
file1 = open('word5Dict.txt','r')                           # Open the corrupted file in read mode
for line in file1:
    single_word = line.strip('\n').strip('#').split('#')    # For every line, we split with '#' and strip '#' and '\n'
    words += single_word                                    # Adding this word to the list
file1.close()                                               # Closing the file
file2 = open('scrabble5.txt','w')                           # Opening the new file in Write mode
for word in words:                                          
    file2.write(word + '\n')                                # Writing every word in a new line
file2.close()                                               # Closing the file