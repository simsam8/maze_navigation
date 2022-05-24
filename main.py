import pygame
import maze_generator as mg
from random import randrange as rr

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

CLOCK = pygame.time.Clock()
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

MAP_WIDTH, MAP_HEIGHT = 30, 30
MAP = mg.generate_maze(MAP_WIDTH, MAP_HEIGHT)
SCREEN_INFO = pygame.display.Info()
WIDTH = SCREEN_INFO.current_w
HEIGHT = SCREEN_INFO.current_h
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
            
# Find end position in maze         
def end_pos(map):
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 4:
                return [j, i]
            else:
                continue
            
# Counts number of a certain cell type
def count_celltype(map, cell):
    count = 0
    for x in map:
        for y in x:
            if y == cell:
                count += 1
                
    return count


class Maze():
    def __init__(self, map) -> None:
        self.map = map
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.colors = cell_colors
        self.block_height = HEIGHT/self.map_height
        self.block_width = WIDTH/self.map_width
        self.block_thickness = int(self.block_width*0.1)
        #print(self.block_thickness)
        
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
            pygame.draw.rect(screen, self.colors[x[1]], x[0]) # Optional: width=self.block_thickness
        

# Stop clock timer class 
class Timer(Maze):
    def __init__(self) -> None:
        super().__init__(MAP)
        self.color = blue
        self.counter = self.map_width
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render(str(self.counter), True, self.color)
        
    def update_counter(self):
        self.counter -= 1
        self.text = self.font.render(str(self.counter), True, self.color)
        
    
    def draw(self):
        screen.blit(self.text, (self.block_width/2,self.block_height/2))
        

class Player(Maze):
    def __init__(self) -> None:
        super().__init__(MAP)
        self.color = blue
        self.radius = self.block_width/4
        self.position = start_pos(self.map)
        self.dimension = (self.block_width/2, self.block_height/2)
        self.coords = (self.position[0]*self.block_width+self.block_width/4,
                        self.position[1]*self.block_height+self.block_height/4)
        self.center = (self.position[0]*self.block_width,
                        self.position[1]*self.block_height)
        self.object = pygame.Rect(self.coords, self.dimension)
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.object)
    
    # Check if player collides with wall    
    def wall_collision(self):
        if self.map[self.position[1]][self.position[0]] == 1:
            #print('Wall collision')
            return True
        

    def win(self):
        if self.map[self.position[1]][self.position[0]] == 4:
            print('YOU WIN')
            return True
        
    # Check if player is out of bounds
    def collision_check(self):
        if self.position[0] < 0:
            self.position[0] += 1
        if self.position[1] < 0:
            self.position[1] += 1
        if self.position[0] > self.map_width-1:
            self.position[0] -= 1
        if self.position[1] > self.map_height-1:
            self.position[1] -= 1
    
    # Updates the player's position 
    def update_pos(self, direction):
        if direction == 'u':
            self.position[1] -= 1
            self.collision_check()
            if self.wall_collision() == True:
                self.position[1] += 1
            self.coords = (self.position[0]*self.block_width+self.block_width/4,
                        self.position[1]*self.block_height+self.block_height/4)
        
        if direction == 'd':
            self.position[1] += 1
            self.collision_check()
            if self.wall_collision() == True:
                self.position[1] -= 1
            self.coords = (self.position[0]*self.block_width+self.block_width/4,
                        self.position[1]*self.block_height+self.block_height/4)
        
        if direction == 'l':
            self.position[0] -= 1
            self.collision_check()
            if self.wall_collision() == True:
                self.position[0] += 1
            self.coords = (self.position[0]*self.block_width+self.block_width/4,
                        self.position[1]*self.block_height+self.block_height/4)
        
        if direction == 'r':
            self.position[0] += 1
            self.collision_check()
            if self.wall_collision() == True:
                self.position[0] -= 1
            self.coords = (self.position[0]*self.block_width+self.block_width/4,
                        self.position[1]*self.block_height+self.block_height/4)
        
        self.object.update(self.coords, self.dimension)
        
        #print(self.position)
        #print(self.map[self.position[1]][self.position[0]])
        #print(self.center)


lab = Maze(MAP)
player = Player()
stop_clock = Timer()



def loop():
    
    running = True
    
    screen.fill(black)
    
    while running:
        # Epilepsy
        #seiz = (rr(0,256), rr(0,256), rr(0,256))
        #lab.colors[1] = seiz
        CLOCK.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            
            # Timer events
            if event.type == timer_event:
                stop_clock.update_counter()
                if stop_clock.counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    print('YOU LOSE!')
                    return pygame.quit()
            
            # Check for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.update_pos('u')
                if event.key == pygame.K_DOWN:
                    player.update_pos('d')
                if event.key == pygame.K_LEFT:
                    player.update_pos('l')
                if event.key == pygame.K_RIGHT:
                    player.update_pos('r')
                    
            
        
        # Draw and fill screen
        lab.draw()
        player.draw()
        stop_clock.draw()
        pygame.display.flip()
        screen.fill(black)
        
        if player.win() == True:
            running = False
            
if __name__ == '__main__':
    loop()