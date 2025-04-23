#creating a function that returns the power of a number
#it accepts Number and Exponent values as parameters
def findPower(number, exponent):
    #initializing the result variable to 1(It stores the resultant power)
    resultPower = 1
    #transversing in the range from 1 to given exponent+1
    for i in range(1, exponent + 1):
        #   Multiplying the resultPower with the given number
        resultPower = resultPower * number
    #returning the resultant power
    return resultPower