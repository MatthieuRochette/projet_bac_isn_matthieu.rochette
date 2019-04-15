# jeu pierre, papier, ciseaux, lézard, spock
# Kevin joue au hasard

from random import randint
from tkinter import *
from tkinter.messagebox import *

#variables générales
score_Kevin=0
score_Max=0
coup_Kevin=0
coup_Max=0

#shifumi
shifumi = Toplevel()   
shifumi.title("Pierre, Papier, Ciseaux, Lezard, Spock")

#images
pierre = PhotoImage(file ='Images signes/_pierre.gif')
papier = PhotoImage(file ='Images signes/_feuille.gif')
ciseaux = PhotoImage(file ='Images signes/_ciseaux.gif')
lezard = PhotoImage(file ='Images signes/_lezard.gif')
spock = PhotoImage(file ='Images signes/_spock.gif')

#jouer

def augmenter_scores(coup_Max,coup_Kevin):
    global score_Max, score_Kevin
    if coup_Max == 1 and coup_Kevin == 2:
        score_Kevin += 1
    elif coup_Max == 1 and coup_Kevin == 3:
        score_Max += 1
    elif coup_Max == 1 and coup_Kevin == 4:
        score_Max += 1
    elif coup_Max == 1 and coup_Kevin == 5:
        score_Kevin += 1
    elif coup_Max == 2 and coup_Kevin == 1:
        score_Max += 1
    elif coup_Max == 2 and coup_Kevin == 3:
        score_Kevin += 1
    elif coup_Max == 2 and coup_Kevin == 4:
        score_Kevin += 1
    elif coup_Max == 2 and coup_Kevin == 5:
        score_Max += 1
    elif coup_Max == 3 and coup_Kevin == 1:
        score_Kevin += 1
    elif coup_Max == 3 and coup_Kevin == 2:
        score_Max += 1
    elif coup_Max == 3 and coup_Kevin == 4:
        score_Max += 1
    elif coup_Max == 3 and coup_Kevin == 5:
        score_Kevin += 1
    elif coup_Max == 4 and coup_Kevin == 1:
        score_Kevin += 1
    elif coup_Max == 4 and coup_Kevin == 2:
        score_Max += 1
    elif coup_Max == 4 and coup_Kevin == 3:
        score_Kevin += 1
    elif coup_Max == 4 and coup_Kevin == 5:
        score_Max += 1
    elif coup_Max == 5 and coup_Kevin == 1:
        score_Max += 1
    elif coup_Max == 5 and coup_Kevin == 2:
        score_Kevin += 1
    elif coup_Max == 5 and coup_Kevin == 3:
        score_Max += 1
    elif coup_Max == 5 and coup_Kevin == 4:
        score_Kevin += 1
    else:
        score_Max +=0
        score_Kevin +=0

    if score_Max==5:
        lab4.configure(text="Vous avez gagné")
        bouton7.grid(row =5, column =2, pady =10, sticky=W)
        bouton1.configure(state=DISABLED)
        bouton2.configure(state=DISABLED)
        bouton3.configure(state=DISABLED)
        bouton4.configure(state=DISABLED)
        bouton5.configure(state=DISABLED)

        data = open("data.txt", "a")
        data.write("+6")
        data.close()

        showinfo("Histoire", "Vous avez battu Kevin. Ce dernier, plutôt mauvais joueur, a accusé Max de tricherie. Après un peu de dispute, il cède et donne à Max\
 le paquet de bonbon. Max se dirige ensuite vers la dernière étape, la poissonnerie.")

    if score_Kevin==5:
        lab4.configure(text="Vous avez perdu")
        bouton7.grid(row =5, column =2, pady =10, sticky=W)
        bouton1.configure(state=DISABLED)
        bouton2.configure(state=DISABLED)
        bouton3.configure(state=DISABLED)
        bouton4.configure(state=DISABLED)
        bouton5.configure(state=DISABLED)

        showinfo("Histoire", "Kévin a gagné. Il se pavane alors fièrement devant Max, et le nargue avec son sachet de bonbons. Après cette humiliation, Max décide de se \
rendre à la dernière étape, la poissonnerie.")

    if score_Kevin == 5 or score_Max == 5:
        shifumi.destroy()


def jouer(coup_Max):
    global score_Max, score_Kevin, score1, score2
    coup_Kevin = randint(1,5)
    
    if coup_Kevin==1:
        lab3.configure(image=pierre)
    elif coup_Kevin==2:
        lab3.configure(image=papier)
    elif coup_Kevin==3:
        lab3.configure(image=ciseaux)
    elif coup_Kevin==4:
        lab3.configure(image=lezard)
    elif coup_Kevin==5:
        lab3.configure(image=spock)
    augmenter_scores(coup_Max,coup_Kevin)
    score1.configure(text=str(score_Max))
    score2.configure(text=str(score_Kevin))
        
def jouer_pierre():
    jouer(1)

def jouer_papier():
    jouer(2)

def jouer_ciseaux():
    jouer(3)

def jouer_lezard():
    jouer(4)

def jouer_spock():
    jouer(5)

"""def reinit():
    global mon_score,ton_score,score1,score2,lab1,lab3
    score_Kevin = 0
    score_Max = 0
    score1.configure(text=str(score_Kevin))
    score2.configure(text=str(score_Max))"""

# boutons
bouton1 = Button(shifumi,command=jouer_pierre)
bouton1.configure(image=pierre)
bouton1.configure(text="Pierre")
bouton1.grid(row =4, column =1)

bouton2 = Button(shifumi,command=jouer_papier)
bouton2.configure(image=papier)
bouton2.configure(text="Papier")
bouton2.grid(row =4, column =2)

bouton3 = Button(shifumi,command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.configure(text="Ciseaux")
bouton3.grid(row =4, column =3)

bouton4 = Button(shifumi,command=jouer_lezard)
bouton4.configure(image=lezard)
bouton4.configure(text="Lézard")
bouton4.grid(row =4, column =4)

bouton5 = Button(shifumi,command=jouer_spock)
bouton5.configure(image=spock)
bouton5.configure(text="Spock")
bouton5.grid(row =4, column =5)

"""bouton6 = Button(shifumi,text='Recommencer',command=reinit)
bouton6.grid(row =5, column =0, pady =10, sticky=E)"""

bouton7 = Button(shifumi,text='Quitter',command=shifumi.destroy)

# Label
texte1 = Label(shifumi, text="Max :", font=("Helvetica", 16))
texte1.grid(row=0,column=0)

texte2 = Label(shifumi, text="Kévin :", font=("Helvetica", 16))
texte2.grid(row=1,column=0)

texte3 = Label(shifumi, text="Cliquez pour jouer")
texte3.grid(row=3, column=0, pady =5)

score1 = Label(shifumi, text=str(score_Kevin), font=("Helvetica", 16))
score1.grid(row=0, column=1)    

score2 = Label(shifumi, text=str(score_Max), font=("Helvetica", 16))
score2.grid(row=1, column=1)

lab3 = Label(shifumi)
lab3.grid(row =2, column =2)

lab4 = Label(shifumi)
lab4.grid(row =2, column =3)


# demarrage :
shifumi.mainloop()
