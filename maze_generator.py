import random

CELL = 0
WALL = 1
UNVISIT = 2
maze = []
walls = []

# REFRENCE: https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e 
        
def surrondingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == CELL):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == CELL):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == CELL):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1] == CELL):
        s_cells += 1
    
    return s_cells


def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)
            
            
def make_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == UNVISIT):
                maze[i][j] = WALL
                
# Creates random entrance and exit
def create_entrance_exit(width, height):
    i = random.randrange(0, width)
    while maze[1][i] != CELL:
        i = random.randrange(0, width)
    if (maze[1][i] == CELL):
        maze[0][i] = 3
    
            
    j = random.randrange(0, width)
    while maze[height-2][j] != CELL:
        j = random.randrange(0, width)
    if (maze[height-2][j] == CELL):
        maze[height-1][j] = 4        
            
    
def generate_maze(width, height):

    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(UNVISIT)
        maze.append(line)
    
    # Randomize starting point and set it as a cell
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    if starting_height == 0:
        starting_height += 1
    if starting_height == height-1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width-1:
        starting_width -= 1
        
    print(starting_height, starting_width)
    
    # Mark it as cell and add surrounding walls to the list    
    maze[starting_height][starting_width] = CELL
    walls.append([starting_height-1, starting_width])
    walls.append([starting_height, starting_width-1])
    walls.append([starting_height, starting_width+1])
    walls.append([starting_height+1, starting_width])
    
    # Denote the blocks around the starting cell as walls
    maze[starting_height-1][starting_width] = WALL
    maze[starting_height][starting_width-1] = WALL
    maze[starting_height][starting_width+1] = WALL
    maze[starting_height+1][starting_width] = WALL
    
    # While there are walls in the list pick a random wall from the list
    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]
    
        # Check if it is a left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == UNVISIT and maze[rand_wall[0]][rand_wall[1]+1] == CELL:
                # Find the number of surrounding cells
                s_cells = surrondingCells(rand_wall)
                
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                    
                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    
                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    
                # Delete wall  
                delete_wall(rand_wall)
                continue
                
        # Check if it is an upper wall
        if (rand_wall[0] != 0):        
            if maze[rand_wall[0]-1][rand_wall[1]] == UNVISIT and maze[rand_wall[0]+1][rand_wall[1]] == CELL:
                
                s_cells = surrondingCells(rand_wall)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                    
                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    
                    # Rightmost cell
                    if (rand_wall[1] != width-1):	
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])       
                    
                # Delete wall
                delete_wall(rand_wall)
                continue
                
        
        # Check the bottom wall
        if rand_wall[0] != height-1:    
            if maze[rand_wall[0]+1][rand_wall[1]] == UNVISIT and maze[rand_wall[0]-1][rand_wall[1]] == CELL:
                
                s_cells = surrondingCells(rand_wall)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    # Mark the new walls
                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    
                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    
                    # Rightmost cell
                    if (rand_wall[1] != width-1):	
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                
                # Delete wall  
                delete_wall(rand_wall)
                continue
        
        # Check the right wall
        if rand_wall[1] != width-1:    
            if maze[rand_wall[0]][rand_wall[1]+1] == UNVISIT and maze[rand_wall[0]][rand_wall[1]-1] == CELL:
                
                s_cells = surrondingCells(rand_wall)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    # Mark the new walls
                    # Rightmost cell
                    if (rand_wall[1] != width-1):	
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    
                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                
                # Delete wall
                delete_wall(rand_wall)
                continue
        
        # Delete the wall from the list anyway
        delete_wall(rand_wall)
    
    # Mark the remaining unvisited cells as walls
    make_walls(width, height)
    
    # Set entrance and exit
    create_entrance_exit(width, height)
    
    return maze
            


if __name__ == '__main__':
    pass