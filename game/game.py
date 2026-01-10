import random #for RNG
import pygame
pygame.init()

black = (0 ,0, 0)
white = (255, 255, 255)
bg = pygame.image.load('cat hands.jpg')
jumping_cat = pygame.image.load('pixel cat.png')
bad_dogs = pygame.image.load('pixel dog.png')
#colors and images

width = 750
height = 500
#dimensions

score = 0
player_x = 50
player_y = 325
y_change = 0
x_change = 0
gravity = 1
fps = 60
background = pygame.transform.scale(bg, (width, height))
timer = pygame.time.Clock()
player_image = pygame.transform.scale(jumping_cat, (50, 75))
enemies_image = pygame.transform.scale(bad_dogs, (25, 50))
enemies = [300, 450, 600]
enemies_speed = 2
alive = False
font = pygame.font.Font('FreeSansBold.ttf', 16)
#game variables

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jump Cat')
#game window

gameRunning = True
while gameRunning:
    timer.tick(fps)
    screen.blit(background, (0,0))
    score_text = font.render(f'Score: {score}', True, black, white)
    screen.blit(score_text, (400, 250))
    floor = pygame.draw.rect(screen, black, [0, 400, width, 5])
#GUI
    
    player_rect = player_image.get_rect()
    player_rect.x = player_x
    player_rect.y = player_y
    player = screen.blit(player_image, player_rect)
#add player to display as rect
    
    enemy0_rect = enemies_image.get_rect()
    enemy0_rect.x = enemies[0]
    enemy0_rect.y = 350
    enemy0 = screen.blit(enemies_image, enemy0_rect)
    enemy1_rect = enemies_image.get_rect()
    enemy1_rect.x = enemies[1]
    enemy1_rect.y = 350
    enemy1 = screen.blit(enemies_image, enemy1_rect)
    enemy2_rect = enemies_image.get_rect()
    enemy2_rect.x = enemies[2]
    enemy2_rect.y = 350
    enemy2 = screen.blit(enemies_image, enemy2_rect)
#add enemies to display as rect
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameRunning = False #prevent infinite loop / allow exit
        if event.type == pygame.KEYDOWN and not alive: 
            if event.key == pygame.K_SPACE: 
                enemies = [300, 450, 600]
                player_x = 50
                score = 0
                alive = True
        if event.type == pygame.KEYDOWN and alive:
            if event.key == pygame.K_UP and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 6 #player speed
            if event.key == pygame.K_LEFT:
                x_change = -6 #player speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0
#player movement

    for i in range(len(enemies)):
        if alive:
            enemies[i] -= enemies_speed
            if enemies[i] < -20:
                enemies[i] = random.randint(750, 850)
                score += 1
            if player.colliderect(enemy0) or player.colliderect(enemy1) or player.colliderect(enemy2):
                alive = False

    if 0 <= player_x <= 700:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 700:
        player_x = 700
#boundaries
                
    if y_change > 0 or player_y < 325:
        player_y -= y_change
        y_change -= gravity
    if player_y > 325:
        player_y = 325 #preventing glitching through floor
    if player_y == 325 and y_change < 0:
        y_change = 0
#jumping
            
    pygame.display.flip()
    
pygame.quit() 
