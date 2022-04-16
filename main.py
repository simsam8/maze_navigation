import pygame
import maze_generator as mg

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

cell_colors = {
    1 : white,
    3 : green,
    4 : red
}



pygame.init()

MAP_WIDTH, MAP_HEIGHT = 10, 10
MAP = mg.generate_maze(MAP_WIDTH, MAP_HEIGHT)
SCREEN_INFO = pygame.display.Info()
WIDTH = SCREEN_INFO.current_w*0.5
HEIGHT = SCREEN_INFO.current_h*0.5
RATIO = WIDTH/HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mazerunner')

# Find start position in maze
def start_pos(map):
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 3:
                return [j, i]
            else:
                continue

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


class Player(Maze):
    def __init__(self) -> None:
        super().__init__(MAP)
        self.color = blue
        self.radius = self.block_width/4
        self.position = start_pos(self.map)
        self.center = (self.position[0]*self.block_width+self.block_width/2,
                        self.position[1]*self.block_height+self.block_height/2)
        
    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.radius)
        
    def update_pos(self, direction):
        if direction == 'u':
            self.position[1] -= 1
            self.center = (self.position[0]*self.block_width+self.block_width/2,
                        self.position[1]*self.block_height+self.block_height/2)
        if direction == 'd':
            self.position[1] += 1
            self.center = (self.position[0]*self.block_width+self.block_width/2,
                        self.position[1]*self.block_height+self.block_height/2)
        if direction == 'l':
            self.position[0] -= 1
            self.center = (self.position[0]*self.block_width+self.block_width/2,
                        self.position[1]*self.block_height+self.block_height/2)
        if direction == 'r':
            self.position[0] += 1
            self.center = (self.position[0]*self.block_width+self.block_width/2,
                        self.position[1]*self.block_height+self.block_height/2)
        
        
        print(self.position)
        print(self.center)


lab = Maze(MAP)
player = Player()



def loop():
    
    running = True
    
    screen.fill((0,0,0))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.update_pos('u')
                if event.key == pygame.K_DOWN:
                    player.update_pos('d')
                if event.key == pygame.K_LEFT:
                    player.update_pos('l')
                if event.key == pygame.K_RIGHT:
                    player.update_pos('r')
                    
            
        
        lab.draw()
        player.draw()
        pygame.display.update()
            
if __name__ == '__main__':
    loop()