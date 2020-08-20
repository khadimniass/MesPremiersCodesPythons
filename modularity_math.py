#ax^2+bx+c=0
import math
print("entrez les coefficients :")
a=input("a  = :")
b=input("b = :")
c= input("c= :")
a=float(a)
b=float(b)
c=float(c)
if a!= :
    d=b*b-4*a*c
    D=float(d)
    if D>0:
        x1=(-b-math.sqrt(D))/2*a
        x2=(-b+math.sqrt(D))/2*a
        print("l'équation a deuxx solutions : ",x1,x2)
    elif D==0 :
        x0=-b/2*a
        print("x0 = :",x0)
    else :
        print("l'equation n'a pas de solution")