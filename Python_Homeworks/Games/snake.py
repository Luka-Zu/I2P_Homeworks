import random
import pygame
from pygame.locals import *
from pygame import mixer
# extensions 
# sscore  Menuline bacground image 
# music   180 rotations are blocked 
class Apple:
    def __init__(self,screen):
        self.applex = round(random.randint(0, 750)/40)*40
        self.appley = round(random.randint(0, 750)/40)*40

class PartOfSnake :
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen 
    def draw(self):
        pygame.draw.rect(self.screen, (255, 165, 0), pygame.Rect((self.x+7, self.y+7), (26, 26)) )
    def eq(self,other):
        return self.x== other.x and self.y==other.y

class Snake():

    def __init__(self,screen):
        mixer.init()
        mixer.music.load('sound.mp3')
        mixer.music.play()
        self.alreadyAte=0
        self.direction = "right"
        self.__speed = 40
        self.__body = [PartOfSnake(280,40,screen),PartOfSnake( 240, 40,screen),PartOfSnake(200,40,screen),PartOfSnake(160,40,screen),PartOfSnake(120,40,screen),PartOfSnake(80,40,screen)]
        self.__screen = screen 
        
    
    def updateDirection(self,newDir):
        self.direction=newDir

    def drawSnake(self,dir,apple):
        self.direction=dir
        if self.Ate(apple):
            self.alreadyAte+=1
            
            nextBody = self.__body
        else: 

            nextBody = self.__body[:-1]
        if self.direction=="right":
            prev = nextBody[0]
            nextBody.insert(0,PartOfSnake(prev.x + self.__speed , prev.y ,self.__screen))
        elif self.direction=="top":
            prev = nextBody[0]
            nextBody.insert(0, PartOfSnake(prev.x  , prev.y - self.__speed,self.__screen))
        elif self.direction=="left":
            prev = nextBody[0]
            nextBody.insert(0, PartOfSnake(prev.x - self.__speed , prev.y ,self.__screen))
        elif self.direction=="down":
            prev = nextBody[0]
            nextBody.insert(0, PartOfSnake(prev.x  , prev.y + self.__speed,self.__screen))
        

        self.__body = nextBody
        for x in self.__body : 
            x.draw()
        
    def Ate(self,apple):
        tail = self.__body[1] 
        head = self.__body[0]
        if tail.x == apple.applex and tail.y== apple.appley:
            return True
        if head.x == apple.applex and head.y== apple.appley:
            return True 
        return False

    def lost(self):
        tail = self.__body[-1] 
        head = self.__body[0]
        counthead=0 
        counttail=0 
        for x in self.__body:
            if tail.eq(x):
                counttail+=1
            if head.eq(x):
                counthead+=1
        if counthead>1 or counttail>1 :
            return True
        if head.x>=800 or head.x<0  or head.y>=760 or head.y<0 or tail.x>800 or tail.x<0  or tail.y>=760 or tail.y<0:
            return True 
        return False
        


class App:
    
    def __init__(self):
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT =  840
        self.running = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT-40))
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)
        self.backgroundImage = pygame.transform.scale( pygame.image.load('42337.webp')  ,(800,800))
    

    def run(self):
        self.init()
        while self.running:
            self.clock.tick(11)
            self.update()
            self.render()
            if self.snake.Ate(self.apple):
                self.render()

                self.apple = Apple(self.screen)
            if self.snake.lost():
                break
                
                
            
        
        self.cleanUp()

    def init(self):
        # self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake")
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        self.events()
 


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction!="right":
                   
                    self.snake.updateDirection("left")

                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d )and self.snake.direction!="left":
                    self.snake.updateDirection("right")


                if (event.key == pygame.K_UP or event.key == pygame.K_w )and self.snake.direction!="down":
                    self.snake.updateDirection("top")

                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction!="top":
                    self.snake.updateDirection("down")
        
        pygame.display.update()

    def render(self):
        self.screen.fill((0,0,1))
        self.screen.blit(self.backgroundImage,(0,0))
        self.drawGrid()
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.apple.applex+7, self.apple.appley+7, 26, 26))
        self.snake.drawSnake(self.snake.direction,self.apple)
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(0,762 , 800, 40))
        font = pygame.font.SysFont("Arial", 30)
        img = font.render('Snake / eat RED blocks /  score:'+str(self.snake.alreadyAte), True, (200,100,100))
        self.screen.blit(img, (20, 760))

    def drawGrid(self):
        blockSize = 40 #Set the size of the grid block
        for x in range(0, self.WINDOW_WIDTH, blockSize):
            for y in range(0, self.WINDOW_HEIGHT-80, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                innerRectangle = pygame.Rect(x+5, y+5, blockSize-10, blockSize-10)
                pygame.draw.rect(self.screen, 	 (165,42,42), innerRectangle, 1)
                pygame.draw.rect(self.screen, (124,252,0), rect, 1)


    def cleanUp(self):
        self= App()

if __name__ == "__main__":
    app = App()
    app.run()