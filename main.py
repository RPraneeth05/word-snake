import pygame, sys
from button import Button
from random import randrange, choice


pygame.init()

SCREEN = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play(difficulty):

    WINDOW = 640
    TILE_SIZE = 32
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

    # Time control
    time, time_step = 0, 120

    complexity = difficulty
    if complexity == 1:
        # WINDOW = 480
        RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
        time, time_step = 0, 100
    elif complexity == 2:
        # WINDOW = 320
        RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
        time, time_step = 0, 80

    existing_rects = []



    def get_random_position(existing_rects):
        while True:
            new_pos = [randrange(*RANGE), randrange(*RANGE)]
            new_rect = pygame.Rect(new_pos[0], new_pos[1], TILE_SIZE, TILE_SIZE)
            if not any(new_rect.colliderect(r) for r in existing_rects):
                return new_pos


    # Snake definition
    snake = pygame.rect.Rect([0, 0, TILE_SIZE, TILE_SIZE])
    snake.center = get_random_position(existing_rects)
    length = 1
    segments = [snake.copy()]
    snake_dir = (0, 0)



    # words = ["BENCH", "BUNCH", "CHAIR", "CHALK", "CHASE", "CLIFF", "CLOUD",
    #         "DANCE", "FLASH", "GREET", "GLASS", "PLANT", "SHINE", "UNION"]
    words = ["PENIS"]

    word = choice(words)
    word_list = list(word)

    # Food definition


    food1 = pygame.image.load(f'./src/letters/{word_list[0]}.png')
    food1Rect = food1.get_rect()
    food1Rect.center = get_random_position(existing_rects)
    existing_rects.append(food1Rect)

    food2 = pygame.image.load(f'./src/letters/{word_list[1]}.png')
    food2Rect = food2.get_rect()
    food2Rect.center = get_random_position(existing_rects)
    existing_rects.append(food2Rect)

    food3 = pygame.image.load(f'./src/letters/{word_list[2]}.png')
    food3Rect = food3.get_rect()
    food3Rect.center = get_random_position(existing_rects)
    existing_rects.append(food3Rect)

    food4 = pygame.image.load(f'./src/letters/{word_list[3]}.png')
    food4Rect = food4.get_rect()
    food4Rect.center = get_random_position(existing_rects)
    existing_rects.append(food4Rect)

    food5 = pygame.image.load(f'./src/letters/{word_list[4]}.png')
    food5Rect = food5.get_rect()
    food5Rect.center = get_random_position(existing_rects)
    existing_rects.append(food5Rect)

    # Pygame initialization
    screen = pygame.display.set_mode([WINDOW] * 2)
    clock = pygame.time.Clock()
    count = 0

    # Event loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake_dir = (0, -TILE_SIZE)
                if event.key == pygame.K_a:
                    snake_dir = (-TILE_SIZE, 0)
                if event.key == pygame.K_s:
                    snake_dir = (0, TILE_SIZE)
                if event.key == pygame.K_d:
                    snake_dir = (TILE_SIZE, 0)

        # Fill screen
        screen.fill('black')

        # Draw food
        # pygame.draw.rect(screen, 'red', food1)
        # pygame.draw.rect(screen, 'red', food2)
        # pygame.draw.rect(screen, 'red', food3)
        # pygame.draw.rect(screen, 'red', food4)
        # pygame.draw.rect(screen, 'red', food5)
        screen.blit(food1, food1Rect)
        screen.blit(food2, food2Rect)
        screen.blit(food3, food3Rect)
        screen.blit(food4, food4Rect)
        screen.blit(food5, food5Rect)

        # Draw snake
        [pygame.draw.rect(screen, 'green', segment) for segment in segments]

        # Move snake
        time_now = pygame.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]

        # Wall collisions and eating self
        self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
            # length, snake_dir = 1, (0, 0)
            # segments = [snake.copy()]
            end_screen(length)

        # Check food
        if snake.center == food1Rect.center:
            count += 1
            food1Rect.center = (-999, -999)
            if count != 1:
                # count = 0
                # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
                # length, snake_dir = 1, (0, 0)
                # segments = [snake.copy()]
                end_screen(length)
            # length += 1

        if snake.center == food2Rect.center:
            count += 1
            food2Rect.center = (-999, -999)
            if count != 2:
                # count = 0
                # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
                # length, snake_dir = 1, (0, 0)
                # segments = [snake.copy()]
                end_screen(length)
            # length += 1

        if snake.center == food3Rect.center:
            count += 1
            food3Rect.center = (-999, -999)
            if count != 3:
                # count = 0
                # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
                # length, snake_dir = 1, (0, 0)
                # segments = [snake.copy()]
                end_screen(length)
            # length += 1

        if snake.center == food4Rect.center:
            count += 1
            food4Rect.center = (-999, -999)
            if count != 4:
                # count = 0
                # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
                # length, snake_dir = 1, (0, 0)
                # segments = [snake.copy()]
                end_screen(length)
            # length += 1

        if snake.center == food5Rect.center:
            count += 1
            food5Rect.center = (-999, -999)
            if count != 5:
                # count = 0
                # snake.center, food1Rect.center, food2Rect.center, food3Rect.center, food4Rect.center, food5Rect.center = get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects), get_random_position(existing_rects)
                # length, snake_dir = 1, (0, 0)
                # segments = [snake.copy()]
                end_screen(length)

            count = 0

            word = choice(words)
            word_list = list(word)

            existing_rects = []

            food1 = pygame.image.load(f'./src/letters/{word_list[0]}.png')
            food1Rect = food1.get_rect()
            food1Rect.center = get_random_position(existing_rects)
            existing_rects.append(food1Rect)

            food2 = pygame.image.load(f'./src/letters/{word_list[1]}.png')
            food2Rect = food2.get_rect()
            food2Rect.center = get_random_position(existing_rects)
            existing_rects.append(food2Rect)

            food3 = pygame.image.load(f'./src/letters/{word_list[2]}.png')
            food3Rect = food3.get_rect()
            food3Rect.center = get_random_position(existing_rects)
            existing_rects.append(food3Rect)

            food4 = pygame.image.load(f'./src/letters/{word_list[3]}.png')
            food4Rect = food4.get_rect()
            food4Rect.center = get_random_position(existing_rects)
            existing_rects.append(food4Rect)

            food5 = pygame.image.load(f'./src/letters/{word_list[4]}.png')
            food5Rect = food5.get_rect()
            food5Rect.center = get_random_position(existing_rects)
            existing_rects.append(food5Rect)

            length += 1

        # Enable display
        pygame.display.flip()
        clock.tick(60)

def start_screen():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("Word Hunter", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 140))


        DIFF = get_font(50).render("Difficulty", True, "#b68f40")
        DIFF_TXT = DIFF.get_rect(center=(320, 250))
        EASY = Button(image=pygame.image.load("assets/tiny.png"), pos=(160, 350), 
                            text_input="1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        MEDIUM = Button(image=pygame.image.load("assets/tiny.png"), pos=(320, 350), 
                            text_input="2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        HARD = Button(image=pygame.image.load("assets/tiny.png"), pos=(480, 350), 
                            text_input="3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/small.png"), pos=(320, 500), 
                            text_input="Quit", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(DIFF, DIFF_TXT)

        for button in [EASY, MEDIUM, HARD, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY.checkForInput(MENU_MOUSE_POS):
                    instructions(0)
                if MEDIUM.checkForInput(MENU_MOUSE_POS):
                    instructions(1)
                if HARD.checkForInput(MENU_MOUSE_POS):
                    instructions(2)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def instructions(carryover):
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("WASD to move", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 140))
        INS = get_font(25).render("Figure out the word", True, "#b68f40")
        INSR = MENU_TEXT.get_rect(center=(320, 200))
        INS2 = get_font(25).render("Pick up letters in order", True, "#b68f40")
        INSR2 = MENU_TEXT.get_rect(center=(320, 260))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/small.png"), pos=(320, 320), 
                            text_input="Continue", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/small.png"), pos=(320, 500), 
                            text_input="Quit", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(INS, INSR)
        SCREEN.blit(INS2, INSR2)
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(carryover)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def end_screen(score):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Score: " + str(score - 1), True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 140))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/small.png"), pos=(320, 320), 
                            text_input="Retry", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/small.png"), pos=(320, 500), 
                            text_input="Quit", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_screen()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

start_screen()