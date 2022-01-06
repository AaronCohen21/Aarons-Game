import pygame

#inits because for whatever reason they don't work down with the other ones
pygame.font.init()
pygame.mixer.init()
#constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60
TITLE = "Aaron's Game"

#colors
GREY = [209, 209, 209]
GREEN = [189, 237, 183]
DARK_GREY = [191, 191, 191]
DARKER_GREY = [82, 82, 82]
BLUE = [130, 208, 224]
PLAYER_GREY = [125, 125, 125]
LIGHT_RED = [242, 162, 162]
DARK_RED = [252, 86, 86]

#classes
class Check():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        image = pygame.image.load('resources/images/checkMark.png')
        screen.blit(image,(self.x,self.y))
        
class Sound():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update(self):
        notMuted = pygame.image.load('resources/images/volumeFull.png')
        muted = pygame.image.load('resources/images/volumeMute.png')
        readVolume = open('storedInformation/Volume.txt','r')
        volume = readVolume.read()
        if volume == "muted":
            screen.blit(muted,(self.x-50,self.y-50))
            pygame.mixer.Channel(1).set_volume(1.0)
            
        else:
            screen.blit(notMuted, (self.x-50,self.y-50))
            pygame.mixer.Channel(1).set_volume(0.0) 
            
        readVolume.close()
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - 50 and pos[0] < self.x+50:
            if pos[1] > self.y - 50 and pos[1] < self.y+50:
                return True
            
        return False
        
class customTitle():
    def __init__(self,x,y,size,text=''):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
    def draw(self,screen):
        if self.text != '':
                font = pygame.font.Font("resources/fonts/gameFont.ttf",self.size)
                text = font.render(self.text, 1, (0,0,0))
                screen.blit(text, (self.x - (text.get_width()/2), self.y - (text.get_height()/2)))

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen):
        #Call this method to draw the button on the screen
        pygame.draw.rect(screen, self.color, (self.x-(self.width/2),self.y-(self.height/2),self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font("resources/fonts/gameFont.ttf",60)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x - (text.get_width()/2), self.y - (text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - (self.width/2) and pos[0] < self.x+(self.width/2):
            if pos[1] > self.y - (self.height/2) and pos[1] < self.y+(self.height/2):
                return True
            
        return False


class Title():
    #sprite for the menu
    def draw(self,screen):
        
        font = pygame.font.Font("resources/fonts/gameFont.ttf",120)
        text = font.render("Aaron's Game", True, (0,0,0))
        screen.blit(text, ((WINDOW_WIDTH/2)-(text.get_width()/2),(WINDOW_HEIGHT/2)-100))
        

#sprites and buttons
startButton = Button(LIGHT_RED,WINDOW_WIDTH/2,(WINDOW_HEIGHT/2)+100,200,66,'start')

#initialize everything
pygame.init()
pygame.mixer.init()

#initialize the screen and everything to do with it
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)

#sprite group

#set up the game loop
clock = pygame.time.Clock()

#start running each scene
