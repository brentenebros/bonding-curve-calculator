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
c = float(input('\n\n\nFor your BuyCurve, you need a factor to measure the increase of token price. \n'
'For example, if you want the factor to be a doubling of tokens, enter 2. \n'
'Enter the desired base for the factor increase:'))
a = float(input('\n\n\nFor your BuyCurve, you need to set a desired price growth per your increase factor. \n'
'For example, if you want the token cost to increase by 25% every factor, enter 0.25. \n'
'Enter your desired price growth:'))

#Query inputs for SellCurve
m = float(input('\n\n\nFor your SellCurve, you may want a Divergent_SellCurve.\n'
'This will maintain a relative difference between both curves, but a growing absolute difference.\n'
'Enter a discount value to your BuyCurve (i.e. 0.9 for 10% discount)- leave blank if you do not want a Divergent_SellCurve:') or '1') #m is a multiplicative factor that adjusts the ‘slope’ of the curve defined.
b = float(input('\n\n\nFor your SellCurve, you may want a ConsistentlyDivergent_SellCurve.\n'
'This will capture an absolute value when minting new tokens, and maintain a consistent absolute difference.\n'
'Enter your discount value per token - leave blank if you do not want a ConsistentlyDivergent_SellCurve:') or '0') #b is a constant that adjusts the functions in the spirit of y = mx + b

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
