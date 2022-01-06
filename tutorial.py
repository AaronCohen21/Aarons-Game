from template import *

running = True

sound = Sound(1202,652)

exitButton = Button(LIGHT_RED,111,42,200,66,'Exit')

title = customTitle(WINDOW_WIDTH/2,165,120,'Tutorial:')

instructions = customTitle(WINDOW_WIDTH/2,300,60,"use a + d to move")
instructions1 = customTitle(WINDOW_WIDTH/2,415,60,"press space to jump")
instructions2 = customTitle(WINDOW_WIDTH/2,530,60,"get to the green area to complete the level")

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
        #for whatever reason the text file is backwards and says muted when unmuted, and unmuted when muted
    
        
            
    #Update
    
    #prepare the frame
    screen.fill(GREY)   #background
    sound.update()
    exitButton.draw(screen)
    title.draw(screen)
    instructions.draw(screen)
    instructions1.draw(screen)
    instructions2.draw(screen)
    
    #after frame is ready
    pygame.display.flip()