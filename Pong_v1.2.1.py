import pygame
import sys
from pygame import Rect, Color


def you_lose():
    Losing_text = "Game Over!"
    draw_winner(Losing_text)


def ball_animations():
    global ball_speed_x, ball_speed_y, Score, text_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player):
        ball_speed_x *= -1
        Score += 10

    if ball.colliderect(opponent):
        ball_speed_x *= 1

    if ball.right > screen_width - 5:
        ball_speed_x = 0
        ball_speed_y = 0
        you_lose()


def show_score(x, y):
    score = font.render('Score: ' + str(Score), True, (255, 255, 255))
    screen.blit(score, (x, y))


def high_score(x, y):
    highest_score = font.render('High Score: ' + str(best_points), True, (255, 255, 255))
    screen.blit(highest_score, (x, y))


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animations():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def draw_winner(text):
    draw_text = Winner_font.render(text, True, White)
    Win.blit(draw_text, (screen_width // 2 - draw_text.get_width() //
                         2, screen_height // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 800
side = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
Length = 140

# Game Rectangles
ball = Rect((screen_width - side) / 2, (screen_height - side) / 2, side, side)
player = Rect(screen_width - 20, screen_height / 2 - 70, 10, Length)
opponent = Rect(10, screen_height / 2 - 70, 10, Length)
shadow = Rect(screen_width/2, 0, 240, 90)

ball_speed_x = 7
ball_speed_y = -7
player_speed = 0
opponent_speed = 7

bg_color = Color('grey12')
red = Color(255,0,0)
light_gray = (200, 200, 200)
black = Color('black')

Winner_text = ""
Score = 0
White = (255, 255, 255)
Winner_font = pygame.font.SysFont('comicsans', 100)
Win = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = screen_width / 2 + 10
text_y = 10
best_points = 0

# Loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # Animations
    ball_animations()
    player_animation()
    opponent_animations()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, red, ball)
    pygame.draw.rect(screen, black, shadow)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if Score > best_points:
        best_points = Score

    show_score(text_x, text_y)
    high_score(text_x, 5 * text_y)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
