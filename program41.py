#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 7, 2022
#This program that computes LIRR transit fares

def computeFare(zone, ticketType):
    fare = 0
    
    if (zone == 1 and ticketType == "peak"):
        fare = 8.75
    if (zone == 1 and ticketType == "off-peak"):
        fare = 6.25
    if ((zone == 2 or zone == 3) and ticketType == "peak"):
        fare = 10.25
    if ((zone == 2 or zone == 3) and ticketType == "off-peak"):
        fare = 7.50
    if (zone == 4 and ticketType == "peak"):
        fare = 12.00
    if (zone == 4 and ticketType == "off-peak"):
        fare = 8.75
    if (((zone == 5 or zone == 6) or zone == 7) and ticketType == "peak"):
        fare = 13.50
    if (((zone == 5 or zone == 6) or zone == 7) and ticketType == "off-peak"):
        fare = 9.75
    if (zone >= 8):
        fare = -1
    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

if __name__ == "__main__":
     main()
