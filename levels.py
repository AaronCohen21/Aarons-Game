from template import *

running = True

#sprites
oneButton = Button(LIGHT_RED,(WINDOW_WIDTH/2)-300,(WINDOW_HEIGHT/2)+50,100,100,'1')
oneCheck = Check(300,460)

twoButton = Button(LIGHT_RED,(WINDOW_WIDTH/2)-150,(WINDOW_HEIGHT/2)+50,100,100,'2')
twoCheck = Check(450,460)

threeButton = Button(LIGHT_RED,(WINDOW_WIDTH/2),(WINDOW_HEIGHT/2)+50,100,100,'3')
threeCheck = Check(600,460)

fourButton = Button(LIGHT_RED,(WINDOW_WIDTH/2)+150,(WINDOW_HEIGHT/2)+50,100,100,'4')
fourCheck = Check(750,460)

fiveButton = Button(LIGHT_RED,(WINDOW_WIDTH/2)+300,(WINDOW_HEIGHT/2)+50,100,100,'5')
fiveCheck = Check(900,460)

mainMenu = Button(LIGHT_RED,134,42,250,66,'Main Menu')
sound = Sound(1202,652)
resetProgress = Button(LIGHT_RED,1079,42,380,66,'Reset Progress')

tutorialButton = Button(LIGHT_RED,120,670,220,66,'Tutorial')

title = customTitle(WINDOW_WIDTH/2,(WINDOW_HEIGHT/2)-100,120,'Choose a Level')
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
                if oneButton.isOver(mousePos) or twoButton.isOver(mousePos) or threeButton.isOver(mousePos) or fourButton.isOver(mousePos) or fiveButton.isOver(mousePos) or mainMenu.isOver(mousePos) or tutorialButton.isOver(mousePos) or resetProgress.isOver(mousePos):
                    pygame.mixer.music.load('resources/sounds/click.wav')
                    pygame.mixer.music.play()
        
        #Reset Progress Button
        if event.type == pygame.MOUSEMOTION:    #change the color if hovering over
            if resetProgress.isOver(mousePos):
                resetProgress.color = DARK_RED
            else:
                resetProgress.color = LIGHT_RED
                
        if event.type == pygame.MOUSEBUTTONDOWN:    #reset the progress and remove check marks if clicked
            if resetProgress.isOver(mousePos):
                #change all the text files to say uncleared and remove the check marks
                delOne = open('storedInformation/oneCleared.txt', 'w')
                delOne.write('uncleared')
                delOne.close()
                
                delTwo = open('storedInformation/twoCleared.txt', 'w')
                delTwo.write('uncleared')
                delTwo.close()
                
                delThree = open('storedInformation/threeCleared.txt', 'w')
                delThree.write('uncleared')
                delThree.close()
                
                delFour = open('storedInformation/fourCleared.txt', 'w')
                delFour.write('uncleared')
                delFour.close()
                
                delFive = open('storedInformation/fiveCleared.txt', 'w')
                delFive.write('uncleared')
                delFive.close()
        
        #lvl 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if oneButton.isOver(mousePos):
                running = False
                exec(open('lvlOne.py').read())
                
        if event.type == pygame.MOUSEMOTION:
            if oneButton.isOver(mousePos):
                oneButton.color = DARK_RED
            else:
                oneButton.color = LIGHT_RED
        
        #lvl 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if twoButton.isOver(mousePos):  #test if previous level has been cleared
                oneCheck = open('storedInformation/oneCleared.txt','r')
                testOne = oneCheck.read()
                if testOne == "cleared":
                    running = False
                    exec(open('lvlTwo.py').read())
                else:
                    readVolume = open('storedInformation/Volume.txt','r')
                    volume = readVolume.read()
                    if volume == "muted":
                        pygame.mixer.music.load('resources/sounds/error.wav')
                        pygame.mixer.music.play()
                    readVolume.close()
                oneCheck.close()
                
        if event.type == pygame.MOUSEMOTION:
            if twoButton.isOver(mousePos):
                twoButton.color = DARK_RED
            else:
                twoButton.color = LIGHT_RED
        
        #lvl 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if threeButton.isOver(mousePos):
                twoCheck = open('storedInformation/twoCleared.txt','r')
                testTwo = twoCheck.read()
                if testTwo == "cleared":
                    running = False
                    exec(open('lvlThree.py').read())
                else:
                    readVolume = open('storedInformation/Volume.txt','r')
                    volume = readVolume.read()
                    if volume == "muted":
                        pygame.mixer.music.load('resources/sounds/error.wav')
                        pygame.mixer.music.play()
                    readVolume.close()
                twoCheck.close()
                
        if event.type == pygame.MOUSEMOTION:
            if threeButton.isOver(mousePos):
                threeButton.color = DARK_RED
            else:
                threeButton.color = LIGHT_RED
                
        #lvl 4
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fourButton.isOver(mousePos):
                threeCheck = open('storedInformation/threeCleared.txt','r')
                testThree = threeCheck.read()
                if testThree == "cleared":
                    running = False
                    exec(open('lvlFour.py').read())
                else:
                    readVolume = open('storedInformation/Volume.txt','r')
                    volume = readVolume.read()
                    if volume == "muted":
                        pygame.mixer.music.load('resources/sounds/error.wav')
                        pygame.mixer.music.play()
                    readVolume.close()
                threeCheck.close()
                
        if event.type == pygame.MOUSEMOTION:
            if fourButton.isOver(mousePos):
                fourButton.color = DARK_RED
            else:
                fourButton.color = LIGHT_RED
                
        #lvl 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fiveButton.isOver(mousePos):
                fourCheck = open('storedInformation/fourCleared.txt','r')
                testFour = fourCheck.read()
                if testFour == "cleared":
                    running = False
                    exec(open('lvlFour.py').read())
                else:
                    readVolume = open('storedInformation/Volume.txt','r')
                    volume = readVolume.read()
                    if volume == "muted":
                        pygame.mixer.music.load('resources/sounds/error.wav')
                        pygame.mixer.music.play()
                    readVolume.close()
                fourCheck.close()
                
        if event.type == pygame.MOUSEMOTION:
            if fiveButton.isOver(mousePos):
                fiveButton.color = DARK_RED
            else:
                fiveButton.color = LIGHT_RED
        
        #main menu button
        if event.type == pygame.MOUSEMOTION:
            if mainMenu.isOver(mousePos):
                mainMenu.color = DARK_RED
            else:
                mainMenu.color = LIGHT_RED
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mainMenu.isOver(mousePos):
                running = False
                exec(open('menu.py').read())
        
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
        
        #tutorial button
        if event.type == pygame.MOUSEMOTION:    #change color
            if tutorialButton.isOver(mousePos):
                tutorialButton.color = DARK_RED
            else:
                tutorialButton.color = LIGHT_RED
        
        if event.type == pygame.MOUSEBUTTONDOWN:    #launch tutorial
            if tutorialButton.isOver(mousePos):
                running = False
                exec(open('tutorial.py').read())
    
    #draw sprites
    screen.fill(GREY)   #background
    oneButton.draw(screen)
    twoButton.draw(screen)
    threeButton.draw(screen)
    fourButton.draw(screen)
    fiveButton.draw(screen)
    title.draw(screen)
    mainMenu.draw(screen)
    sound.update()
    resetProgress.draw(screen)
    tutorialButton.draw(screen)
    
    #check marks
    #these things check the stored text file to see if you have cleared the level and if so, display the check mark
    oneCleared = open('storedInformation/oneCleared.txt', 'r')
    testOne = oneCleared.read()
    if testOne == "cleared":
        oneCheck.draw()
    oneCleared.close()
        
    twoCleared = open('storedInformation/twoCleared.txt', 'r')
    testTwo = twoCleared.read()
    if testTwo == "cleared":
        twoCheck.draw()
    twoCleared.close()
        
    threeCleared = open('storedInformation/threeCleared.txt', 'r')
    testThree = threeCleared.read()
    if testThree == "cleared":
        threeCheck.draw()
    threeCleared.close()
        
    fourCleared = open('storedInformation/fourCleared.txt', 'r')
    testFour = fourCleared.read()
    if testFour == "cleared":
        fourCheck.draw()
    fourCleared.close()
        
    fiveCleared = open('storedInformation/fiveCleared.txt', 'r')
    testFive = fiveCleared.read()
    if testFive == "cleared":
        fiveCheck.draw()
    fiveCleared.close()
    
    #after frame is ready
    pygame.display.flip()