import pygame as pg
import sys,time,random

pg.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
win=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
paddle=pg.Rect(340,770,120,20)
clock=pg.time.Clock()
# writing codes of font
font = pg.font.Font('arial.ttf', 35)
scoreText = font.render('Score: 0', True, (255,200,0), (0,0,0))
scoreTextRect = scoreText.get_rect()
scoreTextRect.center=(SCREEN_WIDTH//1.11,SCREEN_HEIGHT//19.5)


font2 = pg.font.Font('arial.ttf', 55)
gameOverText = font2.render('GAME OVER', True, (255,0,255), (0,0,0))
gameOverTextRect = gameOverText.get_rect()
gameOverTextRect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)


font3 = pg.font.Font('arial.ttf', 40)
welcomeText = font3.render('WELCOME TO THE PADDLE BALL', True, (200,200,255), (0,0,0))
welcomeTextRect = welcomeText.get_rect()
welcomeTextRect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
#speed of the ball and paddle
GAME_RUNNING=True
BOX_SPEED=10
TARGET_FPS=60
MAX_BALL_SPEED=10
MIN_BALL_SPEED=5
BALL_X_SPEED=0
BALL_Y_SPEED=0
GAME_STARTED=False
BALL_X=paddle.x+60
BALL_Y=paddle.y-15
SCORE=0
dt=0
#adding music
old=time.time()
import pygame
file = 'Monkeys-Spinning-Monkeys.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
#pygame.mixer.music.load('mixki-arcade-game-over-3068.wav')
#pygame.mixer.music.play()
pygame.mixer.music.play()
#pygame.mixer.music.play==False


#updating score
def updateScore():
    global SCORE,scoreText
    SCORE+=3
    scoreText = font.render(f'Score: {SCORE}', True, (255,0,0), (0,0,0))

#checking collision
def checkCollision():
    global SCREEN_WIDTH,paddle,BALL_X,BALL_Y,BALL_X_SPEED,BALL_Y_SPEED,GAME_STARTED
    if paddle.x<0:
        paddle.x=0
    if paddle.x+120>SCREEN_WIDTH:
        paddle.x=SCREEN_WIDTH-120

    if BALL_X-13<=0 or BALL_X+13>=SCREEN_WIDTH:
        BALL_X_SPEED=-BALL_X_SPEED
    if BALL_Y-13<=0:
        BALL_Y_SPEED=-BALL_Y_SPEED

    if BALL_Y+13>=paddle.y-5 and GAME_STARTED==True and BALL_X>paddle.x and BALL_X<paddle.x+120:
        BALL_Y-=15
        BALL_Y_SPEED=-BALL_Y_SPEED
        updateScore()
    elif BALL_Y+13>paddle.y:
        gameOver()
        pygame.mixer.music.play==False

def gameOver():
    global GAME_RUNNING
    GAME_RUNNING=False
    
while True:
    new=time.time()
    dt=new-old
    old=new
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                GAME_STARTED=True
                BALL_Y-=10
                sign=random.randint(0,1)
                BALL_Y_SPEED=-random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
                BALL_X_SPEED=random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
                if sign==0:
                    BALL_X_SPEED=-BALL_X_SPEED
    # movement of the paddle
    if GAME_RUNNING==True:
        checkCollision()
        key=pg.key.get_pressed()
        if key[pg.K_LEFT]:
            paddle.x-=BOX_SPEED*dt*TARGET_FPS
            if GAME_STARTED==False:
                BALL_X=paddle.x+60
        elif key[pg.K_RIGHT]:
            paddle.x+=BOX_SPEED*dt*TARGET_FPS
            if GAME_STARTED==False:
                BALL_X=paddle.x+60

        
#giving colour to the paddle and ball and printing text on the screen
        win.fill("black")
        pg.draw.rect(win,"gray",paddle)
        if GAME_STARTED==False:
            win.blit(welcomeText,welcomeTextRect)

            pg.draw.circle(win,"orange",(BALL_X,BALL_Y),15)
        else:
            BALL_X+=BALL_X_SPEED*dt*TARGET_FPS
            BALL_Y+=BALL_Y_SPEED*dt*TARGET_FPS
            pg.draw.circle(win,"green",(BALL_X,BALL_Y),15)
    else:
        win.blit(gameOverText,gameOverTextRect)

        pg.draw.circle(win,"red",(BALL_X,BALL_Y),15)

    
    win.blit(scoreText,scoreTextRect)
    pg.display.update()
    
    clock.tick(60)        


