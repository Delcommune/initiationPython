#on nous affiche "Tapez une lettre"
#on entre une lettre
#le programme nous retourne les symboles correspondants

#retrouver la position de la lettre dans l'alphabet
#afficher le code morse correspondant a l'index trouve


import liste_morse
#pour importer la librairie
#! toujours importer les librairies en debut de code

print("Tapez une lettre")
lettre=input("--->")



index=liste_morse.alphabet.index(lettre)
print(liste_morse.morse[index])

#pour lui dire ou trouver les elements, il faut donner le nom de la librairie. avant (ici, "liste_morse.")