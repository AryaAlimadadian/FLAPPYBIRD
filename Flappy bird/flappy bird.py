import pygame,random,sys
pygame.init()
disp = pygame.display.set_mode((900,600))
yflappy=200
xflappy=80
flag=0
t=0
flappy=[]
flappy1=pygame.image.load("1.png")
flappy1=pygame.transform.scale(flappy1,(50,35))
flappy2=pygame.image.load("2.png")
flappy2=pygame.transform.scale(flappy2,(50,35))
flappy3=pygame.image.load("3.png")
flappy3=pygame.transform.scale(flappy3,(50,35))
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy1)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy2)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
flappy.append(flappy3)
pipup=pygame.image.load("pipup.png")
pipup=pygame.transform.scale(pipup,(60,400))
pipdown=pygame.image.load("pipdown.png")
pipdown=pygame.transform.scale(pipdown,(60,400))
background=pygame.image.load("background.png")
background=pygame.transform.scale(background,(900,600))
background1=pygame.image.load("background1.png")
background1=pygame.transform.scale(background1,(900,600))
startbackground=pygame.image.load("startbackground.jpg")
startbackground=pygame.transform.scale(startbackground,(900,600))
play=pygame.image.load("play.png")
play=pygame.transform.scale(play,(120,70))
font=pygame.font.SysFont("Abril fatface",50)
font1=pygame.font.SysFont("Abril fatface",40)
jump_sound=pygame.mixer.Sound("jump.mp3")
die_sound=pygame.mixer.Sound("die.mp3")
xbackground=0
xbackground1=900
ypipup=[]
ypipdown=[]
xpipup=[]
xpipdown=[]
xpipup1=0
xpipdown1=0
tflappy=0
flaggameover=0
for i in range(1,21):
    xpipup1=xpipup1+200
    xpipdown1=xpipdown1+200
    ypipup.append(random.randint(-250,-150))
    ypipdown.append(random.randint(350,450))
    xpipup.append(xpipup1)
    xpipdown.append(xpipdown1)
gg=True
start=0
while gg:
    while start==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 190<=xm<=290 and 375<=ym<=445:
                    start=1
                    done=False
        disp.blit(startbackground,(0,0))
        disp.blit(play,(190,375))
        pygame.draw.rect(disp,(0, 0, 0),(190,375,120,70),5)
        pygame.display.update()
        pygame.time.Clock().tick(120)
    while not done:
        # events
        for k in pygame.event.get():
            if k.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if k.type==pygame.KEYDOWN:
                if k.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
                if k.key==pygame.K_SPACE:
                    jump_sound.play()
                    flag=1
        # updates
        for i in range(0,len(xpipup)):
            xpipup[i]=xpipup[i]-1
            xpipdown[i]=xpipdown[i]-1
            if (xpipup[i]<=xflappy<=xpipup[i]+60 and yflappy<=ypipup[i]+400) or (xpipup[i]<=xflappy+50<=xpipup[i]+60 and yflappy<=ypipup[i]+400) or (xflappy+50>=xpipup[i] and ypipup[i]<=yflappy<=ypipup[i]+400 and xflappy-xpipup[i]<=60):
                flaggameover=1
                done=True
                die_sound.play()
            if (xpipdown[i]<=xflappy<=xpipdown[i]+60 and yflappy+35>=ypipdown[i]) or (xpipdown[i]<=xflappy+50<=xpipdown[i]+60 and yflappy+35>=ypipdown[i]) or (xflappy+50>=xpipdown[i] and ypipdown[i]<=yflappy<=ypipdown[i]+400 and xflappy-xpipup[i]<=60):
                flaggameover=1
                done=True
                die_sound.play()
        if yflappy<=0 or yflappy>=565:
            flaggameover=1
            done=True
            die_sound.play()
        for i in range(0,len(xpipup)):
            if xpipup[i]==-20:
                xpipup.append(xpipup[len(xpipup)-1]+200)
                xpipdown.append(xpipdown[len(xpipdown)-1]+200)
                ypipup.append(random.randint(-250,-150))
                ypipdown.append(random.randint(400,450))
        xbackground=xbackground-1
        xbackground1=xbackground1-1
        if xbackground==-900:
            xbackground=900
        if xbackground1==-900:
            xbackground1=900
        if flag==1:
            t=t+1
            if t!=25:
                yflappy=yflappy-4
            if t==25:
                flag=0
                t=0
        if flag==0:
            yflappy=yflappy+1.5
        disp.fill((255,255,255))
        disp.blit(background,(xbackground,0))
        disp.blit(background1,(xbackground1,0))
        for i in range(0,len(xpipup)):
            disp.blit(pipdown,(xpipup[i],ypipup[i]))
        for i in range(0,len(xpipdown)):
            disp.blit(pipup,(xpipdown[i],ypipdown[i]))
        disp.blit(flappy[tflappy],(xflappy,yflappy))
        tflappy=tflappy+1
        if tflappy==30:
            tflappy=0
        pygame.display.update()
        pygame.time.Clock().tick(120)
    while flaggameover==1:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 400<=xm<=500 and 385<=ym<=455:
                    pygame.quit()
                    sys.exit()
                if 390<=xm<=510 and 475<=ym<=545:
                    xbackground=0
                    xbackground1=900
                    ypipup=[]
                    ypipdown=[]
                    xpipup=[]
                    xpipdown=[]
                    xpipup1=0
                    xpipdown1=0
                    flaggameover=0
                    for i in range(1,21):
                        xpipup1=xpipup1+200
                        xpipdown1=xpipdown1+200
                        ypipup.append(random.randint(-250,-150))
                        ypipdown.append(random.randint(400,450))
                        xpipup.append(xpipup1)
                        xpipdown.append(xpipdown1)
                    yflappy=200
                    xflappy=80
                    flag=0
                    t=0
                    done=False
        disp.fill((0,0,0))
        gameover_font=font.render("Game Over",True,(255,255,255))
        disp.blit(gameover_font,(350,100))
        pygame.draw.rect(disp,(255, 255, 255),(400,385,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(400,385,100,70),5)
        exit_font=font1.render("Exit",True,(0,0,0))
        disp.blit(exit_font,(422,407))
        pygame.draw.rect(disp,(255, 255, 255),(390,475,120,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(390,475,120,70),5)
        restart_font=font1.render("Restart",True,(0,0,0))
        disp.blit(restart_font,(402,497))
        pygame.display.update()
        pygame.time.Clock().tick(120)
