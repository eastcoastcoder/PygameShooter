import pygame, random
from const import *

class Enemy(pygame.Rect):
    # Init array to store rect blocks
    block = []
        
    # Init array to store block hits
    blockHit = []   
    
    def __init__(self, screen, state):
        self.xpos = BLOCK_X
        self.ypos = BLOCK_Y
        self.wid = BLOCK_WID
        self.ht = BLOCK_HT
        super(Enemy, self).__init__(self.xpos, self.ypos, self.wid, self.ht)
        
        self.screen = screen
        self.state = state
        
        self.generateBlock()
        pygame.mixer.init()
        pygame.mixer.music.load('hit.ogg')
        
    def generateBlock(self):
        while (self.ypos < CENTER-50):
            while (self.xpos < SCREEN_WID_HT-70):
                self.block.append(pygame.Rect(self.xpos, self.ypos, self.wid, self.ht))
                
                #Init hits to 0
                self.blockHit.append(0)
                #Gap between blocks (x)
                self.xpos += self.wid+BLOCK_OFFSET
            
            #Move to next row beginning
            self.xpos = BLOCK_X
            #Gap between blocks (y)
            self.ypos += self.ht+BLOCK_OFFSET
    
    def drawIt(self):
        for blocks in self.block:
            pygame.draw.rect(self.screen, ((random.randint(0,255),random.randint(0,255),random.randint(0,255))), blocks)
    
    def checkIt(self, bullet, player):
        for blocks in self.block:
            if bullet.colliderect(blocks):
                # Get index of colliding block
                curIndex = self.block.index(blocks)

                # Increment block hit attribute of colliding block
                self.blockHit[curIndex] += 1
                
                bullet.checkIt(player, self)
                
                # Play hit sound
                pygame.mixer.music.play(0, 0.6)
                
                # Remove block after hit more than once
                if (self.blockHit[curIndex] > 1):
                    pygame.draw.rect(self.screen, RED, blocks)
                    pygame.display.flip()
                    self.block.remove(blocks)
                    self.state.setPScore() 
                # Re-Color block after hit
                else:    
                    pygame.draw.rect(self.screen, GOLD, blocks)
                    pygame.display.flip()
                break
     
    # Accessors
    def getRemaining(self):
        return len(self.block)