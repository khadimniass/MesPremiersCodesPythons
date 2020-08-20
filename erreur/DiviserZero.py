a=input("dividende=")
b=input("diviseur")
try:
    a,b=int(a),int(b)
    resultat=a/b

except ZeroDivisionError:
    print("impossible de diviser par zéro")
except ValueError:
    print("Les valeurs saisies sont erronées")
else:
    print(resultat)
finally:
    print("FIN PROGRAMME...")
