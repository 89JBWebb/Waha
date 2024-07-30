import math
import pygame
 
def distance(a, b):
    return math.sqrt(math.pow((a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2) )


x = []

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (660, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
selected = None
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 48)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(x)):
                if distance(pygame.mouse.get_pos(), x[i][0]) < x[i][1]:
                    selected = i
                    break
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            selected = None
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x+= [[pygame.mouse.get_pos(), 24]]

    if selected is not None:
        valid = True
        for i in range(len(x)):
            print(pygame.mouse.get_pos())
            if i != selected and distance(pygame.mouse.get_pos(), x[i][0]) <+ x[i][1]+x[selected][1]:
                valid = False
                break
        if valid:
            x[selected][0] = pygame.mouse.get_pos()

    screen.fill((200,200,200))
    for i in range(len(x)):
        pygame.draw.circle(screen, (0, 0, 255), x[i][0], x[i][1])
        text = font.render(str(i+1), True, (255,255,255))
        screen.blit(text, (x[i][0][0]-x[i][1] // 2,x[i][0][1]-(x[i][1]*1.5) ))
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()