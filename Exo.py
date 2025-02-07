
from itertools import product

def afficher_table_verite(fonction):
    variables = fonction.__code__.co_varnames
    n = len(variables)
    print("Table de vérité pour la fonction logique:")
    print(" | ".join(variables) + " | Résultat")
    print("-" * (n * 4 + 9))
    
    for valeurs in product([False, True], repeat=n):
        resultat = fonction(*valeurs)
        print(" | ".join(str(int(v)) for v in valeurs) + " | " + str(int(resultat)))

def premiere_forme_canonique(fonction):
    variables = fonction.__code__.co_varnames
    n = len(variables)
    mintermes = []
    
    for valeurs in product([False, True], repeat=n):
        if fonction(*valeurs):
            minterme = ' AND '.join(f"{var}" if val else f"NOT {var}" for var, val in zip(variables, valeurs))
            mintermes.append(f"({minterme})")
    
    return " OR ".join(mintermes)

def seconde_forme_canonique(fonction):
    variables = fonction.__code__.co_varnames
    n = len(variables)
    maxtermes = []
    
    for valeurs in product([False, True], repeat=n):
        if not fonction(*valeurs):
            maxterme = ' OR '.join(f"NOT {var}" if val else f"{var}" for var, val in zip(variables, valeurs))
            maxtermes.append(f"({maxterme})")
    
    return " AND ".join(maxtermes)

# Exemple de fonction logique
def fonction_logique(w,x,y,z):
    return (w and x) or(x and y) or (y and z)
    

# Affichage de la table de vérité
afficher_table_verite(fonction_logique)

# Affichage des formes canoniques
print("Première forme canonique :")
print(premiere_forme_canonique(fonction_logique))
print("Seconde forme canonique :")
print(seconde_forme_canonique(fonction_logique))