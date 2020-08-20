import math
a=int (input("entrez un nombre : "))
b=False
for i in range(2,int(math.sqrt(a))):
     if a%i==0:
      b=True
if b:
  print(a, " est un nombre premier")
else :
    print(a, " n'est pas un nombre premier")