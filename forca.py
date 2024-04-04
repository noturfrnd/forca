import pygame
import math
import  random

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FORCA")

FPS = 60
clock = pygame.time.Clock()
run = True

# Buttons

radius = 24
space = 20
letters = []
x_start = round((WIDTH - (radius * 2 + space) * 13) / 2)
y_start = 540

A = 65

for i in range(26):
    x = x_start + space * 2 + ((radius * 2 + space) * (i % 13))
    y = y_start + ((i // 13) * (space + radius * 2))
    letters.append([x, y, chr(A + i), True])

font = pygame.font.SysFont("comicsans", 45)
WORD = pygame.font.SysFont("comicsans", 40)
TITLE = pygame.font.SysFont("comicsans", 70)

images = []
for i in range(0, 7):
    image = pygame.image.load("./img/man" + str(i + 1) + ".png")
    images.append(image)

print(images)

hangman = 0
lists = ["TESTE", "JAVA", "DOCKER", "DEVELOPER", "MERDA", "GITHUB", "R", "PYTHON", "BASH"]
words = random.choice(lists)
guessed = []  # to track the letters we have guessed


# Function to draw buttons, and hangman
def draw():
    win.fill((255, 255, 255))  # Display with white color

    # Title for the game
    # Updated title for better visibility
    title = TITLE.render("Hangman", 1, (0, 0, 0))
    # Title in center and then y-axis= 24
    win.blit(title, (WIDTH / 1.7 - title.get_width() / 2, 10))

    # Draw word on the screen
    disp_word = ""
    for letter in words:
        if letter in guessed:
            disp_word += letter + " "
        else:
            disp_word += "_ "

    text = WORD.render(disp_word, 1, (0, 0, 0))
    win.blit(text, (500, 250))

    # Buttons at center
    for btn_pos in letters:
        # Making button visible and invisible after clicking it
        x, y, ltr, visible = btn_pos

        if visible:
            pygame.draw.circle(win, (0, 0, 0), (x, y), radius, 4)
            txt = font.render(ltr, 1, (0, 0, 0))
            win.blit(txt, (x - txt.get_width() / 2, y - txt.get_height() / 2))

    win.blit(images[hangman], (50, 50))
    pygame.display.update()


while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():  # Triggering the event
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()

            for letter in letters:
                x, y, ltr, visible = letter

                if visible:
                    # To handle collision and to click the button exactly in the circle
                    dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)

                    if dist <= radius:
                        letter[3] = False  # To invisible the clicked button
                        guessed.append(ltr)
                        if ltr not in words:
                            hangman += 1

    # Deciding if you won the game or not
    won = True
    for letter in words:
        if letter not in guessed:
            won = False
            break

    if won:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0))
        text = WORD.render("YOU WON", 1, (129, 255, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(4000)
        print("WON")
        break

    if hangman == 6:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0))
        text = WORD.render("YOU LOST", 1, (255, 0, 5))
        answer = WORD.render("The answer is " + words, 1, (129, 255, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        win.blit(answer, ((WIDTH / 2 - answer.get_width() / 2),
                          (HEIGHT / 2 - text.get_height() / 2) + 70))

        pygame.display.update()
        pygame.time.delay(4000)
        print("LOST")
        break

pygame.quit()