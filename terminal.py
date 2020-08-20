commande=True
while commande:
    commande_entree=input(">")
    if commande_entree=="ls":
       continue
    elif commande_entree=="hello":
        print("coucou petit")
        continue
    elif commande_entree=="quit" or commande_entree=="exit":
        break
    else :
        print("commande introuvable")