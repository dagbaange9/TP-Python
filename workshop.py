print("=== Workshop Git & GitHub === \n Date  : 10 juin 2025 \n Lieu  : Salle B204 \n Durée : 8 heures ")
n = 8
dureMinute = 60 * n
print("duree_minute = " ,  dureMinute ,"min")
if dureMinute > 60 * 7 :
    print("Le workshop dure plud d'une journée")


print()



try:
       liste = []
    
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




debutant = 0
intermediaire = 0
avance = 0
for i , perso in  enumerate(liste,1):
         
         
        

        if perso['niveau'] == "debutant":
         
          print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
          print()

          debutant += 1
        elif perso['niveau'] == "intermediaire":
          
          print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
          print()

          intermediaire += 1

        else:
          

          print( {i}, f"| {perso['nom']}" ,f"| {perso['niveau']}" , f"| {perso['email']}")
          print()

          avance += 1
print("debutant : ", debutant )
print("intermediaire : ", intermediaire)
print("avance : ", avance)
  