import datetime
import pygame,sys
from pygame.locals import*
from pygame import mixer
import time
import os
import subprocess
import webbrowser


mixer.init()
mixer.music.load("click.wav")

running = True
now = datetime.datetime.now()

#ICONS
calendicon= pygame.image.load('calendar.png')
homepage= pygame.image.load('homepage.png')
comicon= pygame.image.load('com.png')
inficon= pygame.image.load('inf.png')
enticon= pygame.image.load('ent.png')
homebttn=pygame.image.load('AHome.png')
gamesicon=pygame.image.load('games.png')
musicicon= pygame.image.load('music.png')
youtubeicon=pygame.image.load('youtube.png')
movieicon=pygame.image.load('movie.png')
shopicon=pygame.image.load('shop.png')
emailicon=pygame.image.load('email.png')
foodicon=pygame.image.load('food.png')
webicon=pygame.image.load('web.png')

#SCREENS
maintab = pygame.image.load('maintab.png')
Homescrn = pygame.image.load('AHomescrn.png')
safety=pygame.image.load('safety.png')
entpage=pygame.image.load('entpage.png')
infpage=pygame.image.load('infpage.png')
compage=pygame.image.load('compage.png')
flightinfo=pygame.image.load('flightinfo.png')
flightsafety=pygame.image.load('flightsafety.png')
flightdetails=pygame.image.load('flightdetails.png')
food1=pygame.image.load('food1.png')
food2=pygame.image.load('food2.png')
food3=pygame.image.load('food3.png')
store1=pygame.image.load('store1.png')
store2=pygame.image.load('store2.png')
store3=pygame.image.load('store3.png')
musicbg=pygame.image.load('musicbg.png')
emailbg=pygame.image.load('emailbg.png')
webbg=pygame.image.load('webbg.png')

#MailStuff
yahoo=pygame.image.load('yahoo.png')
gmail=pygame.image.load('gmail.png')

arrow=pygame.image.load("Arrow.png")

x=100
y=15
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)
w = 1024
h = 768
screen = pygame.display.set_mode([w, h])
location="home"    
x = y = 0
pygame.init()

black = (0,0,0)
WHITE=(255,255,255)
blue=(0,0,255)

pygame.init()
font = pygame.font.SysFont("Monospace", 40)
font2 = pygame.font.SysFont('Monospace', 50)

def home(location):
    running = True
    while running and location=='home':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        

        maintab = pygame.image.load('maintab.png')
        homepage= pygame.image.load('homepage.png')
        screen.blit(maintab,(0,0))
        Homebttn=screen.blit(homebttn,(493,640))
        homepage=screen.blit(homepage,(115,88))
        pygame.display.flip()
        #pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print "Click: ",X
                print X[0],X[1]
                
                if homepage.collidepoint(X[0],X[1]):
                    
                   
                    location = 'home1'
                    home1(location)

def home1(location):
    running = True
    while running and location=='home1':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        #For time display
        dt=str(datetime.datetime.today())
        time = dt[11:30]
        hr = dt[11:13]
        min = dt[14:16]
        fontimg = font.render(hr,3,black)
        fontimg1 = font.render(min,3,black)
        fontimg2 = font.render(":",3,black)
        screen.blit(fontimg, (782,100))
        screen.blit(fontimg1, (845,100))
        screen.blit(fontimg2, (827,96))
        pygame.time.delay(0)
        pygame.display.update()
        
        screen.blit(maintab,(0,0))
        screen.blit(Homescrn,(115,88))
        
        #Previous ones


        Information=screen.blit(inficon,(165,271))
        Communication=screen.blit(comicon,(415,270))
        Entertainment=screen.blit(enticon,(675,270))
        
        Homebttn=screen.blit(homebttn,(493,640))
        pygame.display.flip()
        #event = pygame.event.poll()

              

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                X= pygame.mouse.get_pos()
                print "Click: ",X
                print X[0],X[1]
                
                                    
                    
                if Information.collidepoint(X[0],X[1]):
                    
                    location = 'information'
                    information(location)

                    
                elif Entertainment.collidepoint(X[0],X[1]):
                    
                    location = 'entertainment'
                    entertainment(location)
                    
                    
                elif Communication.collidepoint(X[0],X[1]):
                    
                    location = 'communication'
                    communication(location)


                elif Homebttn.collidepoint(X[0],X[1]):
                    location='home1'
                    home1(location)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def entertainment(location):
    
    running = True
    while running and location=='entertainment':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(maintab,(0,0))
        screen.blit(entpage,(115,88))
        Homebttn=screen.blit(homebttn,(493,640))

        games=screen.blit(gamesicon,(513,88))
        music=screen.blit(musicicon,(115,88))
        movie=screen.blit(movieicon,(513,338))
        youtube=screen.blit(youtubeicon,(115,338))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                X= pygame.mouse.get_pos()
                print "Click: ",X
                print X[0],X[1]
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home1'
                    home1(location)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 # GAMES LOOP   # GAMES LOOP   # GAMES LOOP   # GAMES LOOP   # GAMES LOOP

                elif games.collidepoint(X[0],X[1]):

                    location='games'

                    running = True
                    
                    pygame.display.update()
                    screen.blit(maintab,(0,0))
                    screen.blit(musicbg,(115,88))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    subprocess.call("TicTacToe.py",shell=True)

                    while running and location=='games':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MUSIC LOOP   # MUSIC LOOP   # MUSIC LOOP   # MUSIC LOOP   # MUSIC LOOP

                elif music.collidepoint(X[0],X[1]):

                    location='music'

                    running = True
                    
                    pygame.display.update()
                    screen.blit(maintab,(0,0))
                    screen.blit(musicbg,(115,88))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    subprocess.call("music_1.py",shell=True)

                    while running and location=='music':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# MOVIE LOOP   # MOVIE LOOP   # MOVIE LOOP   # MOVIE LOOP   # MOVIE LOOP

                elif movie.collidepoint(X[0],X[1]):
                    location='movie'

                    running = True
                    
                    pygame.display.update()
                    screen.blit(maintab,(0,0))
                    screen.blit(musicbg,(115,88))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    subprocess.call("movie.py",shell=True)

                    while running and location=='movie':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#YOUTUBE LOOP    #YOUTUBE LOOP    #YOUTUBE LOOP    #YOUTUBE LOOP    #YOUTUBE 
                    
                elif youtube.collidepoint(X[0],X[1]):

                    location='youtube'

                    running = True
                    
                    pygame.display.update()
                    screen.blit(maintab,(0,0))
                    screen.blit(musicbg,(115,88))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    subprocess.call("youtube.py",shell=True)

                    while running and location=='youtube':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        

def information(location):
    
    running = True
    while running and location=='information':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(maintab,(0,0))
        screen.blit(entpage,(115,88))
        Homebttn=screen.blit(homebttn,(493,640))

        fsafety=screen.blit(safety,(115,88))
        flightinformation=screen.blit(flightinfo,(513,88))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print "Click: ",X
                print X[0],X[1]
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home1'
                    home1(location)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                elif fsafety.collidepoint(X[0],X[1]):
                    location='safety'

                    running = True
                    
                    while running and location=='safety':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
                        screen.blit(maintab,(0,0))
                        screen.blit(flightsafety,(115,88))
                        Homebttn=screen.blit(homebttn,(493,640))

                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                    

                elif flightinformation.collidepoint(X[0],X[1]):
                    location='flightinfo'

                    running = True
                    
                    while running and location=='flightinfo':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
                        screen.blit(maintab,(0,0))
                        screen.blit(flightdetails,(114,117))
                        Homebttn=screen.blit(homebttn,(493,640))

                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                    
def communication(location):
    running = True
    

    while running and location=='communication':
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.blit(maintab,(0,0))
        screen.blit(compage,(115,88))
        Homebttn=screen.blit(homebttn,(493,640))

        shop=screen.blit(shopicon,(113,88))
        email=screen.blit(emailicon,(513,88))
        food=screen.blit(foodicon,(113,338))
        web=screen.blit(webicon,(513,338))
    

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                #mixer.music.play(0)
                X= pygame.mouse.get_pos()
                print "Click: ",X
                print X[0],X[1]
                
                if Homebttn.collidepoint(X[0],X[1]):
                    location='home1'
                    home1(location)


                elif shop.collidepoint(X[0],X[1]):
                    location='store'

                    running = True
                    
                    while running and location=='store':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
                        screen.blit(maintab,(0,0))
                        foodno1=screen.blit(store1,(115,88))
                        Homebttn=screen.blit(homebttn,(493,640))

                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

                                elif foodno1.collidepoint(X[0],X[1]):
                                    location='store'

                                    running = True
                                    while running and location=='store':
                                        for event in pygame.event.get():
                                            if event.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                                        pygame.display.update()

                                        screen.blit(maintab,(0,0))
                                        foodno2=screen.blit(store2,(115,88))
                                        Homebttn=screen.blit(homebttn,(493,640))
                                        pygame.display.flip()
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                running=False
                                                pygame.quit()
                                                quit()
                                                sys.exit()
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                # Set the x, y postions of the mouse click
                                                #mixer.music.play(0)
                                                X= pygame.mouse.get_pos()
                                                print "Click: ",X
                                                print X[0],X[1]
                
                                                if Homebttn.collidepoint(X[0],X[1]):
                                                    location='home1'
                                                    home1(location)


                                                elif foodno2.collidepoint(X[0],X[1]):
                                                    location='store'


                                                    running = True
                                                    while running and location=='store':
                                                        for event in pygame.event.get():
                                                            if event.type==QUIT:
                                                                pygame.quit()
                                                                sys.exit()
                                                        pygame.display.update()

                                                        screen.blit(maintab,(0,0))
                                                        screen.blit(store3,(115,88))
                                                        Homebttn=screen.blit(homebttn,(493,640))
                                                        pygame.display.flip()
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.QUIT:
                                                                running=False
                                                                pygame.quit()
                                                                quit()
                                                                sys.exit()
                                                            if event.type == pygame.MOUSEBUTTONDOWN:

                                                                # Set the x, y postions of the mouse click
                                                                #mixer.music.play(0)
                                                                X= pygame.mouse.get_pos()
                                                                print "Click: ",X
                                                                print X[0],X[1]
                
                                                                if Homebttn.collidepoint(X[0],X[1]):
                                                                    location='home1'
                                                                    home1(location)





                elif email.collidepoint(X[0],X[1]):
                    location='email'

                    import webbrowser
                    yahoo=pygame.image.load('yahoo.png')
                    gmail=pygame.image.load('gmail.png')
                    running = True
                    Loadscr=screen.blit(maintab,(0,0))
                    Homebttn=screen.blit(homebttn,(493,640))
                    screen.blit(emailbg,(115,88))
                    pygame.display.flip()
                    running = True
                    Yahoo=screen.blit(yahoo,(500,200))
                    Gmail=screen.blit(gmail,(500,400))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    while running and location=='email':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

                                elif Yahoo.collidepoint(X[0],X[1]):
                                    url="https://mail.yahoo.com/";
                                    webbrowser.open(url,new=2);


                                elif Gmail.collidepoint(X[0],X[1]):
                                    url="https://www.google.com/gmail/";
                                    webbrowser.open(url,new=2);



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                elif food.collidepoint(X[0],X[1]):
                    location='food'

                    running = True
                    
                    while running and location=='food':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
                        screen.blit(maintab,(0,0))
                        foodno1=screen.blit(food1,(115,88))
                        Homebttn=screen.blit(homebttn,(493,640))

                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

                                elif foodno1.collidepoint(X[0],X[1]):
                                    location='food'

                                    running = True
                                    while running and location=='food':
                                        for event in pygame.event.get():
                                            if event.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                                        pygame.display.update()

                                        screen.blit(maintab,(0,0))
                                        foodno2=screen.blit(food2,(115,88))
                                        Homebttn=screen.blit(homebttn,(493,640))
                                        pygame.display.flip()
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                running=False
                                                pygame.quit()
                                                quit()
                                                sys.exit()
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                # Set the x, y postions of the mouse click
                                                #mixer.music.play(0)
                                                X= pygame.mouse.get_pos()
                                                print "Click: ",X
                                                print X[0],X[1]
                
                                                if Homebttn.collidepoint(X[0],X[1]):
                                                    location='home1'
                                                    home1(location)


                                                elif foodno2.collidepoint(X[0],X[1]):
                                                    location='food'


                                                    running = True
                                                    while running and location=='food':
                                                        for event in pygame.event.get():
                                                            if event.type==QUIT:
                                                                pygame.quit()
                                                                sys.exit()
                                                        pygame.display.update()

                                                        screen.blit(maintab,(0,0))
                                                        screen.blit(food3,(115,88))
                                                        Homebttn=screen.blit(homebttn,(493,640))
                                                        pygame.display.flip()
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.QUIT:
                                                                running=False
                                                                pygame.quit()
                                                                quit()
                                                                sys.exit()
                                                            if event.type == pygame.MOUSEBUTTONDOWN:

                                                                # Set the x, y postions of the mouse click
                                                                #mixer.music.play(0)
                                                                X= pygame.mouse.get_pos()
                                                                print "Click: ",X
                                                                print X[0],X[1]
                
                                                                if Homebttn.collidepoint(X[0],X[1]):
                                                                    location='home1'
                                                                    home1(location)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



                elif web.collidepoint(X[0],X[1]):
                    location='web'

                    running = True
                    
                    pygame.display.update()
                    screen.blit(maintab,(0,0))
                    screen.blit(webbg,(115,88))
                    Homebttn=screen.blit(homebttn,(493,640))
                    pygame.display.flip()
                    import webbrowser
                    new=2;
                    url="http:\\google.com";
                    webbrowser.open(url,new=new);

                    while running and location=='web':
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                pygame.quit()
                                sys.exit()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                pygame.quit()
                                quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                X= pygame.mouse.get_pos()
                                print "Click: ",X
                                print X[0],X[1]
                
                                if Homebttn.collidepoint(X[0],X[1]):
                                    location='home1'
                                    home1(location)

                    

home(location)


