import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Taemin Game") # 게임 이름

# 배경 이미지 불러오기 # 주소를 불러오고 나서 역슬래쉬는 역슬래쉬 두개 또는 / 하나로 바꿔야 한다.
background = pygame.image.load("C:\\Users\\Taemin\\Desktop\\Python Workspace\\Practical\\pygame_basic\\background.png")

# 이벤트 루프가 항상 실행되어 있어야지 꺼지지 않는다
running = True # 게임이 진행 중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님

    # screen.fill((170, 170, 255))
    screen.blit(background, (0, 0)) # 배경 그리기 # 어떤 걸 어디에 배치하는 지?

    pygame.display.update() # 게임화면을 다시 그리기!! 중요!


# pygame 종료
pygame.quit()