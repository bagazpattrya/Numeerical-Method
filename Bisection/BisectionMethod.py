#NUMERICAL BISECTION METHOD
#Written by Bagaz Pattrya.

import math

def f(x):
    return math.pow(x,3) - 3*x + 1 #write your function here


def forBisectionTol(a, b, iteration, tolerance):
    for i in range(0, iteration):
        c = (a+b)/2
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        print(i, a, b, c, f(c), f(a))   # round(c, 5), round(f(c), 5), round(f(a), 5))
        if abs(f(c)) < tolerance:       #check for tolerance, im not really sure whether i should make it absolute value or not, any idea?
            print("tolerance reached")
            break
    return c

startingNumber = float(input("Enter starting point!\nStarting point = ")) #starting number
endNumber = float(input("Enter end point!\nEnd Point = "))              #end number
iterationCount = int(input("Iteration Number\nIterationNum = "))        #how many you want the function to iterate?
tolerance = float(input("enter the maximum tolerance! tolerance = "))   #tolerance, write it on float valu like 0.01, 0.001, etc
print("i a b x f(x) f(a)")

forBisectionTol(startingNumber, endNumber, iterationCount, tolerance)

input("press any key to continue....")