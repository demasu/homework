def main():
    totalEmployees = 0
    counter = 1
    todayEmployees = 0
    totalPayout = 0
    keepGoing = 'y'

    while keepGoing == 'y':
        totalEmployees = getEmployees(totalEmployees, todayEmployees, counter)
        totalPayout = calcPayout(totalPayout, totalEmployees)
        printInfo(totalEmployees, totalPayout)

        keepGoing = raw_input("Do yu want to run the program again? (y for yes, n for no)")

def getEmployees( totalEmployees, todayEmployees, counter):
    while counter <= 7:
        todayEmployees = input( "Enter number of employees sent out that day ")
        totalEmployees += todayEmployees
        counter += 1
    return totalEmployees

def calcPayout( totalPayout, totalEmployees):
    totalPayout = 0
    totalPayout = totalEmployees * 2.5
    return totalPayout

def printInfo(totalEmployees, totalPayout):
    print "Total number of employees sent out is: " 
    print totalEmployees
    print "Total payout is: "
    print totalPayout

main()