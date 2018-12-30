from numpy import *
from matplotlib.pyplot import *

#define the buy curve
def f1(x):
    return 1*((1+a)**z)+0
#define the sell curve
def f2(x):
    return m*((1+a)**z)+(-b)

x = linspace(0.1, 100000, 500) #(start, end, how many points plotted)

#Query inputs for BuyCurve
print("For your BuyCurve, you need a factor in which the price of the token will increase. For example, if you want the factor to be a doubling of tokens, enter 2.")
c = float(input('Enter the desired base for the factor increase:'))

print("For your BuyCurve, you need to set a desired price growth per your increase factor. For example, if you want the token cost to increase by 25% every factor, enter 0.25.")
a = float(input('Enter your desired price growth:'))

#Query inputs for SellCurve
print("For your SellCurve, you may want a Divergent_SellCurve. This will grow the difference between the BuyCurve and SellCurve as the supply increases.")
m = float(input('Enter a discount value to your BuyCurve (i.e. 0.9 for 10% discount)- leave blank if you do not want a Divergent_SellCurve:') or '1') #m is a multiplicative factor that adjusts the ‘slope’ of the curve defined.

print("For your SellCurve, you may want a ConsistentlyDivergent_SellCurve. This will capture an absolute value when minting new tokens, and maintain a consistent offset between the two curves.")
b = float(input('Enter your discount value per token - leave blank if you do not want a ConsistentlyDivergent_SellCurve:') or '0') #b is a constant that adjusts the functions in the spirit of y = mx + b

z = log(x)/log(c)
y1 = f1(x)  #buy curve
y2 = f2(x) #sell curve

plot(x, y2, 'g-')
plot(x, y1, 'b-')
xlabel('Project-Specific Tokens')
ylabel('RLP')
legend(['SellCurve', 'BuyCurve'])
title('Buy and Sell Bonded Curves')
show()
