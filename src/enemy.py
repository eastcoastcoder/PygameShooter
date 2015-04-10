import pygame 
from const import *

class enemy(pygame.Rect):
    # Init array to store rect blocks
    __block = []
    
    # Init array to store block hits
    __blockHit = []
    
    def __init__(self, xpos, ypos, wid, ht, screen, state):
        super(enemy, self).__init__(xpos, ypos, wid, ht)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__wid = wid
        self.__ht = ht
        self.__screen = screen
        self.__state = state
        
        self.__r = 30
        self.__g = 144
        self.__b = 255
        
        self.generateBlock()
        pygame.mixer.init()
        pygame.mixer.music.load('hit.ogg')
        
    def generateBlock(self):
        while (self.__ypos < CENTER-50):
            while (self.__xpos < SCREEN_WID_HT-70):
                self.__block.append(pygame.Rect(self.__xpos, self.__ypos, self.__wid, self.__ht))
                
                #Init hits to 0
                self.__blockHit.append(0)
                #Gap between blocks (x)
                self.__xpos += self.__wid+BLOCK_OFFSET
            
            #Move to next row beginning
            self.__xpos = BLOCK_X
            #Gap between blocks (y)
            self.__ypos += self.__ht+BLOCK_OFFSET
    
    def drawIt(self):
        for blocks in self.__block:
            pygame.draw.rect(self.__screen, (self.__r, self.__g, self.__b), blocks)
    
    def checkIt(self, bullet):
        for blocks in self.__block:
            if bullet.colliderect(blocks):
                # Get index of colliding block
                curIndex = self.__block.index(blocks)

                # Increment block hit attribute of colliding block
                self.__blockHit[curIndex] += 1
                
                # Bounce the bullet off block
                #bullet.hit()
                
                # Play hit sound
                pygame.mixer.music.play(0, 0.6)
                
                # Remove block after hit more than once
                if (self.__blockHit[curIndex] > 1):
                    pygame.draw.rect(self.__screen, RED, blocks)
                    pygame.display.flip()
                    self.__block.remove(blocks)
                    self.__state.setPScore() 
                # Re-Color block after hit
                else:    
                    pygame.draw.rect(self.__screen, GOLD, blocks)
                    pygame.display.flip()
                break
    
     
    # Accessors
    def getRemaining(self):
        return len(self.__block)

    def resetXpos(self):
        self.__xpos = BLOCK_X