from random import*
from tkinter import*
from tkinter.messagebox import*
#from timeit import default_timer

#PREMIERE FENETRE D'ACCUEIL
"""
fenTir=Toplevel()
fenTir.title('Jeu de tir')
fenTir.geometry('275x50')
def jouer():
    showwarning ("Règle", "C'EST PARTI!")
    fenTir.destroy()

labelRegle=Label(fenTir, text='Attention le chronomètre démarre instantanément!')
labelRegle.grid(row=1)

boutonjouer=Button(fenTir, text='Jouer', command=jouer)
boutonjouer.grid()

fenTir.mainloop()
"""

#SECONDE FENETRE DE JEU
showwarning("Jeu de tir", "Attention, le jeu comprend un chronomètre et il commence immédiatement!")

fenJeu=Toplevel()
fenJeu.title('Jeu de tir')
fenJeu.geometry('800x460')

def cible():
    global xmin, xmax, ymin, ymax, oval
    x=randrange(25,375)
    y=randrange(25,375)

    xmin=x-25
    xmax=x+25
    ymin=y-25
    ymax=y+25

    oval=can1.create_image(x,y,image=cible_vache)

def pointeur(event):
    global xmin, xmax, ymin, ymax, oval, nbtir, vache_toucher
    if xmin <= event.x <= xmax and ymin <= event.y <= ymax:   
        can1.delete(oval)
        vache_toucher+=1
        if nbtir > 1 :
            cible()
    
    nbtir-=1
    if nbtir<=0:
        nbtir=0
    label1.configure(text="Nombre de tirs restant:" +str(nbtir))

    if nbtir==0:
        if vache_toucher == 10:
            
            data.write("+1")                        
            showinfo("Résultat", "Bravo, tu as gagné ton steak!")
            
        else:

            data.write("+0")
            showerror("Résultat", "Tu n'as pas touché toutes les vaches, tu as perdu! Pas de steak pour toi!")
            
        data.close()

        fenfermee = 1
        fenJeu.destroy()
    
def updateTime():
    global temps
    temps+=1
    """now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    str_time = "%02d:%02d" % (minutes, seconds)"""
    fenJeu.after(1000, updateTime)
    if temps < 10:
        label2.configure(text="Chronomètre:  00:0"+str(temps) )
    else:
        label2.configure(text="Chronomètre:  00:"+str(temps) )
    
    if temps==30 and fenfermee == 0:
        showwarning ("Résultat","Temps dépassé, tu as perdu! Pas de steak pour toi!")
        fenJeu.destroy()

#start = default_timer()

nbtir=10
vache_toucher=0
temps=0
fenfermee = 0

can1=Canvas(fenJeu,cursor='diamond_cross',bg='dark grey',height=400,width=400)
can1.bind("<Button-1>",pointeur)
can1.grid(row=0,column=2,padx='60')

label1=Label(fenJeu, text="Nombre de tirs restant:"+str(nbtir))
label1.grid(row=2,column=1)

label2=Label(fenJeu, text="Chronomètre:")
label2.grid(row=2,column=3)

cible_vache= PhotoImage(file="image tir/_cible vache.gif")

data = open("data.txt", 'a')

cible()
updateTime()

fenJeu.mainloop()