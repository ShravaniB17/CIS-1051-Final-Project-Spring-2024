'''
import pygame
import random

pygame.init()


Words = open("Words.txt","r")


WIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("Starting Tiles.png")
#BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

KEYBOARD = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

SCREEN.fill("white")
SCREEN.blit(BACKGROUND) #, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75


guessCount = 0

guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
'''
import pygame
import random

pygame.init()


WIDTH, HEIGHT = 450, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
FILLED_OUTLINE = "#878a8c"
guessesCount = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_bg_x = 110


screen.fill((255, 255, 255))
def tiles():
    for x in range(4):
        for y in range(6):
            pygame.draw.rect(screen, (0, 0, 0), (10 + 110*x, 10 + 110*y, 100, 100), width = 3)


tiles()
pygame.display.update()


letterXspacing = 12
letterYspacing = 12
letterSize = 75

# Main game loop will go here

def read_random_word():
    with open("Words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)
word = read_random_word()



# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
