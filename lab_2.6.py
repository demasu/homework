#This program uses modues and variables



#the main module
def main():
    print 'Tire Service Calculator Program \n' # \n
    print #prints a blank line
    serviceCost = input('Enter the tire service cost$')
    serviceCost = float(serviceCost)
    return serviceCost
    #serviceFee = calcServiceFee(serviceCost)

    #input statements
    serviceCost = input('The service cost is: ')
    #input statements
    serviceFee = input('The service fee is: ')
   

#this module will input tire service price
def inputTireServiceCost():
    return

    
#this module will calculate a service fee at 5%
def calcServiceFee(serviceCost):
    #serviceFee = serviceCost * .05
    return serviceFee
    
#this module will calculate serviceTax at 8.25%
def calcServiceTax(serviceCost):
    #totalServiceCost = calcServiceTotal (serviceCost, serviceFee, serviceTax)
    #serviceTax = serviceCost * .0825
    return serviceTax

#this module will calculate serviceFee, serviceTax,
#and the serviceTotal cost
def calcServiceTotal(serviceCost, serviceFee, serviceTax):
    #serviceTotal = serviceCost + serviceFee + serviceTax
    return serviceTotal

#this module will print tireServiceCost, serviceFee,
#serviceTax, and the serviceTotal cost
def printUserInfo(serviceCost, serviceFee, serviceTax, serviceTotal):
    print 'The tire service cost is $', serviceCost
    print 'The tire service fee is $', serviceFee
    print 'The tire service tax is $', serviceTax
    print 'The total amount is $', serviceTotal
   


#this is the main function that starts the program in
#motion
main() #calls main