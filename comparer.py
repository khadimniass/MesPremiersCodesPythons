def comparateur(n1,n2):
    numb1=int(n1)
    numb2=int(n2)
    if numb1<numb2:
        return numb1,"est plus petit que ",numb2
    elif numb1==numb2:
        return numb1, "est egal a ",numb2
    else :
        return numb1, "plus grand que ",numb2
nombre_entree1=input("entrez le premier :")
nombre_entree2=input("enttrez le second nombre")

print(comparateur (nombre_entree1,nombre_entree2))