import pygame
import random
import time
# hangman = ["hangman1.png", "hangman2.png", "hangman3.png", "hangman4.png", "hangman5.png", "hangman6.png", "hangman7.png"]


def imageloop(add):
    screen.blit(add, (50, 50))


def listtostring(s):
    list_to_string = " ".join(s)
    return list_to_string


def blank_display(text):
    myfont = pygame.font.SysFont("arial", 60)
    font_ob = myfont.render(text, True, black)
    screen.blit(font_ob, (460, 150))


def letter_display(text, position): # position is a tuple
    myfont = pygame.font.SysFont("dokchampa", 24)   # font size 24
    font_ob = myfont.render(text, True, aqua)   # font color aqua
    screen.blit(font_ob, position)  # position is a tuple

def tries(count):
    myfont = pygame.font.SysFont("dokchampa", 18)
    font_ob1 = myfont.render("Tries left:", True, small_violet)
    font_ob2 = myfont.render(str(count), True, small_violet)
    screen.blit(font_ob1, (0, 0))
    screen.blit(font_ob2, (75, 0))

def button(text, x, y, w, h, inactive, active): # x, y, width ,height
    keys = pygame.key.get_pressed() # get the keys pressed
    for event in pygame.event.get():    # get the events
        if event.type == pygame.KEYDOWN:    # if a key is pressed
            answer = pygame.key.name(event.key) # get the name of the key pressed
            numb_of_letters = movie.count(answer)   # count the number of times the key pressed is in the movie
            if numb_of_letters == 0:    # if the key pressed is not in the movie
                pygame.draw.rect(screen, red, (x, y, w, h))
                hangman.pop(0)
                length_of_hangman = len(hangman)
                global pictureno
                pictureno = length_of_hangman

            else:   # if the key pressed is in the movie
                pygame.draw.rect(screen, green, (x, y, w, h))
                ob = [i for i, a in enumerate(movie) if a == answer]
                for tt in ob:
                    list[tt] = answer
                    blank_display(listtostring(list))
        else:
            pygame.draw.rect(screen, inactive, (x, y, w, h))
    letter_display(text, (x + 7, y + 7))

def intro_button (text, x, y, w, h, inactive, active, action = None):   # x, y, width ,height
    keys = pygame.key.get_pressed() # get the keys pressed
    for event in pygame.event.get():    # get the events
        if event.type == pygame.KEYDOWN:    # if a key is pressed
            if event.key == pygame.K_RETURN:
                if action == "PLAY":
                    game_loop()
                elif action == "QUIT":
                    pygame.quit()
                    quit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, active, (x, y, w, h))  # x, y, width ,height
        if click[0] == 1 and action != None:
            if action == "PLAY":
                game_loop()
            elif action == "QUIT":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen, inactive, (x, y, w, h))
    letter_display(text, (x + 8, y + 8))

def button_loop():
    """This function is used to create the buttons for the game"""

    buttons = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    start_x, start_y = 450, 450
    step_x, step_y = 55, 55
    for i, button_label in enumerate(buttons):
        x = start_x + (i % 9) * step_x
        y = start_y + (i // 9) * step_y
        button(button_label, x, y, 40, 40, yellow, bright_yellow)


def game_intro():   # x, y, width ,height
    intro = True
    while intro:    # while the intro is true
        for event in pygame.event.get():    # get the events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(welcome_blue)   # fill the screen with the color
        largetext = pygame.font.SysFont("arial", 115)
        font_ob = largetext.render("     Le Pendu", True, black)
        minitext = pygame.font.SysFont("arial", 20)
        font_ob2 = minitext.render("Crée par Malik", True, black)
        screen.blit(font_ob, (250, 150))
        screen.blit(font_ob2, (0, 650))
        intro_button("Joué", 400, 560, 80, 40, "azure", bright_green, "PLAY")
        intro_button("Quité", 800, 560, 80, 40, "red", bright_red, "QUIT")
        pygame.display.flip()
        clock.tick(100)

def replay (text, x, y, w, h, inactive, active, action = None):  # x, y, width ,height
    replay = True
    while replay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largetext = pygame.font.SysFont("arial", 160)
        largetext2 = pygame.font.SysFont("comicsnasms", 75)
        font_ob1 = largetext.render("Gagner !", True, bright_green)
        font_ob2 = largetext2.render("Le Mot est :", True, orange)
        font_ob3 = largetext2.render(movie, True, orange)
        screen.blit(font_ob1, (390, 150))
        screen.blit(font_ob2, (390, 350))
        screen.blit(font_ob3, (390, 450))
        replay_button("Rejoué", 400, 560, 80, 40, "azure", bright_green, "PLAY")
        replay_button("Quité", 800, 560, 80, 40, "red", bright_red, "QUIT")
        pygame.display.flip()
        clock.tick(100)


def game_loop():
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        button_loop()
        tries(pictureno)
        imageloop(imagelist[pictureno])
        blank_display(listtostring(list))

        if hangman == 0:
            screen.fill(white)
            largetext = pygame.font.SysFont("arial", 160)
            largetext2 = pygame.font.SysFont("comicsnasms", 75)
            font_ob1 = largetext.render("Gagner !", True, bright_green)
            font_ob2 = largetext2.render("Le Mot est :", True, orange)
            font_ob3 = largetext2.render(movie, True, orange)
            screen.blit(font_ob1, (390, 150))
            screen.blit(font_ob2, (60, 430))
            screen.blit(font_ob3, (460, 430))
        elif hangman == 6:
            screen.fill(white)
            largetext = pygame.font.SysFont("arial", 160)
            largetext2 = pygame.font.SysFont("comicsnasms", 75)
            font_ob1 = largetext.render("Perdu !", True, bright_green)
            font_ob2 = largetext2.render("Le Mot est :", True, orange)
            font_ob3 = largetext2.render(movie, True, orange)
            screen.blit(font_ob1, (390, 150))
            screen.blit(font_ob2, (60, 430))
            screen.blit(font_ob3, (460, 430))


        if movie == ("".join(list)):
            screen.fill(white)
            largetext = pygame.font.SysFont("arial", 160)
            largetext2 = pygame.font.SysFont("comicsnasms", 75)
            font_ob1 = largetext.render("Bien jouer !", True, bright_green)
            font_ob2 = largetext2.render("Le Mot est :", True, orange)
            font_ob3 = largetext2.render(movie, True, orange)
            screen.blit(font_ob1, (390, 150))
            screen.blit(font_ob2, (60, 430))
            screen.blit(font_ob3, (460, 430))


        pygame.display.flip()
        clock.tick(100)

pygame.init()
display_width = 1280
display_height = 720

Answer = ""
bright_green = (0, 255, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
red = (200, 0, 0)
yellow = (255, 234, 0)
bright_yellow = (255, 251, 125)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (92, 201, 255)
orange = (255, 159, 0)
aqua = (30, 0, 181)
violet = (193, 122, 255)
small_violet = (159, 52, 235)
welcome_blue = (255, 195, 74)

Hangman2 = pygame.image.load("stage2.png")
Hangman3 = pygame.image.load("stage3.png")
Hangman4 = pygame.image.load("stage4.png")
Hangman5 = pygame.image.load("stage5.png")
Hangman6 = pygame.image.load("stage6.png")
Hangman7 = pygame.image.load("stage7.png")
Hangman8 = pygame.image.load("stage8.png")

imagelist = [Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7, Hangman8]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pendu')
running = False
hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
pictureno = 6

store = []

with open("mots.txt", "r") as f:
    for line in f:
        store.append(line.strip())  # strip() removes the newline character
movie = random.choice(store)
list = []
length_of_movie = len(movie)
for j in range(length_of_movie):
    list.append('_')
print(list)
def add_word(): # add word to the list
    with open("mots.txt", "a") as f:   # open the file in append mode
        f.write("\n" + Answer)  # add the word to the file

def score():
    score = 0
    return score


def listtostring(list): # convert list to string
    string = ""     # empty string
    for i in list:      # iterate over the list
        string += i
    return string
def imageloop(image):
    screen.blit(image, (0, 0))
def tries(pictureno):   # display the number of tries
    largetext = pygame.font.SysFont("arial", 40)
    font_ob = largetext.render("Tries: " + str(pictureno), True, black) # convert the number of tries to string
    screen.blit(font_ob, (0, 0))


screen.fill(white)
game_intro()