from typing import Union  # permet d'utiliser Union pour les types de variables
import pygame  # permet d'utiliser pygame
import sys   # Permet d'utiliser sys. sortie() pour quitter le jeu
from pygame.locals import *  # permet d'utiliser pygame.locals pour les touches du clavier
import random  # permet d'utiliser random.choice pour  choisir un mot aléatoirement
from pygame.surface import Surface, SurfaceType  # permet d'utiliser pygame.Surface pour créer une zone cliquable
from Fonction import *  # permet d'utiliser les fonctions du fichier Fonction.py

# initialise pygame et crée la fenêtre du jeu
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pendu')
pygame.font.init()
pygame.display.flip()

# initialise une fenetre appeler écran
windows: Union[Surface, SurfaceType] = pygame.display.set_mode((640, 480))
windows.fill(WHITE)

# permet de créer une zone cliquable nommée score_rec, elle y contiendra le texte de la variable score.
result_rec = pygame.Rect((310, 30), (120, 40))  # (x, y), (largeur, hauteur)
zone_rec = pygame.Surface(result_rec.size)  # permet de créer une zone cliquable
zone_rec.fill((255, 210, 147))  # permet de colorer la zone cliquable
windows.blit(zone_rec, (320, 20))  # permet de coller la zone cliquable sur la fenetre

police_principale = pygame.font.SysFont("roboto", 30)
result = police_principale.render("Resultat", 1, BLACK)     # permet de créer du texte contenu dans la variable result.
windows.blit(result, (330, 30))

# permet de créer une zone avec du texte qui contiendra le texte de la variable debut_partie.
debut_partie = police_principale.render("Hello ! veux tu jouer ou juste regarder les scores  ?", True, (0, 0, 150))
windows.blit(debut_partie, (105, 140))


""" permet de créer une zone cliquable nommée yes_rec, elle y contiendra le texte de la variable oui."""
yes_rec = pygame.Rect((150, 200), (190, 120))
button_image1 = pygame.image.load("ico2.png").convert_alpha()
button_rect1 = button_image1.get_rect()
button_rect1.topleft = (150, 200)
windows.blit(button_image1, button_rect1)

# permet de créer une zone cliquable nommée no_rec, elle y contiendra le texte de la variable no.
no_rec = pygame.Rect((450, 200), (135, 120))
button_image = pygame.image.load("ico.png").convert_alpha()
button_rect = button_image.get_rect()
button_rect.topleft = (450, 200)
windows.blit(button_image, button_rect)


nbr_erreur = 0  # permet de compter le nombre d'erreur
counter = 0  # permet de compter le nombre de clique sur le bouton score pour afficher le tableau des scores


add = ''  # permet de stocker les lettres entrées par l'utilisateur
nom = ''    # permet de stocker le nom de l'utilisateur

cre_mot = None  # permet de stocker le mot choisi par la fonction random.choice

base_font = pygame.font.Font(None, 32)

continuer = 1  # permet de faire tourner le jeu

while continuer:
    pygame.time.Clock().tick(20)  # permet de fixer le nombre de tick

    # cette boucle for permet de détecter et utiliser les interactions avec l'utilisateur
    for event in pygame.event.get():

        # ce if permet de traiter les clics de la sourri lorsqu'ils sont pressés par l'utilisateur.
        if event.type == pygame.MOUSEBUTTONDOWN:

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle score_rec et il est actif lorsque le compteur a pour valeur 0.
            if pygame.mouse.get_pressed()[0] \
                    and result_rec.collidepoint(pygame.mouse.get_pos()) \
                    and counter == 0:
                counter = 0.5
                pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))

                retour_debut = pygame.Rect((10, 5),
                                           (160, 30))  # (x, y), (largeur, hauteur) permet de créer une zone cliquable
                zone_rec = pygame.Surface(retour_debut.size)
                zone_rec.fill((255, 0, 0))
                windows.blit(zone_rec, (10, 5))

                result = police_principale.render("Acceuil ", 1, WHITE)
                windows.blit(result, (20, 10))

                # permet de créer du texte contenu dans les variables score_facile, scor_moyen et score_difficile.
                result_easy = police_principale.render("niveau facile", 1, "red")
                windows.blit(result_easy, (50, 100))

                result_moyen = police_principale.render("niveau moyen", 1, "red")
                windows.blit(result_moyen, (250, 100))

                result_hard = police_principale.render("niveau difficile", 1, "red")
                windows.blit(result_hard, (450, 100))

                # cette fonction permet d'afficher le tableau des scores
                affich_result(police_principale, windows)

            if pygame.mouse.get_pressed()[0] \
                    and counter == 0.5 \
                    and retour_debut.collidepoint(
                    pygame.mouse.get_pos()):   # permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit

                pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700,
                                                             700))  # efface l'écran de jeu pour le remplacer par le menu de début de jeu

                reinitialise = page_debut(windows, police_principale)
                add = reinitialise[0]  # permet de stocker les lettres entrées par l'utilisateur
                nom = reinitialise[1]  # permet de stocker le nom de l'utilisateur
                nbr_erreur = reinitialise[2]  # permet de compter le nombre d'erreur
                counter = reinitialise[3]   # permet de compter le nombre de clique sur le bouton score pour afficher le tableau des scores

            if pygame.mouse.get_pressed()[0] \
                    and no_rec.collidepoint(pygame.mouse.get_pos()) \
                    and counter == 0:  # permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
                continuer = False  # permet de sortir de la boucle while
                break  # permet de sortir de la boucle while

            if pygame.mouse.get_pressed()[0] \
                    and yes_rec.collidepoint(pygame.mouse.get_pos()) \
                    and counter == 0:  # permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
                counter = 1

                pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))  # efface l'écran de jeu pour le remplacer par le menu de début de jeu
                debut_partie = police_principale.render("Quelle niveau de difficulté souhaitez-vous ", True,
                                                        (0, 0, 150))
                windows.blit(debut_partie, (110, 50))
                easy_rec = pygame.Rect((50, 100), (125, 20))
                zone_rec = pygame.Surface(easy_rec.size)
                zone_rec.fill(WHITE)
                windows.blit(zone_rec, (50, 100))

                easy = police_principale.render("niveau facile", 1, "red")
                windows.blit(easy, (50, 100))

                moyen_rec = pygame.Rect((250, 100), (135, 20))
                zone_rec = pygame.Surface(moyen_rec.size)
                zone_rec.fill(WHITE)
                windows.blit(zone_rec, (250, 100))

                moyen = police_principale.render("niveau moyen", 1, "red")
                windows.blit(moyen, (250, 100))

                hard_rec = pygame.Rect((450, 100), (145, 20))
                zone_rec = pygame.Surface(hard_rec.size)
                zone_rec.fill(WHITE)
                windows.blit(zone_rec, (450, 100))

                hard = police_principale.render("niveau difficile", 1, "red")
                windows.blit(hard, (450, 100))

                zone_add = police_principale.render("Veuillez entrer votre nom ou pseudos ", 1, BLACK)  # permet de créer du texte contenu dans la variable zone_add
                windows.blit(zone_add, (135, 180))

                description = police_principale.render(
                    "pour pouvoir ajouter votre score à la liste des meilleurs scores", 1,
                    BLACK)
                windows.blit(description, (20, 210))

                description_suite = police_principale.render("si vous le souhaitez", 1, BLACK)
                windows.blit(description_suite, (135, 240))

                # permet de créer un bonton nommée valide_rec, ce dernier contiendra le texte de la variable valid.
                valid_rec = pygame.Rect((450, 330), (80, 30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220, 220, 220))
                windows.blit(valider_rec, (450, 330))

                valid = police_principale.render("Valider", 1, (0, 0, 0))
                windows.blit(valid, (455, 335))

                # permet de créer un bonton nommée retour_debut, ce dernier contiendra le texte de la variable retour.
            if pygame.mouse.get_pressed()[0] \
                    and counter == 1.5 and valid_rec.collidepoint(pygame.mouse.get_pos()):

                niveaux = ["facile", "moyen", "difficile"]  # permet de stocker les niveaux de difficulté
                prefixes = ["facile : ", "moyen : ", "hard : "]  # permet de stocker les préfixes correspondant aux niveaux de difficulté

                for i in range(len(niveaux)):  # permet de parcourir le tableau niveaux
                    if niveau == niveaux[i]:
                        nom = prefixes[i] + nom  # permet d'ajouter le préfixe correspondant au niveau choisi

                point = recherche_result(nom)
                nouveau_result(nom, point)   # permet d'ajouter le nom/pseudo et le score dans le fichier score.txt

                counter = 2

            if pygame.mouse.get_pressed()[0] \
                    and counter == 1 \
                    and easy_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "facile"
                counter = 1.5

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle moyen_rec et il est actif lorsque le compteur a pour valeur 1. Si c'est le cas niveau = "moyen".
            if pygame.mouse.get_pressed()[0] \
                    and counter == 1 \
                    and moyen_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "moyen"
                counter = 1.5

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle difficile_rec et il est actif lorsque le compteur a pour valeur 1. Si c'est le cas niveau = "difficile".
            if pygame.mouse.get_pressed()[0] \
                    and counter == 1 \
                    and hard_rec.collidepoint(pygame.mouse.get_pos()):
                niveau = "difficile"
                counter = 1.5

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle non_rec et il est actif lorsque le compteur a pour valeur 3.
            if pygame.mouse.get_pressed()[0] \
                    and no_rec.collidepoint(pygame.mouse.get_pos()) \
                    and counter == 2:
                counter = 4

                # ces variables permettent de choisir un mot de manière aléatoire grâce à la fonction choix_mot()
                # et d'initialiser la longueur de la zone de texte nécessaire au fonctionnement du pendu.
                mot = choix_mot()
                saisie_texte = zone_texte(mot)

                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 600, 300))

                # permet de créer et afficher le texte contenu dans la variable debut_partie, cete dernière permet d'afficher le niveau.
                debut_partie = police_principale.render(niveau, True, (0, 0, 150))
                windows.blit(debut_partie, (110, 80))

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle oui_rec et il est actif lorsque le compteur a pour valeur 3.
            if pygame.mouse.get_pressed()[0] \
                    and yes_rec.collidepoint(pygame.mouse.get_pos()) \
                    and counter == 2:
                counter = 3

                # permet de créer et afficher le texte contenu dans les variables zone_ajout et description.
                zone_add = police_principale.render("Veuillez entrer un mot dont vous voulez l'ajouter à la liste", 1,
                                                    BLACK)
                windows.blit(zone_add, (40, 250))
                valid_rec = pygame.Rect((450, 350), (80, 30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220, 220, 220))
                windows.blit(valider_rec, (450, 350))

                valid = police_principale.render("Valider", 1, BLACK)
                windows.blit(valid, (455, 355))

            if pygame.mouse.get_pressed()[0] \
                    and counter == 3 \
                    and valid_rec.collidepoint(pygame.mouse.get_pos()):

                cre_mot = add_mot(add)

                if cre_mot == "add réussi":
                    mot = choix_mot()
                    saisie_texte = zone_texte(mot)
                    counter = 4

                    pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))

                    debut_partie = police_principale.render(niveau, True, (0, 0, 150))
                    windows.blit(debut_partie, (110, 80))

        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 1.5,
        # avec la variable nom, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN \
                and counter == 1.5:
            nom += event.unicode

        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 4,
        # avec la variable ajout, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN \
                and counter == 3:
            add += event.unicode

            # ce if permet de détecter si une des touches shift est enfoncé, grâce à pygame.key.get_mods() & pygame.KMOD_SHIFT,
            # avec la variable nom, j'enregistre les touches grâce à event.unicode.
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                # la fonction ajout_mot() permet d'ajouter le mot saisie
                cre_mot = add_mot(add)

                # si cre_mot cre_mot == "Ajout réussi", alors je génère un nouveau mot de manière alétoire et j'initialise saisie_texte
                # selon la longueur du mot, cette dernière est nécessaire au fonctionnement du pendu.
                if cre_mot == "Ajout réussi":
                    mot = choix_mot()
                    saisie_texte = zone_texte(mot)
                    counter = 4

                    # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                    pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))

                    # permet de créer et afficher le texte contenu dans la variable debut_partie, cete dernière permet d'afficher le niveau.
                    debut_partie = police_principale.render(niveau, True, (0, 0, 150))
                    windows.blit(debut_partie, (110, 80))

        # ce if permet de détecter si une touche du clavier est enfoncé et il est actif lorsque le compteur a pour valeur 5,
        # avec la variable lettre, j'enregistre les touches grâce à event.unicode.
        if event.type == pygame.KEYDOWN \
                and counter == 4:
            lettre = event.unicode

            # si la lettre saisi n'est pas dans mot ou si il est déjà présent dans saisie_texte, j'ajoute 1 au compteur nbr_erreur.
            if lettre not in mot or lettre in saisie_texte:
                nbr_erreur += 1

            # si la lettre saisi est dans mot, alors je remplace les tiret par la lettre.
            # si la lettre est plusieurs fois présente dans mot, alors elle sera ajouté autant de fois qu'elle est présente dans mot.
            if lettre in mot:
                for x in range(len(mot)):
                    if lettre == mot[x]:
                        ma_list = list(saisie_texte)
                        ma_list[x + x] = lettre
                        saisie_texte = ''.join(ma_list)

            # si niveau == "facile", alors la variable jeu prendra comme valeur la variable pendu_facile, j'y envoie le nombre d'erreur.
            if niveau == "facile":
                jeu = pendu_easy(windows, nbr_erreur)

            # si niveau == "moyen", alors la variable jeu prendra comme valeur la variable pendu_moyen, j'y envoie le nombre d'erreur.
            elif niveau == "moyen":
                jeu = pendu_moyen(windows, nbr_erreur)

            # si niveau == "difficile", alors la variable jeu prendra comme valeur la variable pendu_difficile, j'y envoie le nombre d'erreur.
            elif niveau == "difficile":
                jeu = pendu_hard(windows, nbr_erreur)

            # si la variable jeu a pour valeur "perdu", je rénitialise l'affiche et j'affiche perdu grâce à la variable perdu
            if jeu == "perdu":
                pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))

                perdu = police_principale.render(f"partie PERDU le mot etait  : {mot}", 1, "red")
                windows.blit(perdu, (150, 80))

                reinitialise = page_debut(windows, police_principale)

                add = reinitialise[0]
                nom = reinitialise[1]
                nbr_erreur = reinitialise[2]
                counter = reinitialise[3]

                saisie_texte = zone_texte(mot)

        # si l'événement détecter est égal à QUIT, alors la boucle de jeu s'arrete.
        # L'événement QUIT correspond à la croix rouge en haut à droite de la fenetre.
        if event.type == QUIT:
            continuer = False

    # si compteur == 1,5, alors j'initialise ma zone de texte grâce à la variable zone_saisie,
    # celle-ci y integrera le texte de la variable nom à travers la variable texte.
    if counter == 1.5:
        zone_saisie = pygame.Rect(225, 270, 200, 50)
        pygame.draw.rect(windows, BLACK, zone_saisie, 2)
        texte = base_font.render(nom, True, BLACK)
        windows.blit(texte, (zone_saisie.x + 5, zone_saisie.y + 5))

    # si compteur == 2, alors
    if counter == 2:
        # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
        pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))

        #
        add_mot_liste = police_principale.render("Voulez-vous ajouter un mot  ?", True,
                                                 (0, 0, 150))
        windows.blit(add_mot_liste, (110, 80))  # permet d'afficher le texte à l'endroit voulu.

        yes = police_principale.render("oui", 1, (0, 200, 0))
        windows.blit(yes, (150, 200))

        no = police_principale.render("non", 1, (200, 0, 0))
        windows.blit(no, (450, 200))

    if counter == 3: # si compteur == 3, alors j'initialise ma zone de texte grâce à la variable zone_saisie,
        zone_saisie = pygame.Rect(225, 300, 200, 50)
        pygame.draw.rect(windows, BLACK, zone_saisie, 2)
        texte = base_font.render(add, True, BLACK)
        windows.blit(texte, (zone_saisie.x + 5, zone_saisie.y + 5))

        if cre_mot is not None: # si la variable cre_mot n'est pas vide alors je l'ajoute à la liste mot_liste

            if cre_mot == "Double":  # si le mot est déjà présent dans la liste
                add = ""
                cre_mot = None

                zone_saisie = pygame.Rect(225, 300, 200, 50)
                pygame.draw.rect(windows, WHITE, zone_saisie)

                erreur = police_principale.render("Mot déjà présent dans la liste", 1, (200, 0, 0))
                windows.blit(erreur, (10, 360))

                erreur_bis = police_principale.render("Veuillez taper un autre mot", 1, (200, 0, 0))
                windows.blit(erreur_bis, (10, 380))

    # si compteur == 4, alors j'initialise ma zone de texte grâce à la variable zone_saisie, 
    # celle-ci y integrera le texte de la variable ajout à travers la variable texte.
    if counter == 4:
        zone_saisie = pygame.Rect(200, 225, 140, 32)
        pygame.draw.rect(windows, WHITE, zone_saisie)
        texte = base_font.render(saisie_texte, True, BLACK)
        windows.blit(texte, (zone_saisie.x + 5, zone_saisie.y + 5))

        # j'initialise la variable gagne avec la fonction victoire
        gagne = victoire(saisie_texte, mot)

        # si gagne == "gagné", alors je rénitialise l'affiche et j'affiche gagné grâce à la variable perdu
        if gagne == "gagné":
            nouveau_result(nom, point + 1)
            pygame.draw.rect(windows, WHITE, pygame.Rect(0, 0, 700, 700))
            reinitialise = page_debut(windows, police_principale)
            add = reinitialise[0]
            nom = reinitialise[1]
            nbr_erreur = reinitialise[2]
            counter = reinitialise[3]

            succes = police_principale.render(f"partie gagné le mot etait {mot}", 1, (0, 200, 0))
            windows.blit(succes, (250, 30))

            saisie_texte = zone_texte(mot)

    # grâce à pygame.display.flip() j'actualise l'affichage de la fenêtre
    pygame.display.flip()

# avec pygame.quit() j'arrete le fonctionnement de pygame
pygame.quit()
# avec sys.exit() j'arrete le fonctionnement du programme
sys.exit()
