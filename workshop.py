print("=== Workshop Git & GitHub === \n Date  : 10 juin 2025 \n Lieu  : Salle B204 \n Durée : 8 heures ")
n = 8
dureMinute = 60 * n
print("duree_minute = " ,  dureMinute ,"min")
if dureMinute > 60 * 7 :
    print("Le workshop dure plud d'une journée")


print()



try:
       liste = []
       participants = []
    
       f = open("participants.txt", "r")
       print("Participants =")
        
       for ligne in f:
            infos = ligne.strip().split(";")
            
            
            if len(infos) == 3:
                dico = {
                    "nom": infos[0],
                    "niveau": infos[1],
                    "email": infos[2]
                }
                liste.append(dico)
       for perso in liste:
        print(perso)



   
      

except FileNotFoundError:
    print("Erreur : le fichier participants.txt est introuvable.")






def afficher_participants(liste ):

   for i ,perso in enumerate(liste,1):
      print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
      print()

def  compter_par_niveau(liste):   

    debutant = 0
    intermediaire = 0
    avance = 0

    for  perso in  liste:
        niveau = perso['niveau'].lower()
        if niveau == "debutant":
         
         # print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
          #print()
          debutant += 1
        elif niveau == "intermediaire":
          intermediaire += 1
          
          
        else:
          #print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
          #print()
          avance += 1
    print("intermediaire : ", intermediaire)
    print("avance : ", avance)
    print("debutant : ", debutant )




   
   
  
  

for i, perso in enumerate(liste, 1):
    email = perso['email']
    
   
    if "@" not in email:
        print(f"⚠️ ALERTE : L'email de {perso['nom']} (n°{i}) est invalide : '{email}'")
    

def chercher_participant(liste, nom):
    
    nom = nom.lower()
    
    for participant in liste:
        if nom in participant["nom"].lower():
            return participant
            
   
    return None





def ajouter_participant(liste, nom, niveau, email):
    # 1. On vérifie si l'email existe déjà dans la liste
    for perso in liste:
        if perso["email"] == email:
            print(f"Erreur : L'email {email} est déjà utilisé.")
            return False
    
    # 2. Si on arrive ici, l'email est unique, on crée le dictionnaire
    nouveau = {
        "nom": nom,
        "niveau": niveau,
        "email": email
    }
    
    # 3. On l'ajoute à la liste
    liste.append(nouveau)
    return True





print(afficher_participants(liste))
print(compter_par_niveau(liste))
resultat = chercher_participant(liste, "Gra")
print(resultat)
succes = ajouter_participant(liste, "Alicia", "Expert", "alice@mail.com")
print(f"Ajout réussi ? {succes}")