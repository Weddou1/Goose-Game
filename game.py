import pygame, sys
import time
import random as ra
import os


#Changer  le dossier actuel du Python Shell vers le Dossier actuel
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#changer l'icone de jeu
programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)







# PHASE INITIALISATION 
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X=956
Y=417
pygame.init()
win=pygame.display.set_mode((1280,720))
pygame.display.set_caption("LET'S ROLL - Projet par ADAM KACEM, MOHAMED BELDI ET NADA BOUSSETTA")
bg = pygame.image.load('final.png')
mbg=pygame.image.load('menu.png')
clock = pygame.time.Clock()




#coordonnees de chaque case:

'''
Nous avons utilise un programme annexe afin d'ecrire les coordonnes du jeu (Boucle classique de spirale)

'''

cases=[(26, 644), (129, 644), (232, 644), (335, 644), (438, 644), 
(541, 644), (644, 644), (747, 644), (850, 644), (850, 541), (850, 438), 
(850, 335), (850, 232), (850, 129), (850, 26), (747, 26), (644, 26), (541, 26), 
(438, 26), (335, 26), (232, 26), (129, 26), (26, 26), (26, 129), (26, 232), (26, 335), 
(26, 438), (26, 541), (129, 541), (232, 541), (335, 541), (438, 541), (541, 541), 
(644, 541), (747, 541), (747, 438), (747, 335), (747, 232), (747, 129), (644, 129), 
(541, 129), (438, 129), (335, 129), (232, 129), (129, 129), (129, 232), (129, 335), 
(129, 438), (232, 438), (335, 438), (438, 438), (541, 438), (644, 438), (644, 335), 
(644, 232), (541, 232), (438, 232), (335, 232), (232, 232), (232, 335), (335, 335), 
(438, 335), (541, 335)]
#-----------------------------------






#CLASSES : ---------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name=""
        self.pos= 0
        self.image = pygame.image.load('spy.png')
        self.rect = self.image.get_rect()
        self.isblocked=False


class Case():
    def __init__(self):
        self.contain=None
        self.pos=(26, 644)
        self.effect=0
    
    
    

#------------------------


#Initialisation des cases:-------
List_Case=[]
for i in range(63):
    r=Case()
    r.pos=cases[i]
    List_Case.append(r)



#Declaration des joueurs:------
Theif=Player()
Duck=Player()
Lady=Player()
Guy=Player()






#Chargement des icones et images du jeu
Duck.image=pygame.image.load('Goose.png')
Lady.image=pygame.image.load('Lady.png')
Guy.image=pygame.image.load('Guy.png')
Duck.name="Goose"
Guy.name="Guy"
Lady.name="Lady"
Theif.name="Spy"
yourturntext=pygame.image.load('turn.png')




# Chargement des images des dés
dicepic=pygame.image.load('1.png')
dicepic=pygame.transform.scale(dicepic,(200,200))




#--------------
                
blocked=[] # Liste des joueurs bloqués 
                

#MOUVEMENT

#Mouvement des pions sur la case n1
def case1(p1):
    if p1==Theif:
        Theif.rect.x=1
        Theif.rect.y=619
    elif p1==Duck:
        Duck.rect.x=51
        Duck.rect.y=619
    elif p1==Lady:
        Lady.rect.x=1
        Lady.rect.y=669
    else:
        Guy.rect.x=51
        Guy.rect.y=669
    p1.pos=1



def aller1(P1,i):
    if i==1: case1(P1)
    else:       
        P1.rect.x=cases[i-1][0]
        P1.rect.y=cases[i-1][1]
        P1.pos=i
        if List_Case[i-1].effect==-1:blocked.append(P1)





#Permutation de la position de deux pions
def swap(P1,P2):
    aux=P1.pos
    aller1(P1,P2.pos)
    aller1(P2,aux)
    List_Case[P1.pos-1].contain=P1
    List_Case[P2.pos-1].contain=P2
    if List_Case[P1.pos-1].effect==-1 and P2 in blocked:blocked.remove(P2)
    elif List_Case[P2.pos-1].effect==-1 and P1 in blocked:blocked.remove(P1)






#Deplacement normal d'un pion vers une case
def aller(P1,i):
    

    List_Case[P1.pos-1].contain=None
    
    P1.rect.x=cases[i-1][0]
    P1.rect.y=cases[i-1][1]
    P1.pos=i
    if List_Case[i-1].effect==-1:blocked.append(P1)

    List_Case[i-1].contain=P1
    

#EFFETS
'''
Nous avons attribué un ID a chaque effet (Bloquage -1, Deplacement > 0 et Aucun Effet 0) 
pour lidentifier et lactiver
'''

#effects=     -1:block       0:no effect      0> teleportation

#effect du bloque
def blockcase(n):
    List_Case[n-1].effect=-1



#effect du teleportation
def transcase(n,new):
    List_Case[n-1].effect=new


#application des effects sur les cases

transcase(6,12)
transcase(30,42)
transcase(58,4)

blockcase(19)
blockcase(47)



#DESSIN ET APPLICATION DES IMAGES SUR LA FENETRE

def draw_dice(dicenum):
    
    dicepic=pygame.image.load(['1.png','2.png','3.png','4.png','5.png','6.png'][dicenum-1])
    dicepic=pygame.transform.scale(dicepic,(200,200))
    win.blit(dicepic,(1000,480))





def draw(character,n,players):
    #DEROULEMENT NORMALE DU JEU AVEC UN SYSTEME DE TOUR
    yourturnimage=pygame.transform.scale(character.image,(40,40))
    win.fill((0,0,0))
    win.blit(bg,(0,0))
    
    win.blit(Theif.image,(Theif.rect.x,Theif.rect.y))
    win.blit(Duck.image,(Duck.rect.x,Duck.rect.y))
    if players>=3:
        win.blit(Lady.image,(Lady.rect.x,Lady.rect.y))
        
        if players ==4:
            win.blit(Guy.image,(Guy.rect.x,Guy.rect.y))    
    win.blit(yourturnimage,(1000,430))
    win.blit(yourturntext,(1050,450))
    
        
    draw_dice(n)



    pygame.display.update()












#BOUCLE PRINCIPALE



def main():


    #DEPLACEMENT DES PIONS VERS LA CASE INITIALE
    case1(Duck)
    case1(Theif)
    case1(Lady)
    case1(Guy)
    characters=[Theif,Duck,Lady,Guy]

    
    run = True
    runm=True 
 
    
        
    players=4    
    #apparition dU menu PRINCIPALE:
    while runm:   
        win.fill((0,0,0))    
        win.blit(mbg,(0,0))    
        pygame.display.update()


        #Choix du nombre de joueurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    
                if event.key==pygame.K_KP_2:
                    players=2
                    runm=False
                elif event.key==pygame.K_KP_3:
                    players=3
                    runm=False
                elif event.key==pygame.K_KP_4:
                    players=4
                    runm=False
    
    character=Theif
    


    #Systeme de tour des pions (On enleve les pions suivant le nombre de joueurs choisis)
    characters=characters[:players]

    #Systeme de tour
    def suivant(character):
        if characters.index(character)<len(characters)-1:return characters[characters.index(character)+1]
        return Theif
    
    
    

    
    dicenum=1
    
    while run:
        
        
        draw(character,dicenum,players)
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                #pour tester---------------------------------------------------------------------------
                if event.key == pygame.K_UP:
                    
                    
                    p=57
                    if p>63:p=2*63-character.pos-dicenum
                    elif List_Case[p-1].effect>0:p=List_Case[p-1].effect
                    

                    if List_Case[p-1].contain==None:
                        aller(character,p) 
                    else :
                        swap(character,List_Case[p-1].contain)
                   

                    character=suivant(character) #Passer au joueur suivant
                    

                    while (character in blocked): #Verifie si un joueur est bloque ou non (Et passer le tour pour ce dit joueur)
                        
                        blocked.remove(character)       
                        character=suivant(character)   
                    
                    
 #----------------------------------------------------------------------------------------------
                #Si l'utilisateur appuie sur espace:
                if event.key == pygame.K_SPACE: 
                    dicenum=ra.randint(1,6)
                    p=character.pos+dicenum
                    x=p
                    
                    #Retour en arriere si il depasse 63
                    if p>63:p=2*63-character.pos-dicenum
                    
                    #transportation suivant l'effet du case
                    if List_Case[p-1].effect>0:
                        p=List_Case[p-1].effect
                        draw(character,dicenum,players)
                        #PETITE ANIMATION lorsque le pion fait une teleportation
                        for i in range(x,p):
                                
                            win.blit(pygame.image.load('mm.png'),(cases[i-1]))
                            pygame.display.flip()
                            clock.tick(20)
                        pygame.display.update()  
                    else: #Animation lors dun deplacement normal
                        y=character.pos
                        if y==1:y+=1
                        for i in range(y,p):
                                
                            win.blit(character.image,(cases[i-1]))
                            pygame.display.flip()
                            clock.tick(20)
                            win.blit(bg,(0,0))
                            for e in characters:
                                clock.tick(35)
                                if e!=character:win.blit(e.image,(e.rect.x,e.rect.y))
                            win.blit(pygame.transform.scale(character.image,(40,40)),(1000,430))
                            win.blit(yourturntext,(1050,450))
                            draw_dice(dicenum)
                        pygame.display.update() 
                       
                       
                        
                    #Verifier si on va permuter entre 2 joueurs
                    if List_Case[p-1].contain==None:
                        aller(character,p) 
                    else :
                        swap(character,List_Case[p-1].contain)

                    #verifier si un joueur a gagne et ecran de chargement:
                    if p==63:
                        
                        while True:
                            
                            
                            win.blit(pygame.image.load(['twon.png','dwon.png','lwon.png','gwon.png'][characters.index(character)]),(0,0))
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                     
                                    pygame.quit() 
                                    sys.exit()
                   

                    character=suivant(character) #Passer au joueur suivant
                    
                    
                    #Verifie si un joueur est bloque ou non (Et passer le tour pour ce dit joueur)   
                    while (character in blocked): 
                        blocked.remove(character)       
                        character=suivant(character)    
                    
                    

            
           


    pygame.quit()



if __name__ == "__main__":
    main()