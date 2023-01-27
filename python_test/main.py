import pygame as pg
import sys
 
WIDTH = 360
HEIGHT = 480
 
WHITE = (255, 255 , 255)
 
class Player(pg.sprite.Sprite):
 
    def __init__(self, imagePath):
 
        # We first set the appropriate object variables
        self.image = pg.image.load(imagePath)
 
        # These are the coordinates of the player on the screen
        self.x, self.y = (WIDTH/2, HEIGHT/2)
 
        self.speed = 5
 
    def move(self, mov_tup):
 
        # mov_up contains changes made to the x and y positions
        # we simply add those changes to the player's position
        self.x += mov_tup[0]
        self.y += mov_tup[1]
 
 
def main():
    pg.init()   # initialise pygame
    pg.display.set_mode((WIDTH, HEIGHT)) # setting the window's dimensions
    mainS = pg.display.get_surface()
    FPS = 60 # Frames per second
 
    # the main window can now be accessed through mainS
 
    player = Player("player.png")
 
    # The clock is necessary for refreshing the screen
    clock = pg.time.Clock()   
    mov_tup = (0, 0)
    # This is the actual mainloop
    while True:
 
        for event in pg.event.get():
 
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
 
            elif event.type == pg.KEYDOWN:
 
                if event.key == pg.K_d:
                    mov_tup = (player.speed, 0)
                if event.key == pg.K_a:
                    mov_tup = (-player.speed, 0)
                if event.key == pg.K_w:
                    mov_tup = (0, -player.speed)
                if event.key == pg.K_s:
                    mov_tup = (0, player.speed)
 
        player.move(mov_tup)
        mainS.fill(WHITE)       # Fill the screen with the colour white
        mainS.blit(player.image, (player.x, player.y))  # Paint the player in the correct pos
        pg.display.update()
 
        # re-paint FPS times a second
        clock.tick(FPS)
 
 
main()