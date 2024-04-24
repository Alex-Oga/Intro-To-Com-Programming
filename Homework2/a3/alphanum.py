# Assignment 3, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:40 hrs
def phoneWord2Num(word: str) -> int:
    answer = '' # Empty string that will contain all the numbers
    word = word.lower() # lowercase all letters so that it would not clash with uppercase letters
    two = ('a','b','c')
    three = ('d','e','f')
    four = ('g','h','i')
    five = ('j','k','l')
    six = ('m','n','o')
    seven = ('p','q','r','s')
    eight = ('t','u','v')
    nine = ('w','x','y','z')
    for letter in word:
        if letter in two:
            answer = answer+'2'
        if letter in three:
            answer = answer+'3'
        if letter in four:
            answer = answer+'4'
        if letter in five:
            answer = answer+'5'
        if letter in six:
            answer = answer+'6'
        if letter in seven:
            answer = answer+'7'
        if letter in eight:
            answer = answer+'8'
        if letter in nine:
            answer = answer+'9'
    return int(answer) # Convert the string into int and return
# assert phoneWord2Num('FLOWERS') == 3569377
# assert phoneWord2Num('PrOGrAM') == 7764726
# assert phoneWord2Num('Battery') == 2288379