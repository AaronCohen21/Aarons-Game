from template import *

running = True

sound = Sound(1202,652)
exitButton = Button(LIGHT_RED,111,42,200,66,'Exit')



class Wall():
    def __init__(self,x,y,width,height,hasPlayer,playerOnRight,playerOnLeft):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hasPlayer = hasPlayer
        self.playerOnRight = playerOnRight
        self.playerOnLeft = playerOnLeft
        
    def draw(self):
        pygame.draw.rect(screen, DARK_GREY, (self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
        
        #this is where it is going to test what side of the player is touching the platform
            
        #top of the platform and bottom of the player
        if (player.x+(player.width/2) > self.x-(self.width/2) and player.x-(player.width/2) < self.x+(self.width/2) and player.y+(player.height//2) == self.y-(self.height//2)):
            if player.jumping == False:
                player.grounded = True
                self.hasPlayer = True
        else:
            self.hasPlayer = False
                    
        #bottom of the platform and top of the player
        if (player.x+(player.width/2) > self.x-(self.width/2) and player.x-(player.width/2) < self.x+(self.width/2) and player.y-(player.height//2) == self.y+(self.height//2)):
            if player.jumping == False:
                self.hasPlayer = True
            else:
                player.jumping = False
                self.hasPlayer = False
                
        #right of the wall and left of the player
        if (player.x-(player.width//2) == self.x+(self.width//2) and player.y+(player.height//2) > self.y-(self.height//2) and player.y-(player.height//2) < self.y+(self.height//2)):
            player.canMoveLeft = False
            self.playerOnRight = True
        else:
            self.playerOnRight = False
            
        #left of the wall and right of the player
        if (player.x+(player.width//2) == self.x-(self.width//2) and player.y+(player.height//2) > self.y-(self.height//2) and player.y-(player.height//2) < self.y+(self.height//2)):
            player.canMoveRight = False
            self.playerOnLeft = True
        else:
            self.playerOnLeft = False

class DeathPlane():
    def __init__(self,x,y,width,height,triggered,lenient):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.triggered = triggered
        self.lenient = lenient
        
    def draw(self):
        pygame.draw.rect(screen, LIGHT_RED, (self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
        
        if self.lenient and (player.x+(player.width/2)-(player.width/4) > self.x-(self.width/2) and player.x-(player.width/2)+(player.width/4) < self.x+(self.width/2) and player.y+(player.height//2)-(player.height/4) > self.y-(self.height//2) and player.y-(player.height//2)+(player.height/4) < self.y+(self.height//2)):
            self.triggered = True
        elif (player.x+(player.width/2) > self.x-(self.width/2) and player.x-(player.width/2) < self.x+(self.width/2) and player.y+(player.height//2) > self.y-(self.height//2) and player.y-(player.height//2) < self.y+(self.height//2)):
            self.triggered = True

class EndZone():
    def __init__(self,x,y,width,height,active):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = active
        
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
        
        #if the player is in the end zone mark the level as cleared and return to levels screen
        if (player.x+(player.width/2) > self.x-(self.width/2) and player.x-(player.width/2) < self.x+(self.width/2) and player.y+(player.height//2) > self.y-(self.height//2) and player.y-(player.height//2) < self.y+(self.height//2) and player.grounded):
            changeCleared = open('storedInformation/twoCleared.txt','w')
            changeCleared.write('cleared')
            changeCleared.close()
            self.active = True
        
class Player():
    def __init__(self,x,y,width,height,grounded,jumping,jumpHeight,canAddHeight,addedHeight,canMoveLeft,canMoveRight):
        self.x = x
        self.y= y
        self.width = width
        self.height = height
        self.grounded = grounded
        self.jumping = jumping
        self.jumpHeight = jumpHeight
        self.canAddHeight = canAddHeight
        self.addedHeight = addedHeight
        self.canMoveLeft = canMoveLeft
        self.canMoveRight = canMoveRight
        
    def draw(self):
        pygame.draw.rect(screen,PLAYER_GREY,(self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
        #jump
        if self.grounded:
            self.jumping = False
            self.jumpHeight = 15
            self.canAddHeight = True
            
        if self.jumping:
            if self.jumpHeight > 0:
                #if the player has not landed continue to give height
                if self.grounded == False:
                    self.y -= 4
                    self.jumpHeight-=1
            else:
                #end of the jump
                self.jumping = False
                self.grounded = False
                self.canAddHeight = True
                self.jumpHeight = 15
        
        #make sure to test if all the instantiated platforms do not have the player on them
        if flashingPlatform.hasPlayer == False and startingWall.hasPlayer == False and secondWall.hasPlayer == False and startingPlatform.hasPlayer == False and secondPlatform.hasPlayer == False:
            self.grounded = False
            
        #make sure to test if all the instantiated walls do not have the player on them and let the player move left
        if startingWall.playerOnRight == False and secondWall.playerOnRight == False:
            self.canMoveLeft = True
            
        #make sure to test if all of the instantiated walls do not have the player on them and let the player move right
        if startingWall.playerOnLeft == False and secondWall.playerOnLeft == False:
            self.canMoveRight = True
            
class Platform():
    def __init__(self,x,y,width,height,hasPlayer,color=DARK_GREY):
        self.x = x
        self.y= y
        self.width = width
        self.height = height
        self.hasPlayer = hasPlayer
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
    
        #makes the player stop falling and able to jump if it is on a platform
        if (player.x+(player.width/2) > self.x-(self.width/2) and player.x-(player.width/2) < self.x+(self.width/2) and player.y+(player.height//2) == self.y-(self.height//2)):
            if player.jumping == False:
                player.grounded = True
                self.hasPlayer = True
        else:
            self.hasPlayer = False
    
player = Player(195,552-100,100,100,False,False,15,True,0,True,True)

startingPlatform = Platform(0+(450/2),550,450,25,False)
secondPlatform = Platform(986-50,425+25,250,25,False)

flashingPlatform = Platform(450+(315.5/2),550,315.5,25,False,DARKER_GREY)
flashingPlane = DeathPlane(753,500-(250/2)+20,25,250+40,False,False)

endzone = EndZone(secondPlatform.x,secondPlatform.y-50,250,100,False)
deathPlane = DeathPlane(WINDOW_WIDTH/2,702,WINDOW_WIDTH+1000,200,False,True)

startingWall = Wall(753,250/2,25,250,False,False,False)
secondWall = Wall(753,550,25,25,False,False,False)


flashTimer = 0

while running:
    #Keep the loop running at the correct speed
    clock.tick(FPS)
    
    #change the color of the flashing platform and move it along with the deathplane
    if flashTimer < 180:
        flashTimer += 1
        
    else:
        flashTimer = 0
        
    if flashTimer == 120:
        flashingPlatform.y -= 10000
        flashingPlane.y -= 10000
        
    elif flashTimer == 90:
        flashingPlatform.color = BLUE
        
    elif flashTimer == 100:
        readVolume = open('storedInformation/Volume.txt','r')
        volume = readVolume.read()
                #play the sound if the volume is unmuted
        if volume == "muted":    
            pygame.mixer.music.load('resources/sounds/lightBeep.wav')
            pygame.mixer.music.play()
        readVolume.close()
        
    elif flashTimer == 0:
        flashingPlatform.color = DARKER_GREY
        flashingPlatform.y += 10000
        flashingPlane.y += 10000
    
    #input and events
    for event in pygame.event.get():
        
        #set the mouse position in a tuple
        mousePos = pygame.mouse.get_pos()
        
        #Play a click noise if you click the mouse and the volume is not muted
        if event.type == pygame.MOUSEBUTTONDOWN:
            readVolume = open('storedInformation/volume.txt')
            volume = readVolume.read()
            if volume == "muted":
                #test if the mouse is over top of a button
                if exitButton.isOver(mousePos):
                    pygame.mixer.music.load('resources/sounds/click.wav')
                    pygame.mixer.music.play()
        
        #exit button
        if event.type == pygame.MOUSEMOTION:
            if exitButton.isOver(mousePos):
                exitButton.color = DARK_RED
            else:
                exitButton.color = LIGHT_RED
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitButton.isOver(mousePos):
                running = False
                exec(open('levels.py').read())
        
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False #stop the loop
            
        #change if the sound if muted or not
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sound.isOver(mousePos):
                #check if the volume is muted or not
                readVolume = open('storedInformation/Volume.txt','r')
                volume = readVolume.read()
                #unmute if the volume is muted
                if volume == "unmuted":
                    changeVolume = open('storedInformation/volume.txt','w')
                    changeVolume.write('muted')
                    changeVolume.close()
                #mute if the volume is unmuted
                else:
                    changeVolume = open('storedInformation/volume.txt','w')
                    changeVolume.write('unmuted')
                    changeVolume.close()
                readVolume.close()
        #for whatever reason the text file is backwards and says muted when unmuted, and unmuted when muted
        
        #jump when the space bar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #this is where it will test if the player is standing on something it can jump off of
                if player.grounded:
                    player.grounded = False
                    player.jumping = True
                    
        #remove extra height when the space bar is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if player.jumping:
                    player.jumpHeight-=player.addedHeight
        
    #Get all the keys that are being currently pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:    #while the a key is being pressed move the player left
        if player.canMoveLeft:
            player.x -= 4
    if keys[pygame.K_d]:
        if player.canMoveRight:
            player.x += 4
    
    #if the player is holding the space bar add more height to the jump
    if keys[pygame.K_SPACE]:
        if player.jumping:
            if player.canAddHeight:
                player.addedHeight = player.jumpHeight
                player.jumpHeight += player.addedHeight + 5
                player.canAddHeight = False
        
    #gravity
    if player.grounded == False and player.jumping == False:
        player.y+=4
    
    #end the level because for whatever reason I cant do it from the endZone class
    if endzone.active:
        readVolume = open('storedInformation/Volume.txt','r')
        volume = readVolume.read()
        if volume == "muted":
            pygame.mixer.music.load('resources/sounds/ding.wav')
            pygame.mixer.music.play()
        clock.tick(2)
        running = False
        exec(open('levels.py').read())
        
    #restart the level if dead
    if deathPlane.triggered or flashingPlane.triggered:
        readVolume = open('storedInformation/Volume.txt','r')
        volume = readVolume.read()
        if volume == "muted":
            pygame.mixer.music.load('resources/sounds/error.wav')
            pygame.mixer.music.play()
        clock.tick(2)
        running = False
        exec(open('lvlTwo.py').read())
        
    
    #prepare the frame
    screen.fill(GREY)   #background
    
    #level
    endzone.draw()
    deathPlane.draw()
    startingPlatform.draw()
    secondPlatform.draw()
    
    flashingPlane.draw()
    flashingPlatform.draw()
    
    startingWall.draw()
    #secondWall.draw()
    
    #player
    player.draw()
    
    #UI
    exitButton.draw(screen)
    sound.update()

        
    #after frame is ready
    pygame.display.flip()
