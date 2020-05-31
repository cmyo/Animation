import sys
import pygame
import time

class Dino(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()

        # load the sprite sheet 
        sheet=pygame.image.load("dinos.jpg").convert() 

        # create a list of images that correspond to the different animation
        # frames - in this case 22 different frames
        self.frame=[]
        for i in range(12):
           self.frame.append(pygame.Surface([75,65]).convert())
           patch = (75*(i%4),65*(i//4),75,95)
##           patch = (5+123*(i%8),5+112*(i//8),75,115)                            
           self.frame[i].blit(sheet,(0,0), patch)
           self.frame[i].set_colorkey((255,255,255))

        # set the image and rect properties to the first frame.
        self.anim_frame=0
        self.image=self.frame[0]                            
        self.rect=self.image.get_rect()

        # set the initial position of the sprite and other attributes
        self.rect.x=x
        self.rect.y=y                             
        self.accel=10
        self.deltax=0
        self.deltay=0



    def update(self):
        # increase the animation frame to the next panel
        self.anim_frame = (self.anim_frame+1)%12

        # set the image from the animation frame, flip it if it is moving
        # to the right
        if self.deltax<0:
            self.image=self.frame[self.anim_frame]
        else:
            self.image=pygame.transform.flip(self.frame[self.anim_frame],True,False)

        # modify the position of the bird, make sure it stays in bounds
        self.deltay += self.accel*0.1
        self.rect.y += self.deltay*.1 
        if self.rect.y >450:
            self.deltay = 0
            self.rect.y = 450
                
        self.rect.x += self.deltax

        # reset gravity in case the user had hit he space bar to flap wings
        self.accel=10
                             
                             


def main():

    pygame.init()


    # Create a display surface which you can draw on.  This is 800 by 600 pixels.
    main_surface = pygame.display.set_mode((1020,680))

    # draw the background
    background=pygame.image.load("flyingdinoclub.jpg")
    main_surface.blit(background,(0,0))


    # create the sprites and initialize the sprite groups
    dino=Dino(20,200)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(dino)

    
    # Below is the game loop.  It erases the old screen, changes the position
    # and draws the new screen.
    
                            
    while True:


        # The below for loop checks to see if someone has tried to exit the game.
        # if so close out gracefully.

        #do other event checks here too like look for keyboard or mouse input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == 32:
                    dino.accel=-500
                elif key == pygame.K_LEFT:
                   dino.deltax=-3
                elif key == pygame.K_RIGHT:
                   dino.deltax=3
                else:
                   dino.deltax=0
            
             
        #update the position variables and image

        all_sprites.update()
        main_surface.blit(background, (0,0))

        # redraw the screen
    
        pygame.draw.rect(main_surface,(255,255,255),(0,0,1200,0))

        all_sprites.draw(main_surface)


        # flip the drawn surface onto the monitor
        pygame.display.flip()

        # keep it from going too fast
        time.sleep(0.05)  

if __name__=='__main__':    
    main()

# OK, it works.  Good work getting most of the white hidden. The patches can
# be adjusted a little better so that the animation will be smoother.
# Score: 95
