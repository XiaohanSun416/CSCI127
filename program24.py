#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 15, 2022
#This program asks the user for a list of nouns and approximates the fraction that are plural by counting the fraction that end in "s"

noun = input("Enter nouns: ")
print("You entered: ", noun)

words = noun.split()
print(words)

number = len(words)
print(number)

for i in noun:
    if i[-1] == "s":
        last = 1
    else:
        last = 0

plural = noun.count("s ")
plurals = plural + last
print(plurals)

fraction = plurals / number
print(fraction)
