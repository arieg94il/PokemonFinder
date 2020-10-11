import pygame, sys
from pygame.locals import *
from Colors import SKY_BLUE, BLUE, RED
from Dimentions import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_START_POSITION, MOVE_SPEED, \
    INTRO_IMG_HEIGHT, INTRO_IMG_WIDTH
from Player_Class import Player
from Images.Images import player_image, bul_image, char_image, evee_image, pika_image, squir_image, Pikachu_Intro, \
    programIcon, Ash
from Pokemon_Class import Pokemon
import random

pygame.init()
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Pokemon Finder')
clock = pygame.time.Clock()
Screen.fill(SKY_BLUE)
pygame.display.set_icon(programIcon)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.mixer.init()
Catch_Sound = pygame.mixer.Sound("Audio/catch.wav")
Miss_Sound = pygame.mixer.Sound("Audio/miss.wav")
BG_Music = pygame.mixer.music.load("Audio/background_music.wav")


def About():
    intro = True
    while intro:

        Screen.fill(SKY_BLUE)
        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            GoBack_Game_Text = myfont.render('Go Back', False, BLUE)

            Screen.blit(GoBack_Game_Text, (20, SCREEN_HEIGHT - 70))

            if (20 < mouse[0] < 135 and 550 < mouse[1] < 570) and click[0] == 1:
                Menu()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        Screen.blit(Ash, (SCREEN_WIDTH - INTRO_IMG_WIDTH, int(SCREEN_HEIGHT - 350)))

        mouse = pygame.mouse.get_pos()

        GoBack_Game_Text = myfont.render('Go Back', False, BLUE)

        Screen.blit(GoBack_Game_Text, (20, SCREEN_HEIGHT - 70))

        if 20 < mouse[0] < 135 and 550 < mouse[1] < 570:
            Quit_Game_Text = myfont.render('Go Back', False, RED)
            Screen.blit(Quit_Game_Text, (20, SCREEN_HEIGHT - 70))

        About_Title = myfont.render('Can you Help Ash?', False, BLUE)
        Screen.blit(About_Title, (int(SCREEN_WIDTH / 2 - 150), 20))

        Description1 = myfont.render('Ash is set on a goal catching all the Pokemons!', False, BLUE)
        Screen.blit(Description1, (int(SCREEN_WIDTH / 2 - 350), int((SCREEN_HEIGHT / 2) - 200)))

        Description2 = myfont.render('Try to catch as many Pokemons as you can.', False, BLUE)
        Screen.blit(Description2, (int(SCREEN_WIDTH / 2 - 350), int((SCREEN_HEIGHT / 2) - 150)))

        Description3 = myfont.render('Every Pokemon you catch, you recieve a point.', False, BLUE)
        Screen.blit(Description3, (int(SCREEN_WIDTH / 2 - 350), int((SCREEN_HEIGHT / 2) - 100)))

        Description4 = myfont.render('Every Pokemon you miss, you lose a point.', False, BLUE)
        Screen.blit(Description4, (int(SCREEN_WIDTH / 2 - 350), int((SCREEN_HEIGHT / 2) - 50)))

        Description5 = myfont.render('Best of luck!', False, BLUE)
        Screen.blit(Description5, (int(SCREEN_WIDTH / 2 - 350), int((SCREEN_HEIGHT / 2) - 0)))

        pygame.display.update()

def Game_Loop():

    player_position = PLAYER_START_POSITION

    pokemon_ball = Player(player_image, player_position)
    pokemons_set_1 = Pokemon([bul_image, char_image, evee_image, pika_image, squir_image], 0,0,0)
    selected_image_index = random.randint(0, (len(pokemons_set_1.images) - 1))

    counter = 0
    game_loop =True

    while game_loop:

        pokemons_set_1.y_position=pokemons_set_1.drop()
        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if (20 < mouse[0] < 135 and 550 < mouse[1] < 570) and click[0] == 1:
                Menu()

            if (644 < mouse[0] < 759 and 536 < mouse[1] < 572) and click[0] == 1:
                counter =0

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_position = pokemon_ball.move_left()

                elif event.key == pygame.K_RIGHT:
                    player_position = pokemon_ball.move_right()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pokemons_set_1.y_position==0:
            pokemons_set_1.x_position = random.randint(0, SCREEN_WIDTH-PLAYER_WIDTH)
            selected_image_index=random.randint(0, (len(pokemons_set_1.images) - 1))

        touch = 0

        if ((pokemons_set_1.x_position <= pokemon_ball.position[0] < pokemons_set_1.x_position+PLAYER_WIDTH) \
                or (pokemons_set_1.x_position <= pokemon_ball.position[0]+PLAYER_WIDTH < pokemons_set_1.x_position+PLAYER_WIDTH)) \
                and (pokemons_set_1.y_position <= pokemon_ball.position[1] < pokemons_set_1.y_position+PLAYER_HEIGHT):
            counter+=1
            touch=1
            pokemons_set_1.y_position = 0
            pokemons_set_1.x_position = random.randint(0, SCREEN_WIDTH - PLAYER_WIDTH)
            selected_image_index = random.randint(0, (len(pokemons_set_1.images) - 1))
            pygame.mixer.Sound.play(Catch_Sound)

        if (touch == 0) and (pokemons_set_1.y_position == 600):
            counter-=1
            pygame.mixer.Sound.play(Miss_Sound)

        Screen.fill(SKY_BLUE)

        Quit_Game_Text = myfont.render('Quit', False, BLUE)
        Screen.blit(Quit_Game_Text, (20, SCREEN_HEIGHT - 70))

        Restart_Game_Text = myfont.render('Restart', False, BLUE)
        Screen.blit(Restart_Game_Text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70))

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 20 < mouse[0] < 135 and 550 < mouse[1] < 570:
            Quit_Game_Text = myfont.render('Quit', False, RED)
            Screen.blit(Quit_Game_Text, (20, SCREEN_HEIGHT - 70))

        if 644 < mouse[0] < 759 and 536 < mouse[1] < 572:
            Restart_Game_Text = myfont.render('Restart', False, RED)
            Screen.blit(Restart_Game_Text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70))


        Screen.blit((myfont.render("Score: " + str(counter), True, BLUE)),(20,20))

        Screen.blit(pokemon_ball.image, player_position)
        Screen.blit(pokemons_set_1.images[selected_image_index], (pokemons_set_1.x_position, pokemons_set_1.y_position))

        Clock.tick(15)

        pygame.display.update()

def Menu():

    newGame_color=BLUE
    aboutGame_color=BLUE
    quitGame_color=BLUE


    intro = True
    while intro:
        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 488 > mouse[0] > 338 and 295 > mouse[1] > 258:
                newGame_color=RED
                aboutGame_color = BLUE
                quitGame_color = BLUE

            if 430 > mouse[0] > 338 and 358 > mouse[1] > 330:
                newGame_color = BLUE
                aboutGame_color = RED
                quitGame_color = BLUE

            if 405 > mouse[0] > 338 and 425 > mouse[1] > 401:
                newGame_color = BLUE
                aboutGame_color = BLUE
                quitGame_color = RED

            if (488 > mouse[0] > 338 and 295 > mouse[1] > 258) and click[0]==1:
                Game_Loop()

            if (430 > mouse[0] > 338 and 358 > mouse[1] > 330) and click[0]==1:
                About()

            if (405 > mouse[0] > 338 and 425 > mouse[1] > 401) and click[0]==1:
                pygame.quit()
                sys.exit()

            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

        Screen.fill(SKY_BLUE)
        Screen.blit(Pikachu_Intro, (int(SCREEN_WIDTH / 2) - int(INTRO_IMG_HEIGHT / 2), 20))

        New_Game_Text = myfont.render('New Game', False, newGame_color)
        About_Game_Text = myfont.render('About', False, aboutGame_color)
        Quit_Game_Text = myfont.render('Quit', False, quitGame_color)

        Screen.blit(New_Game_Text, (int((SCREEN_WIDTH / 2) - 60), 250))
        Screen.blit(About_Game_Text, (int((SCREEN_WIDTH / 2) - 60), 320))
        Screen.blit(Quit_Game_Text, (int((SCREEN_WIDTH / 2) - 60), 390))

        pygame.display.update()

pygame.mixer.music.play(-1)
Menu()




