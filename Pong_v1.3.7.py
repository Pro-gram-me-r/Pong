import pygame
import sys
from pygame import Rect, Color, mixer
from random import choice


def ball_animations():
    global ball_speed_x, ball_speed_y, Score, text_y, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= gap or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        ball_restart()
        Score -= 5

    if ball.left <= 0:
        ball_restart()
        opponent_score -= 5

    if ball.colliderect(player):
        ball_speed_x *= -1
        Score += 10

    if ball.colliderect(opponent):
        ball_speed_x *= -1
        opponent_score += 10


def show_score(x, y):
    score = font.render('Score: ' + str(Score), True, White)
    screen.blit(score, (x, y))


def high_score(x, y):
    highest_score = font.render('High Score: ' + str(best_points), True, White)
    screen.blit(highest_score, (x, y))


def opponent_scoring(x, y):
    opponent_score_font = font.render('Opponent Score: ' + str(opponent_score), True, White)
    screen.blit(opponent_score_font, (x, y))


def player_animation():
    player.y += player_speed
    if player.top <= gap:
        player.top = gap
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animations():
    if opponent.top + Length / 4 < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom - Length / 4 > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= gap:
        opponent.top = gap
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= giving_choice
    ball_speed_y *= giving_choice


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
gap = 90

# Game Rectangles
ball = Rect((screen_width - side) / 2, (screen_height - side + gap) / 2, side, side)
player = Rect(screen_width - 20, screen_height / 2 - 70, 10, Length)
opponent = Rect(10, screen_height / 2 - 70, 10, Length)
shadow = Rect(0, 0, screen_width, gap)

giving_choice = choice((1, -1))
ball_speed_x = 7 * giving_choice
ball_speed_y = 7 * giving_choice
player_speed = 0
opponent_speed = 6

bg_color = Color('grey12')
red = Color(255, 0, 0)
light_gray = (200, 200, 200)
black = Color('black')

song_choices = ["Blueballed.mp3", "Fading.mp3", "Headache.mp3", 'Nerves.mp3', 'Playtime.mp3', 'Release.mp3',
                'Unleashed.mp3', "Last Chance.mp3", 'Genocide.mp3']
song_going_to_be_played = choice(song_choices)
mixer.music.load(song_going_to_be_played)
mixer.music.play(-1)

Winner_text = ""
Score = 0
White = (255, 255, 255)
Winner_font = pygame.font.SysFont('comicsans', 100)
Win = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10
best_points = 0
opponent_score = 0

# Loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 6
            if event.key == pygame.K_UP:
                player_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 6
            if event.key == pygame.K_UP:
                player_speed += 6

    # Animations
    ball_animations()
    player_animation()
    opponent_animations()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, red, ball)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.rect(screen, black, shadow)

    if Score > best_points:
        best_points = Score

    show_score(text_x, text_y)
    high_score(text_x, 5 * text_y)
    opponent_scoring(screen_width / 2, text_y)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
