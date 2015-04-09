'''
The goal of this assignment is to accomplish a tried and true single screen arena shooter game.  
Moving and shooting will be the primary mechanics along with the prescence of hostile agents.

Inspirations: 

Crimson Land - https://youtu.be/XD_EBXpUYX0
Smash TV - https://youtu.be/n6uyWTtuYxg
Astroids - https://youtu.be/WYSupJ5r2zo
Space Invaders - https://youtu.be/437Ld_rKM2s

Specifications:
The player should be able to moveIt and moveIt. 
The player shoud have access to at least two weapons 
Grade Levels (applies to the specifications portion of the rubric)
A - Full control against artificial agents that are actively aggressive - Smash TV
B - More dynamic controls shooting of mobile targets that don't show intelligence (although they might moveIt back) - Astroids
C - Simple moving and shooting against stationary or nearly stationary obstacles - Space Invaders
'''
import sys
import pygame
from const import *
from player import player
from enemy import enemy
from bullet import bullet
from state import state

pygame.init()
pygame.display.set_caption("Breakout")
scoreBoard = pygame.font.SysFont( "arial", 30 )
screen = pygame.display.set_mode((SCREEN_WID_HT, SCREEN_WID_HT))
clock = pygame.time.Clock()

gameState = state(scoreBoard, screen)
lastKey = '\0'
fire = False

# Instantiate Basic Rects
boundTop = pygame.Rect(ORIGIN, ORIGIN, SCREEN_WID_HT, BOUND_WID)
boundLeft = pygame.Rect(ORIGIN, ORIGIN, BOUND_WID, SCREEN_WID_HT)
boundRight = pygame.Rect(SCREEN_WID_HT-BOUND_WID, ORIGIN, BOUND_WID, SCREEN_WID_HT)

# Instantiate Rect-like Children
player = player(PLAYER_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, PLAYER_SPEED, 0)
bullet = bullet(player.getX(), player.getY(), PUCK_WD_HT, PUCK_WD_HT, -PLAYER_SPEED, PLAYER_SPEED, screen, gameState)
breakMe = enemy(BLOCK_X, BLOCK_Y, BLOCK_WID, BLOCK_HT, screen, gameState)

def main():
    
    #Player Control
    def moveIt(key):
        if key[pygame.K_LEFT]:
            player.checkIt("MOVE_LEFT")
        if key[pygame.K_RIGHT]:
            player.checkIt("MOVE_RIGHT")
        if key[pygame.K_UP]:
            player.checkIt("MOVE_UP")
        if key[pygame.K_DOWN]:
            player.checkIt("MOVE_DOWN")
        if key[pygame.K_SPACE]:
            bullet.fire(player.getX(),player.getY())
            
        # Handle Close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
    
    
    def checkIt():
        bullet.checkIt(player, boundLeft, boundRight, boundTop)
        breakMe.checkIt(bullet)
        
    
    def drawIt():
        screen.fill((BLACK))
        
        pygame.draw.rect(screen, WHITE, boundTop)
        pygame.draw.rect(screen, WHITE, boundLeft)
        pygame.draw.rect(screen, WHITE, boundRight)
        
        pygame.draw.rect(screen, RED, player)
        bullet.drawIt()
        breakMe.drawIt()
        
        if (gameState.getPLives() == 0 or breakMe.getRemaining() == 0):
            gameState.drawIt(SCORE_LBL, GAMEOVER_LBL)
            enemy(BLOCK_X, BLOCK_Y, BLOCK_WID, BLOCK_HT, screen, gameState)
            
            pygame.display.flip()
            pygame.time.delay(3000)
            gameState.resetGame()
        else:
            gameState.drawIt(SCORE_LBL, LIVES_LBL)
        
        pygame.display.flip()
    
    while True:
        moveIt(pygame.key.get_pressed())
            
        checkIt()
        bullet.moveIt(player.getPlayerDirection())
            
        drawIt()
        clock.tick(30)

if __name__ == '__main__':
    main()