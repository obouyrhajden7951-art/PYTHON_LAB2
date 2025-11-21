# Étape 1 – Créer des variables de types différents

entier = 42              # int
flottant = 3.14          # float
texte = "Python"         # str
vrai_ou_faux = True      # bool


# Étape 2 – Vérifier les types avec type()


print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))


# Étape 3 – Convertir des chaînes en nombres


age_str = input("Quel âge as-tu ? ")
print("Tu as saisi :", age_str, "→", type(age_str))

age = int(age_str)
print("Après conversion :", age, "→", type(age))



# Étape 4 – Réaffectation vs recréation d’une variable

nombre = 10
print(nombre)

nombre = 10 + 5
print(nombre)

liste = [1, 2, 3]
liste.append(4)
print(liste)
