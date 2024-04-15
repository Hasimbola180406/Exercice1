from itertools import product

def fonction_logique(A, B):
    # Exemple de fonction: A AND B
    return A and B

def generer_table_de_verite(func):
    variables = [0, 1]  # 0 pour faux, 1 pour vrai
    table = []

    for values in product(variables, repeat=2):
        resultat = func(*values)
        table.append((*values, resultat))
    
    return table

def forme_canonique(table):
    fnd = []
    fnc = []

    for ligne in table:
        A, B, resultat = ligne
        if resultat:
            fnd.append(f"({'A' if A else '~A'} AND {'B' if B else '~B'})")
        else:
            fnc.append(f"({'A' if not A else '~A'} OR {'B' if not B else '~B'})")
    
    # Joindre les expressions avec OR pour FND et AND pour FNC
    fnd_expression = " OR ".join(fnd)
    fnc_expression = " AND ".join(fnc)

    return fnd_expression, fnc_expression

# Génération de la table de vérité
table = generer_table_de_verite(fonction_logique)

# Affichage de la table de vérité
print("A B | F(A,B)")
print("---------")
for ligne in table:
    print(f"{ligne[0]} {ligne[1]} | {ligne[2]}")

# Calcul des formes canoniques
fnd, fnc = forme_canonique(table)

print("\nForme Normale Disjonctive (FND):", fnd)
print("Forme Normale Conjonctive (FNC):", fnc)
