from template import *

running = True

sound = Sound(1202,652)
byAaron = customTitle(113,678,60,'By Aaron')

exitButton = Button(LIGHT_RED,111,42,200,66,'Quit')

while running:
    #Keep the loop running at the correct speed
    clock.tick(FPS)
    
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
                if startButton.isOver(mousePos):
                    pygame.mixer.music.load('resources/sounds/click.wav')
                    pygame.mixer.music.play()
                elif exitButton.isOver(mousePos):
                    pygame.mixer.music.load('resources/sounds/click.wav')
                    pygame.mixer.music.play()
                    clock.tick(16)  #give just enough time to play the sound effect
            readVolume.close()
                
        
        #test if the mouse is hovering over the button and change color if it is
        if event.type == pygame.MOUSEMOTION:
            if startButton.isOver(mousePos):
                startButton.color = DARK_RED
            else:
                startButton.color = LIGHT_RED
        
        #test if mouse is clicking the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(mousePos):
                running = False
                exec(open('levels.py').read())
                
        
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False #stop the loop
            
        #quit the game
        if event.type == pygame.MOUSEMOTION:
            if exitButton.isOver(mousePos):
                exitButton.color = DARK_RED
            else:
                exitButton.color = LIGHT_RED
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitButton.isOver(mousePos):
                
                running = False
        
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
        #for whatever reason the text file is backwards and says muted when unmuted, and unmuted when muted
    
    #Update
    
    #prepare the frame
    screen.fill(GREY)   #background
    startButton.draw(screen)
    Title.draw(screen,screen)
    sound.update()
    byAaron.draw(screen)
    exitButton.draw(screen)
    
    #after frame is ready
    pygame.display.flip()
