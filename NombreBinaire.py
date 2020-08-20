def binaire():
    n = int(input("saisir un entier : "))
    while (n < 0):
        n = int(input("saisir un entier:"))
        res=[]
        res.append(n % 2)
        r = n //2
        while (r != 0):
            res.append(r % 2)
            r = r // 2
            res.reverse()
        return res
print(binaire())

