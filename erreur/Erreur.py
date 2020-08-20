ageUser=input("Donnz votre age: ")
try:
    ageUser=int(ageUser)
except:
    print("L'age indiqué est erroné")
else:
    '''ce qui se passe en cas de reussite'''
    print("Tu as ",ageUser, "ans")
finally:
    print("Fin programme...")