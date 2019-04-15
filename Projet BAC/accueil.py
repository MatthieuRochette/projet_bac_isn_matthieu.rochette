# ------ Importations ------ #

from tkinter import *
from tkinter.messagebox import *

# ---------------------------------------------------------------------- #

# -------- Fonctions ------- #

def lancer_jeu():

    my_jouer.grid_forget()
    my_title.grid_forget()
    labNoms.grid_forget()

    frame1.configure(width = 150)
    frame2.configure(height = 100)
    frame6.grid_forget()

    #labObjets.grid(row = 2, column = 1)

    my_quit.configure(height = 1, width = 5)
    my_quit.grid(row = 10, column = 10)

    suivant.grid(row = 5, column = 5)
    precedent.grid(row = 5, column = 0)
    precedent.configure(state = DISABLED)
    my_image_scenario.grid(row = 1, column = 1)

def quizz():
    global nbObjets, numQ, im4

    my_image_scenario.configure(image = im4)

    def reponse1():
        global nbObjets, numQ
        numQ += 1
        if numQ == 1:

            nbObjets +=1

            choix1.configure(bg = 'lime', state = DISABLED)
            choix2.configure(state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text='Indice: Ce fromage brille (BRIE) par sa réputation!')

        if numQ == 2:
            choix1.configure(bg = 'red', state = DISABLED)
            choix2.configure(bg = 'lime', state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text="Indice: *S*eul un *BRIN* de *Z*este le différencie (SBRINZ)")

        if numQ == 3:
            choix1.configure(bg = 'red', state = DISABLED)
            choix2.configure(state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(bg = 'lime', state = DISABLED)
            indice.configure(text = "*P*ar *U*ne *L*utte *E*ffarouchée, la réponse est à présent dévoilée. (PULE)")

        labObjets.configure(text = "Nombres de fromages récupérés: "+str(nbObjets)+"/3")
        questSuiv.grid(row = 10, column = 1)

    def reponse2():
        global nbObjets, numQ
        numQ += 1
        if numQ == 1:

            choix2.configure(bg = 'red', state = DISABLED)
            choix1.configure(state = DISABLED, bg = "lime")
            choix3.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text="Indice: Ce fromage brille (BRIE) par sa réputation!")

        if numQ == 2:

            nbObjets += 1

            choix1.configure(state = DISABLED)
            choix2.configure(bg = 'lime', state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text="Indice: *S*eul un *BRIN* de *Z*este le différencie (SBRINZ)")

        if numQ == 3:
            choix2.configure(bg = 'red', state = DISABLED)
            choix1.configure(state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(bg = 'lime', state = DISABLED)
            indice.configure(text = "*P*ar *U*ne *L*utte *E*ffarouchée, la réponse est à présent dévoilée. (PULE)")

        labObjets.configure(text = "Nombres de fromages récupérés: "+str(nbObjets)+"/3")
        questSuiv.grid(row = 10, column = 1)

    def reponse3():
        global nbObjets, numQ
        numQ += 1
        if numQ == 1:

            choix3.configure(bg = 'red', state=DISABLED)
            choix1.configure(state = DISABLED, bg = "lime")
            choix2.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text="Indice: Ce fromage brille (BRIE) par sa réputation!")

        if numQ == 2:
            choix3.configure(bg = 'red', state = DISABLED)
            choix2.configure(bg = 'lime', state = DISABLED)
            choix1.configure(state = DISABLED)
            choix4.configure(state = DISABLED)
            indice.configure(text="Indice: *S*eul un *BRIN* de *Z*este le différencie (SBRINZ)")

        if numQ == 3:
            choix3.configure(bg = 'red', state = DISABLED)
            choix2.configure(state = DISABLED)
            choix1.configure(state = DISABLED)
            choix4.configure(bg = 'lime', state = DISABLED)
            indice.configure(text = "*P*ar *U*ne *L*utte *E*ffarouchée, la réponse est à présent dévoilée. (PULE)")

        labObjets.configure(text = "Nombres de fromages récupérés: "+str(nbObjets)+"/3")
        questSuiv.grid(row = 10, column = 1)

    def reponse4():
        global nbObjets, numQ
        numQ += 1
        if numQ == 1:

            choix4.configure(bg = 'red', state=DISABLED)
            choix1.configure(state = DISABLED, bg = "lime")
            choix3.configure(state = DISABLED)
            choix2.configure(state = DISABLED)
            indice.configure(text="Indice: Ce fromage brille (BRIE) par sa réputation!")

        if numQ == 2:
            choix4.configure(bg = 'red', state = DISABLED)
            choix2.configure(bg = 'lime', state = DISABLED)
            choix3.configure(state = DISABLED)
            choix1.configure(state = DISABLED)
            indice.configure(text="Indice: *S*eul un *BRIN* de *Z*este le différencie (SBRINZ)")

        if numQ == 3:

            nbObjets += 1

            choix1.configure(state = DISABLED)
            choix2.configure(state = DISABLED)
            choix3.configure(state = DISABLED)
            choix4.configure(bg = 'lime', state = DISABLED)
            indice.configure(text = "*P*ar *U*ne *L*utte *E*ffarouchée, la réponse est à présent dévoilée. (PULE)")

        labObjets.configure(text = "Nombres de fromages récupérés: "+str(nbObjets)+"/3")
        questSuiv.grid(row = 10, column = 1)

    def next_question():
        global numQ, nbObjets

        choix1.configure(state = "normal", bg = "#f0f0f0")
        choix2.configure(state = "normal", bg = "#f0f0f0")
        choix3.configure(state = "normal", bg = "#f0f0f0")
        choix4.configure(state = "normal", bg = "#f0f0f0")

        if numQ == 1:  #on modifie les parametres pour afficher la question 2
            questSuiv.grid_forget()
            question.configure(text="Lequel de ces fromages n'est pas français?")
            choix1.configure(text = "Casgiu Sartinesu")
            choix2.configure(text = "Sbrinz")
            choix3.configure(text = "Kaïku")
            choix4.configure(text = "Kibidoo")
            indice.configure(text="Indice: Seul un brin de zeste le différencie.")

        if numQ == 2:  #on modifie les parametres pour afficher la question 2
            questSuiv.grid_forget()
            question.configure(text="Lequel de ces fromages coûte le plus cher?")
            choix1.configure(text = "Camembert de Normandie")
            choix2.configure(text = "Fourme d'Ambert")
            choix3.configure(text = "Epoisses")
            choix4.configure(text = "Pule")
            indice.configure(text="Indice: Par une lutte effarouchée, la réponse est à présent dévoilée.")

        if numQ == 3:
            questSuiv.grid_forget()

            if nbObjets == 3:
                showinfo("Information", "Max a trouvé tous les fromages. Fier de lui, il se dirige avec entrain vers le prochain rayon.")

            elif nbObjets == 1:
                showinfo("Information", "Max n'a trouvé qu'un fromage, il abandonne l'idée de trouver les deux autres et espère que sa mère\
ne le grondera pas trop quand il rentrera.")

            elif nbObjets == 2:
                showinfo("Information", "Max ne trouve que deux fromages, \
il abandonne l’idée de chercher le troisième et se rend au rayon suivant. Il espère que sa mère ne va pas trop le gronder.")

            else:
                showerror("GAME OVER", "Max n’a trouvé aucun fromages. Il termine les courses, \
mais sa mère le gronde pour son manque déplorable de culture générale \
au sujet du fromage et l’envoie travailler dans sa chambre, l’obligeant \
à apprendre par cœur la totalité des appellations de fromages du monde. \
Max ne supporte pas la quantité de travail énorme et meurt d’un AVC. GAME OVER")
                showinfo("Information", "Le jeu va maintenant se fermer automatiquement.")
                fen.destroy()

            if nbObjets >= 1:

                choix1.grid_forget()
                choix2.grid_forget()
                choix3.grid_forget()
                choix4.grid_forget()
                question.grid_forget()
                indice.grid_forget()

                frame1.configure(width = 150)
                frame2.configure(height = 100)

                labObjets.grid_forget()

                data = open("data.txt","w")
                data.write(str(nbObjets))
                data.close()

                my_quit.grid(row = 10, column = 10)

                suivant.grid(row = 5, column = 5)
                suivant.configure(command = lancer_tir)

                precedent.grid(row = 5, column = 0)
                precedent.configure(state = DISABLED)

                my_image_scenario.grid(row = 1, column = 1)

    my_image_scenario.grid_forget()
    suivant.grid_forget()
    precedent.grid_forget()

    question = Label(fen, text="Lequel de ces fromages est à pâte molle?", height  = 5,\
    width = 100, relief = RAISED)
    choix1 = Button(fen, text = "Brie", height = 3, width = 100,command = reponse1)
    choix2 = Button(fen, text = "Cantal", height = 3, width = 100, command = reponse2)
    choix3 = Button(fen, text = "Parmesan", height = 3, width = 100, command = reponse3)
    choix4 = Button(fen, text = "Sbrinz", height = 3, width = 100, command = reponse4)
    indice = Label(fen, text = "Indice: Ce fromage brille par sa réputation!")
    questSuiv = Button(fen, text="Suivant", command = next_question)

    frame5.configure(height = 10, width = 0)
    frame6.configure(height = 10)

    question.grid(row = 1, column = 1)
    frame3.grid(row = 2, column = 1)
    choix1.grid(row = 3, column = 1)
    frame4.grid(row = 4, column = 1)
    choix2.grid(row = 5, column = 1)
    frame5.grid(row = 6, column = 1)
    choix3.grid(row = 7, column = 1)
    frame6.grid(row = 8, column = 1)
    choix4.grid(row = 9, column = 1)
    labObjets.grid(row = 11, column = 1)
    indice.grid(row = 12, column = 1)

    showinfo("Règle du Quiz", "Vous allez jouer à un quiz. Les règles sont simples:\n\n-Cliquez sur une des réponses possibles pour la valider.\n\
-Pour chaque réponse juste, Max gagne 1 fromage.\n-Il n'y a pas de limite de temps.\n\nBonne chance!")
# ------------------------------------ Fin Quiz ------------------------------------------------------------- #

def lancer_bat():
    suivant.configure(command = fin_jeu)
    showinfo("Règles du jeu", "Le jeu de la bataille de carte va se lancer. En voici les règles:\n\n-Chaque joueur possède un tas de 26 cartes au départ.\n-Chaque\
 joueur retourne la carte sur le haut de son paquet. On confronte les deux cartes retournées et celle avec la plus grande valeur gagne.\n-Si les cartes ont la \
même valeur, on procède à une bataille: chaque joueur retourne 2 cartes supplémentaires, on confronte les deux dernières cartes, et le gagnant remporte la totalité \
des cartes retournées.\n-Le vainqueur est le joueur qui n'aura plus de cartes en premier, ou qui en aura le moins.\n\nBonne chance!")
    import bataille.py

def lancer_sfm():
    suivant.configure(command = my_next)
    showinfo("Règles du jeu",'Un jeu de Pierre/Feuille/Ciseaux "amélioré" va se lancer. Voici les règles:\n\n-Cliquez sur une figure de main pour jouer cette figure.\n\
-Le signe joué par Kévin, votre adversaire, est affiché à chaque tour.\n-Le premier joueur à atteindre le score de 5 gagne la partie.\n\nLes combinaisons:\n\
-La pierre gagne contre les ciseaux et le serpent, et perd contre la feuille et Spock.\n-La feuille gagne contre la pierre et Spock, et perd contre\
le serpent et les ciseaux.\n-Les ciseaux gagnent contre la feuille et contre le serpent, et perdent contre Spock et la pierre.\n-Le serpent gagne contre Spock et la\
 feuille et perd contre les ciseaux et la pierre.\n-Spock gagne contre les ciseaux et la pierre et perd contre le serpent et la feuille.\n\nBonne chance!')
    import Shifumi.py

def lancer_tir():
    global nbObjets
    suivant.configure(command = my_next)
    showinfo("Règles du jeu","Un jeu de tir va apparaître.Voici les règles:\n\n-Cliquez sur les têtes de vaches(attention, il ne faut en rater aucune!).\
\n-Le temps imparti est de 30 secondes. Un chronomètre vous permet de savoir à combien de temps vous en êtes.\n\nBonne chance!")
    import tir.py
        
def my_next():
    global imagesScenarioListe, imageNumX, numIm
    
    if numIm <=2:
        precedent.configure(state = "normal")

    numIm += 1
    
    if numIm >= imagesScenarioListe.index(imagesScenarioListe[-1]) and numIm !=2 and numIm != 5:
        suivant.configure(state = DISABLED)
    
    if numIm == 4:
        suivant.configure(command = lancer_sfm)
        showinfo('Histoire', "Alors que Max est sur le chemin de la poissonnerie, il tombe sur Kévin, son ami de longue date.")
    
    imageNumX = imagesScenarioListe[numIm]
    my_image_scenario.configure(image=imageNumX)

    if numIm == 2:
        numIm = 3
        suivant.configure(command = quizz)

    if numIm == 5:
        suivant.configure(command = lancer_bat)

def my_previous():
    global imagesScenarioListe, imageNumX, numIm
    suivant.configure(state = "normal", command = my_next)
    numIm -= 1
    
    if numIm <= 0:
        numIm = 0
        precedent.configure(state = DISABLED)
    imageNumX = imagesScenarioListe[numIm]
    my_image_scenario.configure(image=imageNumX)

def fin_jeu():
    global im_fin

    my_image_scenario.configure(image = im_fin)

    data = open("data.txt", "r")
    contenu  = data.read()
    contenu = str(contenu)
    i = 0
    score = 0
    while i < len(contenu):
            a = contenu[i]
            if a == "1" or a == "2" or a == "3" or a == "6": 
                score = score + int(a)
            i += 1
    objManquants = 5 - score
    if score <= 3:
        showinfo("Mère", "Max, tu te fiches de moi? Je t'ai demandé 5 ingrédients et il en manque "+str(objManquants)+" ! \
Allez ouste, dans ta chambre! Au fait, tu es privé de sortie jusqu'à la fin du mois!")

    if score == 4:
        showinfo("Mère", "Et bien, il manque un ingrédient... Tu préfères la corvée de vaisselle pendant 2 semaines \
ou être privé de téléphone pendant 1 mois?")
                
    if score == 5:
        showinfo("Mère", "Bien mon fils, maintenant je vais te demander de faire le ménage pendant que je fais mon\
 fameux ragoût bœuf-colin-fromage que tu adores. Nan je rigole, toi t’auras des haricots au beurre.")

    if score > 5:
        showinfo("Mère", "DEPUIS QUAND ES-TU AUTORISE A ACHETER DES BONBONS DE TA PROPRE INITIATIVE?! DANS TA CHAMBRE, IMMÉDIATEMENT !!! ET DONNE-MOI CA !\n\
Pendant que Max était sous huis-clos dans sa chambre, il entendait sa mère manger des bonbons dans le salon.")

    data.close()
    showinfo("C'est la fin...", "C'est la fin de ce jeu, il va maintenant se fermer de lui-même.\nMerci d'y avoir joué!")
    fen.destroy()

# ---------------------------------------------------------------------- #

# -------------------------------- Programme principal du jeu entier ----------------------------- #

#---------------- Initialisation ----------------- #
fen = Tk()
fen.title("Max va faire les courses")
fen.resizable(width = False, height = False)
fen.geometry("1100x1000")
#fen.attributes("-fullscreen", True)

# -------------------- Images -------------------- #

# ---- Images scénario ----
im1 = PhotoImage(file="Images scénario/_supermarche ext.gif")
im2 = PhotoImage(file="Images scénario/_liste courses.gif")
im3 = PhotoImage(file="Images scénario/_rayon fromagerie.gif")
im4 = PhotoImage(file="Images scénario/_rayon boucherie.gif")
im5 = PhotoImage(file="Images scénario/_rayon bonbons.gif")
im6 = PhotoImage(file="Images scénario/_rayon poissonerie.gif")

title = PhotoImage(file="Images scénario/_title.gif")
im_fin = PhotoImage(file="Images scénario/_maison.gif")

# ----------------- Variables -------------------- #
numIm = 0
imagesScenarioListe = [im1,im2,im3,im4,im5,im6] #etc
imageNumX = imagesScenarioListe[numIm]

nbObjets = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    # ---- Valeurs Quiz ---- #
numQ = 0
numRep = 0

# ----------------------------------- Widgets ------------------------------------- #

my_quit = Button(fen, text="Quitter", command = fen.destroy, height = 3, width = 50, cursor = "hand2")

my_jouer = Button(fen, text="Jouer", command = lancer_jeu, height = 3, width = 50, cursor = "hand2")

my_title = Label(fen, image = title)  #Pourquoi pas remplacer par une image stylée ?

suivant=Button(fen, text="Page suivante", command = my_next)

precedent = Button(fen, text="Page précédente", command = my_previous)
my_image_scenario = Label(fen, image =imageNumX)

labNoms = Label(fen, text="Projet de Léa Zisette,\nMatthieu Maugeais et \nMatthieu Rochette.")

labObjets = Label(fen, text="Nombres de fromages récupérés: "+str(nbObjets)+"/3")

# ---- frames pour créer des espaces ---- #

frame1 = Frame(fen, width = 200)
frame1.grid_propagate(0)

frame2 = Frame(fen, height = 300)
frame2.grid_propagate(0)

frame3 = Frame(fen, height = 35)
frame3.grid_propagate(0)

frame4 = Frame(fen, height = 10)
frame4.grid_propagate(0)

frame5 = Frame(fen, width = 10)
frame5.grid_propagate(0)

frame6 = Frame(fen, height = 280)
frame6.grid_propagate(0)

frame7 = Frame(fen, width = 15)
frame7.grid_propagate(0)

# ---- Positions ---- #

my_title.grid(row = 1, column = 1)
my_jouer.grid(row = 3, column = 1)
my_quit.grid(row = 5, column = 1)
labNoms.grid(row = 7, column = 0)

frame1.grid(row = 0, column = 0)
frame2.grid(row = 0, column = 1)
frame3.grid(row = 2, column = 1)
frame4.grid(row = 4, column = 1)
frame5.grid(row = 10, column = 9)
frame6.grid(row = 6, column = 0)

fen.mainloop()
