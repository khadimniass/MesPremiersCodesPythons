
p=int(input("entrez le nombre premier p: "))
x=int(input("entrez l'entier x: "))
i=1;ord=0
while(True):
    if(x**i%p==1):
        ord=i
        break
    i+=1
print("ordre de ",ord)

def ordre(p,x):
    p,x=int(p),int(x)
    compteur,ordr=1,0
    while(True):
        if (x**compteur%p==1):
            ordr=compteur
            break
    compteur+=1
    return ordr