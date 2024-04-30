


import pygame
import sys
import random

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 420, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle Lite")

font = pygame.font.Font(None, 40)


with open("words.txt", "r") as file:
    words = file.read().splitlines()
correct_word = random.choice(words).upper()
print("Correct word:", correct_word)


RECT_WIDTH = 75
RECT_HEIGHT = 75
RECT_GAP_X = 15
RECT_GAP_Y = 15
START_X = 65
START_Y = 65
WORD_GAP = 30

def draw_rectangles(x, y):
    rectangles = []
    for i in range(4):
        for j in range(6):  
            rect = pygame.Rect(x + i * (RECT_WIDTH + RECT_GAP_X), y + j * (RECT_HEIGHT + RECT_GAP_Y), RECT_WIDTH, RECT_HEIGHT)
            pygame.draw.rect(screen, BLACK, rect, 2)
            rectangles.append(rect)
    return rectangles

def draw_feedback(correct_word, guessed_word):
    feedback_x = 50
    feedback_y = 420
    for i, letter in enumerate(guessed_word):
        color = BLACK
        if letter in correct_word:
            if letter == correct_word[i]:
                color = GREEN
            else:
                color = YELLOW
        text_surface = font.render(letter, True, color)
        screen.blit(text_surface, (feedback_x + i * (RECT_WIDTH + RECT_GAP_X), feedback_y))

word_input_x = 50
word_input_y = 50

entered_words = [''] * 6  
feedback_shown = [False] * 6  

running = True
current_column = 0  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not feedback_shown[current_column]:
                    entered_word = entered_words[current_column]
                    draw_feedback(correct_word, entered_word)
                    feedback_shown[current_column] = True
                else:
                    current_column += 1
                    if current_column >= 6:  
                        break
                    word_input_x = 50 
                    entered_words[current_column] = ''  
                    feedback_shown[current_column] = False  
            elif event.key == pygame.K_BACKSPACE:  
                if entered_words[current_column]:
                    entered_words[current_column] = entered_words[current_column][:-1]
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(entered_words[current_column]) < 4:
                    entered_words[current_column] += event.unicode  

    screen.fill(WHITE)
    

    for i, word in enumerate(entered_words):
        for j, char in enumerate(word):
            rect_center_x = rectangles[i * 4 + j].centerx
            rect_center_y = rectangles[i * 4 + j].centery
            text_surface = font.render(char, True, BLACK)
            text_rect = text_surface.get_rect(center=(rect_center_x, rect_center_y))
            screen.blit(text_surface, (50 + j * (RECT_WIDTH + RECT_GAP_X), 50 + i * (RECT_HEIGHT + RECT_GAP_Y)))
            #draw_feedback(correct_word, entered_words)
            
 
    rectangles = draw_rectangles(word_input_x-30, word_input_y-30)
    for rect in rectangles:
        pygame.draw.rect(screen, GRAY, rect, 2)
    
    pygame.display.flip()

pygame.quit()
sys.exit()




