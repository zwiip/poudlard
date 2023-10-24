"""
Choixpeau Magique
Voici un programme qui permet de simuler la cérémonie de répartitions des élèves de Poudlard, me servant d'entrainement python.

TODO
  - Personnalisation de l'élève :
      - demander prénom
      - Questions du choixpeaux et entrées user pour définir qualités

"""
"""
importations

"""
import random

"""
constantes
"""
students_number = 5
behaviors = ["enthousiasme", "fougue", "indifférence", "crainte"]
qualities = ["courage", "loyauté", "intelligence", "ruse"]

houses = {
   "Gryffondor": 0,
   "Poufsouffle": 0,
   "Serdaigle": 0,
   "Serpentard": 0
}

"""
functions
"""

def start_ceremony():
    print(f"Je n'suis pas d'une beauté suprême \n Mais faut pas s'fier à ce qu'on voit \n Je veux bien me manger moi-même \n Si vous trouvez plus malin qu'moi.")
    sort_a_student()
    print(f"Il y a maintenant {houses['Gryffondor']} Gryffondors, {houses['Poufsouffle']} Poufsouffles, {houses['Serdaigle']} Serdaigles et {houses['Serpentard']} Serpentards")

def sort_a_student():
   for student in range(students_number):
      print(f"un nouveau étudiant approche avec {random.choice(behaviors)}")
      quality = get_quality()
      get_house(quality)

def get_quality():
   quality = random.choice(qualities)
   print(f"Je vois... hmmm... ooh.. hmmm... {quality}")
   return quality

def get_house(quality):
   house = ""
   if quality == qualities[0]:
      house = "Gryffondor"
   elif quality == qualities[1]:
      house = "Poufsouffle"
   elif quality == qualities[2]:
      house = "Serdaigle"
   else:
      house = "Serpentard"
   houses[house] += 1
   print(f"ce sera donc {house} !")


start_ceremony()