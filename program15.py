#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: February 27, 2022
#This program makes the pseudocode as a complete program

s = input("Enter a string: ")
Ls = len(s)
print(s)

for i in range(0,ls-1):
    print(s[0:i])
    for i in range(0,ls-1):
        print(s[i:ls])

print("Thank you for using my program!")
