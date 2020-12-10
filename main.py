import pygame
import sys
import time
from settings import Settings
from player import Player_object
from meteors import Meteor

def run_game():
    pygame.init()
    settings=Settings()
    welcome = True
    running = False
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    background_image = pygame.image.load('images/space.jpg')
    bg_image = pygame.transform.scale(background_image, (1100, 560))
    screen.blit(bg_image, (0, 0))
    test = pygame.draw.rect(screen, (255, 255, 255), (450, 200, 200, 100))
    font = pygame.font.SysFont('Arial', 60)
    screen.blit(font.render('PLAY', True, (255, 0, 0)), (490, 210))
    pygame.display.update()
    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()
                if pressed and test.collidepoint(pos):
                    running = True
            elif event.type == pygame.MOUSEBUTTONUP:
                welcome = False
    while running:
        pygame.mixer_music.load('game_background_music.mp3')
        pygame.mixer_music.play(-1, 0.0)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Hover in Space")
        background_image = pygame.image.load('images/space.jpg')
        bg_image = pygame.transform.scale(background_image,(1100,560))
        screen.blit(bg_image, (0, 0))
        fps = 100
        fpsclock = pygame.time.Clock()
        player_obj = Player_object(screen)
        while True:
            screen.blit(bg_image,(0,0))
            player_obj.blitme()
            status = True
            meteor_obj_1 = Meteor(screen)
            meteor_obj_2 = Meteor(screen)
            meteor_obj_2.rect.bottom += 100
            meteor_obj_3 = Meteor(screen)
            meteor_obj_3.rect.bottom += 400
            position_update_m1, position_update_m2, position_update_m3 = 0, 0, 0
            score = 0
            while status:
                if meteor_obj_1.rect.left <0:
                    update = meteor_obj_1.rect.bottom
                    meteor_obj_1 = Meteor(screen)
                    meteor_obj_1.update_position(update,0)
                    if update >= 500:
                        position_update_m1 += 30
                        meteor_obj_1.update_position(update,position_update_m1,update)
                if meteor_obj_2.rect.left <0:
                    update = meteor_obj_2.rect.bottom
                    meteor_obj_2 = Meteor(screen)
                    meteor_obj_2.update_position(update,0)
                    if update >= 500:
                        position_update_m2 += 80
                        meteor_obj_2.update_position(update,position_update_m2,update)
                if meteor_obj_3.rect.left <0:
                    update = meteor_obj_3.rect.bottom
                    meteor_obj_3 = Meteor(screen)
                    meteor_obj_3.update_position(update,0)
                    if update >= 500:
                        position_update_m3 += 40
                        meteor_obj_3.update_position(update,position_update_m3,update)
                screen.blit(bg_image, (0, 0))
                score += 1
                pygame.draw.rect(screen,(0, 0, 0),(850, 20, 200, 60))
                font = pygame.font.SysFont('Arial', 35)
                screen.blit(font.render(str(score), True, (255, 255, 255)), (870, 30))
                pygame.draw.rect(screen, (0, 0, 0), (70, 20, 100, 40), -1)
                font = pygame.font.SysFont('Arial', 30)
                file_open = open("scores.txt", "r")
                lines = file_open.readlines()
                file_open.close()
                if lines:
                    lines = [x.strip() for x in lines]
                    score_array = list(map(int, lines))
                    screen.blit(font.render('BEST SCORE: ' + str(max(score_array)), True, (255, 255, 255, 128)), (30, 20))
                else:
                    screen.blit(font.render('BEST SCORE: 0', True, (255, 255, 255, 128)), (30, 20))
                player_obj.blitme()
                meteor_obj_1.rect.left -= 7
                meteor_obj_2.rect.left -= 14
                meteor_obj_3.rect.left -= 10
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            player_obj.moving_top = True
                        elif event.key == pygame.K_DOWN:
                            player_obj.moving_bottom = True
                        elif event.key == pygame.K_LEFT:
                            player_obj.moving_left = True
                        elif event.key == pygame.K_RIGHT:
                            player_obj.moving_right = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            player_obj.moving_top = False
                        elif event.key == pygame.K_DOWN:
                            player_obj.moving_bottom = False
                        elif event.key == pygame.K_LEFT:
                            player_obj.moving_left = False
                        elif event.key == pygame.K_RIGHT:
                            player_obj.moving_right = False
                player_obj.update()
                meteor_obj_1.blitme()
                meteor_obj_2.blitme()
                meteor_obj_3.blitme()
                pygame.display.update()
                fpsclock.tick(fps)
                if player_obj.rect.colliderect(meteor_obj_1.rect) or player_obj.rect.colliderect(meteor_obj_2.rect) or player_obj.rect.colliderect(meteor_obj_3.rect):
                    file_open = open("scores.txt", "a")
                    file_open.write(str(score)+'\n')
                    file_open.close()
                    pygame.display.update()
                    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1100, 550))
                    font = pygame.font.SysFont('Arial', 90)
                    screen.blit(font.render('GAME OVER', True, (255, 0, 0)), (340, 210))
                    pygame.display.update()
                    time.sleep(1)
                    sys.exit()

run_game()