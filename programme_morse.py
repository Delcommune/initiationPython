#on nous affiche "Tapez une lettre"
#on entre une lettre
#le programme nous retourne les symboles correspondants

#retrouver la position de la lettre dans l'alphabet
#afficher le code morse correspondant a l'index trouve


from tkinter import Variable
import liste_morse
#pour importer la librairie
#! toujours importer les librairies en debut de code

#print("Tapez une lettre")
#lettre=input("--->")

print("Tapez un mot")
mot=input("--->")
code=""
#pour poser qu'on va entrer une chaine de caracteres

#pour chaque lettre dans le mot, on encode la lettre en morse
#une fois le mot encode, on l'affiche
for lettre in mot:
    code=code+liste_morse.encode(lettre)
    code=code+" "
#pour mettre des espaces entre chaque lettre


#on appelle notre fonction encode dans notre librairie et on stocke le code recupere
#code=liste_morse.encode(lettre)
print(code)

#pour lui dire ou trouver les elements, il faut donner le nom de la librairie. avant (ici, "liste_morse.")

print("entrez un code morse")
code=input("--->")
mot=""


liste_code=str.split(code," ")
print(liste_code)

#pour chaque element de la liste_code,
#on recupere la lettre correspondante
#et on la stocke dans la variable mot

for element in liste_code:
    mot=mot+liste_morse.decode(element)

print(mot)
