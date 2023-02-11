# Description: Ce module permet de créer des fonctions pour le jeu du pendu
# Auteur: Malik
# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import os
import random
import pygame



WHITE = (255, 255, 255)  # définit la couleur blanche
BLACK = (0, 0, 0)  # définit la couleur noire


def page_debut(windows, police_principale):
    """Cette fonction permet d'afficher la page de début du jeu"""
    result_rec = pygame.Rect((310, 30), (90, 40))  # définit la position et la taille de la zone de texte
    zone_rec = pygame.Surface(result_rec.size)  # définit la taille de la zone de texte
    zone_rec.fill(("red"))  # définit la couleur de la zone de texte
    windows.blit(zone_rec, (320, 10))

    result = police_principale.render("Resultat", 3, BLACK)  # définit la police du texte
    windows.blit(result, (320, 15))

    debut_partie = police_principale.render("Voulez-vous rejoué  ?", True, (0, 0, 150))
    windows.blit(debut_partie, (125, 150))

    yes = police_principale.render("OUI", 1, "blue")
    windows.blit(yes, (150, 200))

    no = police_principale.render("Quité", 1, "RED")
    windows.blit(no, (450, 200))
    add = ''  # définit la variable add
    nom = ''   # définit la variable nom
    nbr_erreur = 0 # définit la variable nbr_erreur
    counter = 0    # définit la variable counter
    return add, nom, nbr_erreur, counter



def pendu_easy(windows, erreurs):
    """Cette fonction permet d'afficher le pendu niveau facile"""
    if erreurs in range(1, 11):
        if erreurs == 1: # si le nombre d'erreur est égale à 1
            pygame.draw.line(windows, (0, 0, 0), (250, 200), (400, 200)) # dessine une ligne
        elif erreurs == 2: # si le nombre d'erreur est égale à 2
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (300, 200))  # dessine une ligne
        elif erreurs == 3:
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (400, 50))
            pygame.draw.line(windows, (0, 0, 0), (325, 50), (300, 75))
        elif erreurs == 4:
            pygame.draw.line(windows, (0, 0, 0), (375, 50), (375, 75))
        elif erreurs == 5:
            pygame.draw.circle(windows, (0, 0, 0), (375, 90), 15, 1)
        elif erreurs == 6:
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (375, 140))
        elif erreurs == 7:
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (360, 120))
        elif erreurs == 8:
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (390, 120))
        elif erreurs == 9:
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (360, 155))
        elif erreurs == 10:
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (390, 155))
            return "perdu" # retourne la valeur perdu



def pendu_moyen(windows, erreurs):
    """Cette fonction permet d'afficher le pendu niveau moyen"""
    if erreurs in range(1, 7):
        if erreurs == 1:
            pygame.draw.line(windows, (0, 0, 0), (250, 200), (400, 200))
        elif erreurs == 2:
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (300, 200))
        elif erreurs == 3:
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (400, 50))
            pygame.draw.line(windows, (0, 0, 0), (325, 50), (300, 75))
        elif erreurs == 4:
            pygame.draw.line(windows, (0, 0, 0), (375, 50), (375, 75))
            pygame.draw.circle(windows, (0, 0, 0), (375, 90), 15, 1)
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (375, 140))
        elif erreurs == 5:
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (360, 120))
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (390, 120))
        elif erreurs == 6:
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (360, 155))
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (390, 155))
            return "perdu"


def pendu_hard(windows, erreurs):
    """Cette fonction permet d'afficher le pendu niveau difficile"""
    # erreur permise 3
    if erreurs in range(1, 4):
        if erreurs == 1:
            pygame.draw.line(windows, (0, 0, 0), (250, 200), (400, 200))
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (300, 200))
            pygame.draw.line(windows, (0, 0, 0), (300, 50), (400, 50))
            pygame.draw.line(windows, (0, 0, 0), (325, 50), (300, 75))
        elif erreurs == 2:
            pygame.draw.line(windows, (0, 0, 0), (375, 50), (375, 75))
            pygame.draw.circle(windows, (0, 0, 0), (375, 90), 15, 1)
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (375, 140))
        elif erreurs == 3:
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (360, 120))
            pygame.draw.line(windows, (0, 0, 0), (375, 105), (390, 120))
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (360, 155))
            pygame.draw.line(windows, (0, 0, 0), (375, 140), (390, 155))
            return "perdu"



def zone_texte(mot):
    """Cette fonction permet de créer une zone de texte, en fonction du nombre de lettres du mot à trouver."""
    erreurs = 0  # je définis une variable erreurs à 0
    while erreurs < len(mot): # tant que erreurs est inférieur au nombre de lettres du mot
        erreurs += 1 # j'incrémente erreurs de 1
    texte = " _ " * erreurs # je multiplie le texte " _ " par le nombre de lettres du mot
    return texte # je retourne le texte



def victoire(saisie_texte, mot):
    """ Cette fonction permet de vérifier si le joueur a gagné ou non."""
    reponse = "" # je définis une variable reponse vide
    for x in saisie_texte: # je parcours la saisie du joueur
        if x != " ":  # si x est différent d'un espace
            reponse += x # je concatène x à reponse
    if reponse == mot: # si reponse est égale au mot
        return "gagné" # je retourne la valeur gagné







def lecture_fichier():  #
    """Cette fonction permet de lire le fichier mots.txt et de le mettre dans un tableau."""

    f = open("mots.txt", "r", encoding="UTF-8") # je lis le fichier mots.txt
    mots = ""  # je définis une variable mots vide
    lettre = f.read(1)  # je lis le fichier mots.txt lettre par lettre.
    while lettre:  # tant que lettre est différent de rien
        mots += lettre  # je concatène lettre à mots
        lettre = f.read(1)    # je lis le fichier mots.txt lettre par lettre.
    f.close()   # je ferme le fichier mots.txt
    tableau_mots = mots.split(" ")   # je sépare les mots du fichier mots.txt par un espace
    return tableau_mots   # je retourne le tableau de mots



def choix_mot():
    """Cette fonction permet de choisir un mot au hasard dans le fichier mots.txt."""
    tableau_mots = lecture_fichier()  # je lis le fichier mots.txt
    mot = random.choice(tableau_mots)   # je choisis un mot au hasard dans le tableau de mots
    return mot # je retourne le mot choisit au hasard



def add_mot(mot):
    """Cette fonction permet d'ajouter un mot dans le fichier mots.txt."""
    tableau_mots = lecture_fichier() # je lis le fichier mots.txt
    ma_list = "" # je définis une variable ma_list vide
    tableau_mots += [mot]  # je concatène le mot à ajouter au tableau de mots
    erreur = 0 # je définis une variable erreur à 0
    for x in tableau_mots: # je parcours le tableau de mots
        if x not in ma_list: # si x n'est pas dans ma_list
            ma_list += x + " " # je concatène x à ma_list
        elif x in ma_list: # si x est dans ma_list
            erreur += 1 # j'incrémente erreur de 1
    f = open("mots.txt", "w")
    f.write(ma_list)
    f.close()
    if erreur > 1:
        return "Doublon"
    elif erreur <= 1:
        return "ajout réussi"


def lecture_tableau_result():
    """Cette fonction permet de lire le fichier scores.txt et de le mettre dans un tableau."""
    tableau_result = {}
    try: # je tente de lire le fichier scores.txt
        with open("scores.txt", "r") as f: # je lis le fichier scores.txt
            for mot in f.readlines(): # je parcours le fichier scores.txt ligne par ligne
                ancien_nom, ancien_result = mot.split(":")  # je sépare le nom du joueur et son score par un ":"
                ancien_result = ancien_result.strip()
                ancien_result = int(ancien_result)
                tableau_result[ancien_nom] = ancien_result
            return tableau_result
    except:
        return tableau_result



def nouveau_result(nom, result):
    """Cette fonction permet d'ajouter un nouveau score dans le fichier scores.txt"""
    tableau_result = lecture_tableau_result() # je lis le fichier scores.txt

    tableau_result[nom] = result  # je concatène le nouveau nom et le nouveau score au tableau de scores
    try:
        with open("scores.txt", "w") as f: # je lis le fichier scores.txt
            for nom, result in tableau_result.items(): # je parcours le tableau de scores
                f.write(f"{nom}: {result}\n") # je concatène le nouveau nom et le nouveau score au fichier scores.txt
    except:
        print(
            f"Une erreur s'est produite lors de l'écriture du ancien_nom et du ancien_result dans le fichier scores.txt")



def affich_result(police, windows):
    """Cette fonction permet d'afficher les scores"""
    tableau_result = lecture_tableau_result()  # je lis le fichier scores.txt

    with open("scores.txt", "r") as f:  # je lis le fichier scores.txt
        i = 130 # je définis une variable i à 130
        for ancien_nom, ancien_result in tableau_result.items():  # je parcours le tableau de scores
            if ancien_nom[0:2] == "facile : ":  # si le nom du joueur commence par "facile : "
                ancien_result = (f"{ancien_nom[2::]}: {ancien_result}")  # je concatène le nom du joueur et son score
                result_hard = police.render(ancien_result, 1, BLACK) # je rend le texte en noir
                windows.blit(result_hard, (50, i))
                i += 30
        i = 130
        for ancien_nom, ancien_result in tableau_result.items():
            if ancien_nom[0:2] == "moyen : ":
                ancien_result = (f"{ancien_nom[2::]}: {ancien_result}")
                result_hard = police.render(ancien_result, 1, BLACK)
                windows.blit(result_hard, (250, i))
                i += 30
        i = 130
        for ancien_nom, ancien_result in tableau_result.items():
            if ancien_nom[0:2] == "hard : ":
                ancien_result = (f"{ancien_nom[2::]}: {ancien_result}")
                result_hard = police.render(ancien_result, 1, BLACK)
                windows.blit(result_hard, (450, i))
                i += 30



def recherche_result(nom):
    """Cette fonction permet de chercher s'il y a un score associé au nom entré dans le pendu"""
    tableau_result = lecture_tableau_result()

    with open("scores.txt", "r") as f: # je lis le fichier scores.txt
        for ancien_nom, ancien_result in tableau_result.items(): # je parcours le tableau de scores
            if nom == ancien_nom: # si le nom entré dans le pendu est égal au nom du joueur
                return ancien_result # je retourne le score du joueur
        return 0