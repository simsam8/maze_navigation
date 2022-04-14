import pygame
import map


pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH = SCREEN_INFO.current_w*0.3
HEIGHT = SCREEN_INFO.current_h*0.3
RATIO = WIDTH/HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mazerunner')



class Maze():
    def __init__(self, map) -> None:
        self.map = map
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.color = (255,255,255)
        self.block_height = HEIGHT/self.map_height
        self.block_width = WIDTH/self.map_width
        #print(self.block_height, self.block_width)
        
    def draw(self):
        blocks =  []
        x = 0
        y = 0
        
        r = 0
        c = 0
        
        for row in self.map:
            for col in row:
                if col == 1:
                    blocks.append(pygame.Rect(x, y, self.block_width, self.block_height))
                else:
                    pass
                x += self.block_width
                c +=1
                
                if c == self.map_width:
                    x = 0
                    c = 0
            
            y += self.block_height
            r += 1
            
            
            
            
        for x in blocks:
            pygame.draw.rect(screen, self.color, x, width=10)
        
    
    def print_dim(self):
        print(self.map_width, self.map_height)

lab = Maze(map.random)


def loop():
    
    running = True
    
    screen.fill((0,0,0))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            
        
        lab.draw()
        pygame.display.update()
            
if __name__ == '__main__':
    loop()