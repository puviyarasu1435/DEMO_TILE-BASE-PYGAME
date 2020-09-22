#---------------------------------------------------------------------------------------------------------------#
#                                          Name     : main.py                                                   #
#                                          Purpose  : game                                                      #
#                                          Author   : puviyarasu.p                                              #
#                                          Created  : 28-05-2020                                                #
#---------------------------------------------------------------------------------------------------------------#
import pygame, sys,os #images impoting work so etha sys add panniruku
from pygame.locals import * #local events
import gamemap as gm
import images as img
#---------------------------------------------------------------------------------------------------------------
pygame.init()#pygame starting
clock = pygame.time.Clock()#loop speed
pygame.display.set_caption('GAME')
mediam = pygame.font.Font("ALGER.TTF", 20)
large = pygame.font.Font("ALGER.TTF", 30)
winsize = (1000,600)#window size
screen = pygame.display.set_mode(winsize,0,32) #normal window
display = pygame.Surface((winsize)) #pygame surface
score,jumptime,n,gravity = 0,0,0,0
count,coine=0,0

#-----------------------------------------------------------------------------------------------------------------
def obj_test(rect,tiles):# this def function is compar the two rect box collage
    obj_block = []
    for tile in tiles:
        if rect.colliderect(tile):
            obj_block.append(tile)
    return obj_block

def chang_con(obj):# this def is used coine obj taken
    x=(obj.x//15)
    y=(obj.y//15)
    gm.map[y][x]='0'

def chang_misty(obj):# tis def is box obj taken
    x=(obj.x//15)
    y=(obj.y//15)
    gm.map[y][x]='0'
    gm.map[y][x+1]='0'
    gm.map[y-1][x]='0'
    gm.map[y-1][x+1]='0'
def work(box,axies,obj_list,box_con,box_misty,block_list,box_door,end_list):# work the obj
    bottom=False
    global score,coine
    box.x += axies[0]
    obj_block = obj_test(box,obj_list)
    for obj in obj_block:
        if axies[0] > 0:
            box.right = obj.left
        elif axies[0] < 0:
            box.left = obj.right
    box.y += axies[1]
    obj_block = obj_test(box,obj_list)
    for obj in obj_block:
        if axies[1] > 0:
            box.bottom = obj.top
            bottom= True
        elif axies[1] < 0:
            box.top = obj.bottom

    obj_win = obj_test(box,box_con)
    for obj in obj_win:
        if obj not in block_list:
            block_list.append(obj)
            score+=10
            coine+=1
            chang_con(obj)
    obj_win = obj_test(box,box_misty)
    for obj in obj_win:
        if obj not in block_list:
            block_list.append(obj)
            score+=100
            chang_misty(obj)
    obj_door = obj_test(box,box_door)
    for obj in obj_door:
        if coine>=1:
            import win
    obj_door = obj_test(box,end_list)
    for obj in obj_door:
        over()
    return box,bottom

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def loop():
    player_rect = pygame.Rect(100,100,5,13)
    background = pygame.image.load(os.path.join('images','sea.png'))
    time_mcro=0
    right = False#right
    left = False#left
    global score,jumptime,n,gravity
    score=0
    box_misty,block_list,box_con,box_door,end_list=[],[],[],[],[]
    second=120
    global count,coine
    while True: # game loop
        #pygame.time.delay(c)
        display.blit(background,(0,0)) # clear screen by filling it with blue
        object_list = []#list of object
        y = 0
        for layer in gm.map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(img.inner,(x*15,y*15))
                if tile == '2':
                    display.blit(img.outline,(x*15,y*15))
                if tile == 'b1':
                    display.blit(img.box1,(x*15,y*15))
                elif tile == 'b2':
                    display.blit(img.box2,(x*15,y*15))
                elif tile == 'b3':
                    box_misty.append(pygame.Rect(x*15,y*15,15,15))# store the box obj file
                    display.blit(img.box3,(x*15,y*15))
                elif tile == 'b4':
                    display.blit(img.box4,(x*15,y*15))
                elif tile == 'e':
                    end_list.append(pygame.Rect(x*15,y*15,15,15))
                elif tile == 'con':
                    if n==6:
                        n=0
                    display.blit(img.con_list[n],(x*15,y*15))
                    box_con.append(pygame.Rect(x*15,y*15,15,15))# stored the coine obj file
                    n+=1
                elif tile == 'd1':
                    display.blit(img.door[0],(x*15,y*15))
                elif tile == 'd2':
                    display.blit(img.door[1],(x*15,y*15))
                elif tile == 'd3':
                    display.blit(img.door[2],(x*15,y*15))
                elif tile == 'd4':
                    display.blit(img.door[3],(x*15,y*15))
                elif tile == 'd5':
                    display.blit(img.door[4],(x*15,y*15))
                elif tile == 'd6':
                    display.blit(img.door[5],(x*15,y*15))
                elif tile == 'd7':
                    display.blit(img.door[6],(x*15,y*15))
                elif tile == 'd8':
                    display.blit(img.door[7],(x*15,y*15))
                elif tile == 'd9':
                    display.blit(img.door[8],(x*15,y*15))
                elif tile == 'd10':
                    display.blit(img.door[9],(x*15,y*15))
                elif tile == 'd11':
                    display.blit(img.door[10],(x*15,y*15))
                elif tile == 'd12':
                    display.blit(img.door[11],(x*15,y*15))
                elif tile == 'd13':
                    display.blit(img.door[12],(x*15,y*15))
                elif tile == 'd14':
                    display.blit(img.door[13],(x*15,y*15))
                elif tile == 'd15':
                    display.blit(img.door[14],(x*15,y*15))
                elif tile == 'd16':
                    display.blit(img.door[15],(x*15,y*15))
                elif tile == 'd17':
                    display.blit(img.door[16],(x*15,y*15))
                elif tile == 'd18':
                    box_door.append(pygame.Rect(x*15,y*15,15,15))# stored the coine obj file
                    display.blit(img.door[17],(x*15,y*15))
                elif tile == 'd19':
                    box_door.append(pygame.Rect(x*15,y*15,15,15))# stored the coine obj file
                    display.blit(img.door[18],(x*15,y*15))
                elif tile == 'd20':
                    display.blit(img.door[19],(x*15,y*15))
                elif tile != '0':
                    object_list.append(pygame.Rect(x*15,y*15,15,15))
                x += 1
            y += 1

        #---------------------------------------------------------------------------------------------------------------
        axies = [0,0]# player axies (x,y)
        if right == True:
            axies[0] += 3# x axies increment
        if left == True:
            axies[0] -= 3 # x axies decrement
        axies[1] += gravity
        gravity += 0.20
        player_rect,bottom =work(player_rect,axies,object_list,box_con,box_misty,block_list,box_door,end_list)# call def obj function
        if bottom == True:
            jumptime = 0
            gravity = 0
        else:
            jumptime += 1

        display.blit(img.player,(player_rect.x,player_rect.y))# print the player

        box_con.pop()
       #-----------------------------------------------------------------------------------------------------------------
       for event in pygame.event.pump(): # event loop
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    right = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_UP:
                    if jumptime < 6:
                        gravity = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    right = False
                if event.key == K_LEFT:
                    left = False
        scorebord = mediam.render("score : "+str(score)+"    coine :"+str(coine), True, (250,250,250))
        display.blit(scorebord,(20,10))
        scorebord = mediam.render("Time : "+str(second), True, (250,250,250))
        display.blit(scorebord,(800,10))
        if count>=60:
            if second<=0:
                import over
            else:
                second-=1
            count=0
        else:
            count+=2
        #------------------------------------------------------------------------------------------------------------------
        screen.blit(pygame.transform.scale(display,winsize),(0,0))
        pygame.display.update()
        clock.tick(10000)

def over():
    while True:
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            sys.exit()
        display.blit(img.win_back,(0,0))
        scorebord = large.render("GAME OVER!", True, (250,250,250))
        aging = large.render("retry press space", True, (250,250,250))
        display.blit(scorebord,(400,200))
        display.blit(aging,(350,400))
        screen.blit(pygame.transform.scale(display,winsize),(0,0))
        pygame.display.update()
        clock.tick(70)
#=======================================================================================================================






loop()
