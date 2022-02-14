# I. Variables
#boite qui contient une valeur (comme cellules Excell)
var1 = 5 #nombre entier, integer number #integer
var2 = 4.2 #nombre decimal, floating point number #float 
var3 = "bonjour" #chaine de caracteres, string #string
var4 = True #bouleen #boolean
var5 = ["bonjour", 5, 3.5] #liste (plusieurs valeurs ; elles peuvent etre de types differents) #liste

#! on separe les elements d'une liste avec une virgule
#! les virgules des chiffres s'ecrivent en point

total = var1 + var2

print(total) #!toujours () apres print
#fonction qui permet d'imprimer dans le terminal (jusque la il avait juste noté que les variables existent et calcule le total)

# II. Conditions
if var1 > var2: #!toujours mettre : et à la ligne apres une condition (sinon il ne comprend pas que la condition est finie)
    print("c'est plus grand")
elif var1 < var2: #elif = contraction de else if, et si
    print("c'est plus petit")
else: #il n'y a jamais de condition apres un else ! aux deux points
    print("c'est egal")

#NB si on veut tester tout ca, il faut changer les valeurs des variables au-dessus
#NB on peut avoir autant de (el)if qu'on veut
#NB il vaut meixu toujours mettre un else, histoire d'avoir une valeur par defaut

# III. Boucles
#principe d'une boucle: repeter une instruction
while var1 > var2: #! toujours :, c'est aussi une instruction
    print(var1)
#si on executait maintenant, on aurait une boucle infinie: il repeterait tout le temps 5
#pour arreter une boucle infinie: ctrl c
    var1 = var1 - 1
for element in var5: #for each, pour chaque #var5, c'est le nom de notre liste (ici)
    print(element) 
#for, pas de condition, il parcourt juste tous les elements


print("---------------")
#pour s'y retrouver

# IV. Fonctions
# micro-programme qui permet d'executer une (suite d')instruction(s)
# ! toujours la definir avant de pouvoir l'utiliser (def)
def add(a,b): #def est une instruction donc il faut deux points
    resultat = a + b
    return resultat

total = add(var1, var2)  
print(total)


