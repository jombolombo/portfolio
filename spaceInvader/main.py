import pygame
import random
import math
# intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load(
    "C:/Users/Admin/OneDrive/Documents/Python Scripts/games/spaceInvader/milkyWay.jpg")
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(
    "C:/Users/Admin/OneDrive/Documents/Python Scripts/games/spaceInvader/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(
    "C:/Users/Admin/OneDrive/Documents/Python Scripts/games/spaceInvader/spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyY = []
enemyX = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(
    "C:/Users/Admin/OneDrive/Documents/Python Scripts/games/spaceInvader/alien.png"))
    enemyY.append(random.randint(50, 150))
    enemyX.append(random.randint(0, 736))
    enemyX_change.append(4) 
    enemyY_change.append(40)

# bullet

# ready- state means you can see the bullet on the screen
# Fire- the bullet is currently moving
bulletImg = pygame.image.load(
    "C:/Users/Admin/Documents/Python Scripts/games/spaceInvader/bullet.png")
bulletY = 480
bulletX = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_value= 0
font = pygame.font.Font('freesansbold.ttf',32 )
textX = 10
textY = 10

def showScore(x, y):
    # text gets rendered
    score = font.render("score: " + str(score_value),True,(255,255,255))
    screen.blit(score,(x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
                         math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


def player(x, y):
    # blit is for drawing on screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # blit is for drawing on screen
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    # global lets you use global variables inside function.
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:

    # create a background fill uses RGB (0-225)
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # pygame.QUIT is the action that happens when you press the exit button
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed check whether it is right or left.
        if(event.type == pygame.KEYDOWN):
            #print(" a keystroke has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # CHecking for boundaries
    playerX += playerX_change
    if playerX > 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] > 736:
            enemyX[i] = 736
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
         #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision :
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            enemyY[i] = random.randint(50, 150)
            enemyX[i] = random.randint(0, 736)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if(bullet_state is "fire"):
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    
    player(playerX, playerY)
    showScore(textX,textY)
    # code to update screen
    pygame.display.update()
