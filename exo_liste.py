liste1 = ["a","b","c"]
liste2 = ["ananas", "banane", "citron"]

#print(liste1[0])

#il va imprimer l'element qui est dans la position que je lui demande
#! ca commence par 0
#si on met un numero qui est trop loin (ex ici 5), on a un message d'erreur ("list index out of range")

#index = liste1.index("a")
#print("postion de la lettre =", index)

#on veut qu'il affiche le fruit de la liste2 qui correspond a la lettre de la liste1
#positions des lettres : a=0, b=1, c=2
#positions des fruits : ananas=0, banane=1, citron=2
print("quelle lettre voulez-vous? a->c")
lettre = input("-->")

index=liste1.index(lettre)
print(liste2[index])
