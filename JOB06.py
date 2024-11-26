
N = int(input("choisissez un nombre entier supérieur à 0 : "))
print(f"Les 7 premiers résultats de la table de multiplication de {N} est de :")

i = 0
while i < 7:
    print(f"{i} x {N} = {i * N}")
    i = i + 1
