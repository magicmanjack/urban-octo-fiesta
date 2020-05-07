import pygame
import player

pygame.init()
screen = pygame.display.set_mode((800, 600))

g_acc = 3

def update():
    player.x_acc = 0
    player.y_acc = g_acc
    under_control = False
    if(pygame.key.get_pressed()[pygame.K_LEFT]):
        player.x_acc += -2
        under_control = True
    if(pygame.key.get_pressed()[pygame.K_RIGHT]):
        player.x_acc += 2
        under_control = True
    if(pygame.key.get_pressed()[pygame.K_SPACE]):
        player.y_acc += player.jump_acc
    if(not under_control):
        player.slow_down_x()
    
    player.update_pos()
                    
def draw():
    pygame.draw.rect(screen, (0, 255, 0), player.r)

clock = pygame.time.Clock()
loop = True
while(loop):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            loop = False

    clock.tick(30) # Limits to 30 FPS
    update()
    screen.fill((0, 0, 0))
    draw()
    pygame.display.flip()

pygame.quit()
