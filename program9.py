#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: February 19, 2022
#This program prompts the user to enter a word and then prints out the word with each letter shifted right by 13

word = input("Enter a Word:")
newWord = ""
for c in word:
    offset = ord(c) - ord('a')+13
    wrap = offset % 26
    newChar = chr(ord('a') + wrap)
    print(wrap, chr(ord('a') + wrap))
    newWord = newWord + newChar

print("The coded word (with wrap) is", newWord)
