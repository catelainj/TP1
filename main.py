#TP_1_word_count

def count_word(chaine):
    mot = chaine.split()
    nombre_de_mot = len(mot)
    return nombre_de_mot


#demande a utilisateur de écrire une chaine
chaine = input("entre une chaine: \n")
nombre_de_mot = count_word(chaine)
print("nombre de mots est : \n, nombre_de_mot")
