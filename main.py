import pygame
import maze_generator as mg

cell_colors = {
    1 : (255,255,255),
    3 : (255,0,0),
    4 : (0,255,0)
}


pygame.init()

MAP = mg.generate_maze(100,100)
SCREEN_INFO = pygame.display.Info()
WIDTH = SCREEN_INFO.current_w*0.5
HEIGHT = SCREEN_INFO.current_h*0.5
RATIO = WIDTH/HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mazerunner')



class Maze():
    def __init__(self, map) -> None:
        self.map = map
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.colors = cell_colors
        self.block_height = HEIGHT/self.map_height
        self.block_width = WIDTH/self.map_width
        
    def draw(self):
        blocks =  []
        x = 0
        y = 0
        
        r = 0
        c = 0
        
        for row in self.map:
            for col in row:
                if col == 0:
                    pass
                else:
                    blocks.append([pygame.Rect(x, y, self.block_width, self.block_height), col])
                
                x += self.block_width
                c += 1
                
                if c == self.map_width:
                    x = 0
                    c = 0
            
            y += self.block_height
            r += 1
            
            
            
            
        for x in blocks:
            #print(x)
            pygame.draw.rect(screen, self.colors[x[1]], x[0], width=10)
        
    
    def print_dim(self):
        print(self.map_width, self.map_height)

lab = Maze(MAP)


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