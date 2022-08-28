#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 03, 2022
#This program fills in the missing function

def monthString(monthNum):
    monthString = ""

    if monthNum == 1:
        return("January")
    elif monthNum == 2:
        return("February")
    elif monthNum == 3:
        return("March")
    elif monthNum == 4:
        return("April")
    elif monthNum == 5:
        return("May")
    elif monthNum == 6:
        return("June")
    elif monthNum == 7:
        return("July")
    elif monthNum == 8:
        return("August")
    elif monthNum == 9:
        return("September")
    elif monthNum == 10:
        return("October")
    elif monthNum == 11:
        return("November")
    elif monthNum == 12:
        return("December")
    else:
        return(monthString)

def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)
if __name__ == "__main__":
     main()
