import pygame
import os
from random import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
# 배경화면
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 똥, 캐릭터
poop = pygame.image.load(os.path.join(current_path, "poop.png"))
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = randint(0,screen_width - poop_width)
poop_y_pos = 0

character = pygame.image.load(os.path.join(current_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

poop_speed = 0.7

character_speed = 1
to_x = 0

game_font = pygame.font.Font(None, 40)
score = 0

running = True # 게임이 진행 중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    poop_y_pos += poop_speed * dt 
    if poop_y_pos > screen_height:
        poop_x_pos = randint(0,screen_width - poop_width)
        poop_y_pos = - poop_height
        score += 100

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    if character_rect.colliderect(poop_rect):
        print("충돌했어요")
        running = False


    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(poop, (poop_x_pos,poop_y_pos))
    screen.blit(character, (character_x_pos,character_y_pos))
    
    total_score = game_font.render("SCORE : " + str(score), True, (255,255,255))
    screen.blit(total_score, (0,0))

    pygame.display.update() # 게임화면을 다시 그리기!! 중요!

# pygame 종료
pygame.time.delay(1000)

pygame.quit()