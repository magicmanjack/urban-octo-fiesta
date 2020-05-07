import pygame

r = pygame.Rect(350, 300, 100, 100)

x_vel = 0
max_x_vel = 10
x_acc = 0
de_x_acc = -1

y_vel = 0
y_acc = 0
jump_acc = -50

def slow_down_x():
    global x_vel
    global de_x_acc

    if(x_vel > 0):
        if(x_vel + de_x_acc < 0):
            x_vel = 0
        else:
            x_vel += de_x_acc
    if(x_vel < 0):
        if(x_vel - de_x_acc > 0):
            x_vel = 0
        else:
            x_vel -= de_x_acc

def update_pos():
    global x_vel
    global max_x_vel
    global x_acc
    global y_vel
    global y_acc
    global r
    
    if(x_vel + x_acc < -max_x_vel):
        x_vel = -max_x_vel
    elif(x_vel + x_acc > max_x_vel):
        x_vel = max_x_vel
    else:
        x_vel += x_acc

    y_vel += y_acc
    
    r.x += x_vel
    r.y += y_vel
    
    
    
    



