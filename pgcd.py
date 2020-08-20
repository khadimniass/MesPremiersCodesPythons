#import sympy
def pgdc(a,b):
    while (a%b!=0):
        a,b=b,a%b
        return b
print(pgdc(14,4))
#print(x=sympy.Symbol("x"))