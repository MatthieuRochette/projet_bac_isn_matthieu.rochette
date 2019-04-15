#----------------------------------- Importations -----------------------------------------------------

from tkinter import *
from tkinter.messagebox import *
from random import *

#----------------------------------- Code de la fenêtre -----------------------------------------------
#def quitBat():
 #   fenBat.destroy()

fenBat = Toplevel()
fenBat.title("La Bataille")
#quitterBat = Button(fenBat, text="Quitter", command = quitBat)
#quitterBat.grid(row = 0, column = 0)

#------------------------------------------------------------------------------------------------------
#------------------------------------ Code du jeu -----------------------------------------------------
#------------------------------------------------------------------------------------------------------

#---------------- Fonctions -----------------------------------------------

def tirer_nvlle_carte():
    global x, carteJ, carteIA, tas2
    infoBulle.configure(text="")
    
    # ------ Fonctions internes ------
    def bataille(premiereCarte1, premiereCarte2, premiereCarteAff1, premiereCarteAff2):
        global cartesMlg1, cartesMlg2,carteRetournee1, carteRetournee2,tasAff1,tasAff2,test       
            
        def test_fin_egalite():
            global cartesMlg1, cartesMlg2,carteRetournee1, carteRetournee2,tasAff1,tasAff2,test       
            carteJ.configure(image=carteRetourneeIm1)
            carteIA.configure(image=carteRetourneeIm2)

            if carteRetournee1 > carteRetournee2:
                infoBulle.configure(text= "Bataille gagnée!")
                cartesMlg1.extend(tasC1)
                tasAff1.extend(tasIm1)
                
                cartesMlg1.extend(tasC2)
                tasAff1.extend(tasIm2)

                test = True

            elif carteRetournee1 < carteRetournee2:
                infoBulle.configure(text="Bataille perdue!")
                cartesMlg2.extend(tasC1)
                tasAff2.extend(tasIm1)
                
                cartesMlg2.extend(tasC2)
                tasAff2.extend(tasIm2)

                test = True

            else:
                infoBulle.configure(text="Multi Bataille!")

            var.set(1)

        tasC1=[premiereCarte1]
        tasC2=[premiereCarte2]
        tasIm1=[premiereCarteAff1]
        tasIm2=[premiereCarteAff2]
        test=False
        
        while test == False :
            carteCachee1 = cartesMlg1[0]
            carteCachee2 = cartesMlg2[0]
            carteCacheeIm1 = tasAff1[0]
            carteCacheeIm2 = tasAff2[0]
            carteRetournee1 = cartesMlg1[1]
            carteRetournee2 = cartesMlg2[1]
            carteRetourneeIm1 = tasAff1[1]
            carteRetourneeIm2 = tasAff2[1]
            
            del(cartesMlg1[0:2])
            del(cartesMlg2[0:2])
            del(tasAff1[0:2])
            del(tasAff2[0:2])

            tasC1.append(carteCachee1)
            tasC1.append(carteRetournee1)
            tasC2.append(carteCachee2)
            tasC2.append(carteRetournee2)
            tasIm1.append(carteCacheeIm1)
            tasIm1.append(carteRetourneeIm1)
            tasIm2.append(carteCacheeIm2)
            tasIm2.append(carteRetourneeIm2)

            var = IntVar()
            tas2.configure(command = test_fin_egalite)

            tas2.wait_variable(var)
            
            var.set(0)
            
        tas2.configure(command=tirer_nvlle_carte)       
    # ------ Fonction principale -----
    x+=1
    compteTour.configure(text="Nombre de tours: "+str(x))

    if x == 360 or len(cartesMlg1) == 0 or len(cartesMlg2) == 0:
        data = open("data.txt", 'a')
        
        if len(cartesMlg1) > len(cartesMlg2):
            showinfo("Victoire", "Vous avez gagné!Max prend son poisson et rentre chez lui.")
            data.write("+1")
            
        elif len(cartesMlg1) < len(cartesMlg2):
            showinfo("Perdu", "Vous avez été battu! Max ne prend donc pas de poisson et rentre chez lui.")
            data.write("+0")
            
        else:
            showinfo("Egalité", "Vous avez fait une égalité. Le poissonnier décide, non sans pitié envers Max, de le laisser prendre le poisson. Max rentre chez lui.")

        data.close()
        fenBat.destroy()

    nvlleCarte1 = cartesMlg1[0]
    carteAfficher1 = tasAff1[0]
    cartesMlg1.remove(nvlleCarte1)
    tasAff1.remove(carteAfficher1)
    
    nvlleCarte2 = cartesMlg2[0]
    carteAfficher2 = tasAff2[0]
    cartesMlg2.remove(nvlleCarte2)
    tasAff2.remove(carteAfficher2)

    carteJ.configure(image = carteAfficher1)
    carteIA.configure(image = carteAfficher2)

    carteJ.grid(row = 4, column = 1)
    carteIA.grid(row = 1, column = 3)
    
    if nvlleCarte1 > nvlleCarte2:
        cartesMlg1.append(nvlleCarte1)
        cartesMlg1.append(nvlleCarte2)
        tasAff1.append(carteAfficher1)
        tasAff1.append(carteAfficher2)
        infoBulle.configure(text="Gagné!")

    elif nvlleCarte2 > nvlleCarte1:
        cartesMlg2.append(nvlleCarte1)
        cartesMlg2.append(nvlleCarte2)
        tasAff2.append(carteAfficher1)
        tasAff2.append(carteAfficher2)
        infoBulle.configure(text="Perdu!")
        
    else:
        infoBulle.configure(text="Bataille!")
                
        var2 = IntVar()
        tas2.configure(command = lambda: var2.set(1))
        tas2.wait_variable(var2)
        
        carteJ.configure(image = dosCarte)
        carteIA.configure(image = dosCarte)

        bataille(nvlleCarte1,nvlleCarte2,carteAfficher1,carteAfficher2)
        
    
#----------- Cartes -------------------------------------------------------

#-------- Images pour la fenetre graphique ------

dosCarte = PhotoImage(file="cartes/_dos carte.gif")

asCarreau = PhotoImage(file="cartes/_as carreau.gif")
asCoeur = PhotoImage(file="cartes/_as coeur.gif")
asTrefle = PhotoImage(file="cartes/_as trefle.gif")
asPique = PhotoImage(file="cartes/_as pique.gif")

deuxCarreau = PhotoImage(file="cartes/_deux carreau.gif")
deuxCoeur = PhotoImage(file="cartes/_deux coeur.gif")
deuxTrefle = PhotoImage(file="cartes/_deux trefle.gif")
deuxPique = PhotoImage(file="cartes/_deux pique.gif")

troisCarreau = PhotoImage(file="cartes/_trois carreau.gif")
troisCoeur = PhotoImage(file="cartes/_trois coeur.gif")
troisTrefle = PhotoImage(file="cartes/_trois trefle.gif")
troisPique = PhotoImage(file="cartes/_trois pique.gif")

quatreCarreau = PhotoImage(file="cartes/_quatre carreau.gif")
quatreCoeur = PhotoImage(file="cartes/_quatre coeur.gif")
quatreTrefle = PhotoImage(file="cartes/_quatre trefle.gif")
quatrePique = PhotoImage(file="cartes/_quatre pique.gif")

cinqCarreau = PhotoImage(file="cartes/_cinq carreau.gif")
cinqCoeur = PhotoImage(file="cartes/_cinq coeur.gif")
cinqTrefle = PhotoImage(file="cartes/_cinq trefle.gif")
cinqPique = PhotoImage(file="cartes/_cinq pique.gif")

sixCarreau = PhotoImage(file="cartes/_six carreau.gif")
sixCoeur = PhotoImage(file="cartes/_six coeur.gif")
sixTrefle = PhotoImage(file="cartes/_six trefle.gif")
sixPique = PhotoImage(file="cartes/_six pique.gif")

septCarreau = PhotoImage(file="cartes/_sept carreau.gif")
septCoeur = PhotoImage(file="cartes/_sept coeur.gif")
septTrefle = PhotoImage(file="cartes/_sept trefle.gif")
septPique = PhotoImage(file="cartes/_sept pique.gif")

huitCarreau = PhotoImage(file="cartes/_huit carreau.gif")
huitCoeur = PhotoImage(file="cartes/_huit coeur.gif")
huitTrefle = PhotoImage(file="cartes/_huit trefle.gif")
huitPique = PhotoImage(file="cartes/_huit pique.gif")

neufCarreau = PhotoImage(file="cartes/_neuf carreau.gif")
neufCoeur = PhotoImage(file="cartes/_neuf coeur.gif")
neufTrefle = PhotoImage(file="cartes/_neuf trefle.gif")
neufPique = PhotoImage(file="cartes/_neuf pique.gif")

dixCarreau = PhotoImage(file="cartes/_dix carreau.gif")
dixCoeur = PhotoImage(file="cartes/_dix coeur.gif")
dixTrefle = PhotoImage(file="cartes/_dix trefle.gif")
dixPique = PhotoImage(file="cartes/_dix pique.gif")

valetCarreau = PhotoImage(file="cartes/_valet carreau.gif")
valetCoeur = PhotoImage(file="cartes/_valet coeur.gif")
valetTrefle = PhotoImage(file="cartes/_valet trefle.gif")
valetPique = PhotoImage(file="cartes/_valet pique.gif")

dameCarreau = PhotoImage(file="cartes/_dame carreau.gif")
dameCoeur = PhotoImage(file="cartes/_dame coeur.gif")
dameTrefle = PhotoImage(file="cartes/_dame trefle.gif")
damePique = PhotoImage(file="cartes/_dame pique.gif")

roiCarreau = PhotoImage(file="cartes/_roi carreau.gif")
roiCoeur = PhotoImage(file="cartes/_roi coeur.gif")
roiTrefle = PhotoImage(file="cartes/_roi trefle.gif")
roiPique = PhotoImage(file="cartes/_roi pique.gif")


#------ Association images / valeurs -----------

listeAs = [asCarreau, asCoeur, asTrefle, asPique]
listeDeux = [deuxCarreau, deuxCoeur, deuxTrefle, deuxPique]
listeTrois = [troisCarreau, troisCoeur, troisTrefle, troisPique]
listeQuatre = [quatreCarreau, quatreCoeur, quatreTrefle, quatrePique]
listeCinq = [cinqCarreau, cinqCoeur, cinqTrefle, cinqPique]
listeSix = [sixCarreau, sixCoeur, sixTrefle, sixPique]
listeSept = [septCarreau, septCoeur, septTrefle, septPique]
listeHuit = [huitCarreau, huitCoeur, huitTrefle, huitPique]
listeNeuf = [neufCarreau, neufCoeur, neufTrefle, neufPique]
listeDix = [dixCarreau, dixCoeur, dixTrefle, dixPique]
listeValet = [valetCarreau, valetCoeur, valetTrefle, valetPique]
listeDame = [dameCarreau, dameCoeur, dameTrefle, damePique]
listeRoi = [roiCarreau, roiCoeur, roiTrefle, roiPique]

listeTout = [0, 0, listeDeux, listeTrois, listeQuatre, listeCinq, listeSix, listeSept, listeHuit, listeNeuf, listeDix, listeValet, listeDame, listeRoi, listeAs]

tasAff1 = []
tasAff2 = []

#-------- Valeurs et mélanges -------------------

cartesSsMlg = [14,14,14,14, 2,2,2,2, 3,3,3,3 ,4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 11,11,11,11, 12,12,12,12, 13,13,13,13]
#14 représente l'as(c'est sa valeur) donc placé avant le 2 par souci de logique

cartesMlg1 = []
cartesMlg2 = []

#Repartition des cartes au hasard en 2 tas
for i in range(26):
    carteHasard = choice(cartesSsMlg)
    carteAffHasard = choice(listeTout[carteHasard])
    cartesMlg1.append(carteHasard)
    tasAff1.append(carteAffHasard)
    listeTout[carteHasard].remove(carteAffHasard)
    cartesSsMlg.remove(carteHasard)

for j in range(26):
    carteHasard = choice(cartesSsMlg)
    carteAffHasard = choice(listeTout[carteHasard])
    cartesMlg2.append(carteHasard)
    tasAff2.append(carteAffHasard)
    cartesSsMlg.remove(carteHasard)
    listeTout[carteHasard].remove(carteAffHasard)

#---------------------Fenetre graphique-----------------------------------

tas1= Label(fenBat)
tas1.configure(image = dosCarte)
tas1.grid(row = 1, column = 1)

x=0
compteTour = Label(fenBat)
compteTour.configure(text="Nombre de tours:")
compteTour.grid(row =5, column = 0)

tas2= Button(fenBat, image = dosCarte, command = tirer_nvlle_carte)
tas2.configure(image = dosCarte)
tas2.grid(row = 4, column = 3)

carteJ = Label(fenBat)
carteIA = Label(fenBat)

infoBulle = Label(fenBat)
infoBulle2 = Label(fenBat)

infoBulle.configure(text="")
infoBulle2.configure(text="Cliquez sur votre tas pour continuer.")

infoBulle.grid(row = 2, column = 2)
infoBulle2.grid(row = 5, column = 2)

nomTas1 = Label(fenBat)
nomTas1.configure(text="Votre tas")
nomTas1.grid(row = 5, column = 3)

nomTas2 = Label(fenBat)
nomTas2.configure(text="Tas adverse")
nomTas2.grid(row = 0, column = 1)

nomC1 = Label(fenBat)
nomC1.configure(text="Votre carte")
nomC1.grid(row = 5, column = 1)

nomC2 = Label(fenBat)
nomC2.configure(text="Carte adverse")
nomC2.grid(row = 0, column = 3)
fenBat.mainloop()
