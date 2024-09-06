import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Cyan = (0, 255, 255)
Magenta = (255, 0, 255)
Orange = (255, 128, 0)
Lightblue = (3, 161, 252)
Darkgreen = (16, 143, 31)
Crazyyellow = (217, 217, 17)


display_surface.fill(Black)

Center = (100,100)
radius = 100
pygame.draw.circle(display_surface, Yellow, Center, radius)

Center = (500,100)
radius = 50
pygame.draw.circle(display_surface, White, Center, radius)

Start = (400, 500)
End = (500, 300)
pygame.draw.line(display_surface, Darkgreen, Start, End, 50)

Center = (400,100)
radius = 10
pygame.draw.circle(display_surface, White, Center, radius)



Center = (409,140)
radius = 10
pygame.draw.circle(display_surface, Red, Center, radius)

Start = (100, 300)
End = (300, 500)
pygame.draw.line(display_surface, Darkgreen, Start, End, 50)

Top_left_x = 208
Top_Left_y = 100
Width = 150
Height = 400
Data = (Top_left_x, Top_Left_y, Width, Height)
pygame.draw.rect(display_surface, Crazyyellow, Data)


Top_left_x = 150
Top_Left_y = 400
Width = 300
Height = 150
Data = (Top_left_x, Top_Left_y, Width, Height)
pygame.draw.rect(display_surface, Darkgreen, Data)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()