import random

CELL = 0
WALL = 1

# REFRENCE: https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e 

# TODO: make a better solid_wall function
def solid_wall(end, place, version):
    place = place
    i = 0
    if version == 'row':
        while i < end:
            place[i] = 1
            i+=1
    
    # implement general case for edges       
    elif version == 'col':
        while i < end:
            pass
        

def surrondingCells(maze, rand_wall):
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


def gm(width, height):
    cell = 0
    wall = 1
    maze = []

    # Generates maze with only walls
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(WALL)
        maze.append(line)
    
    # Choose a random wall in the maze 
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    
    # Makes sure the starting wall is not part of the outer wall
    if starting_height == 0:
        starting_height += 1
    if starting_height == height-1:
        starting_height -= 1
    
    if starting_width == 0:
        starting_width += 1
    if starting_width == width-1:
        starting_width -= 1
        
    
    # Change current wall to path and marks surrounding walls    
    maze[starting_height][starting_width] = CELL
    walls = []
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
        rand_wall = walls[int(random.random()*len(walls))-1]
    
    
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == WALL and maze[rand_wall[0]][rand_wall[1]+1] == CELL:
                s_cells = surrondingCells(maze, rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
        
        if rand_wall[0] != 0:        
            if maze[rand_wall[0]-1][rand_wall[1]] == WALL and maze[rand_wall[0]+1][rand_wall[1]+1] == CELL:
                s_cells = surrondingCells(maze, rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
        
        if rand_wall[0] != height-1:    
            if maze[rand_wall[0]+1][rand_wall[1]] == WALL and maze[rand_wall[0]-1][rand_wall[1]] == CELL:
                s_cells = surrondingCells(maze, rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
        
        if rand_wall[1] != width-1:    
            if maze[rand_wall[0]][rand_wall[1]+1] == WALL and maze[rand_wall[0]][rand_wall[1]-1] == CELL:
                s_cells = surrondingCells(maze, rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = CELL
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
        
    
    return maze

def generate_maze(width, height):
    maze = []
    for row in range(0, height):
        maze.append(list())
        for col in range(0, width):
            maze[row].append(random.randint(0,1))
   
    solid_wall(len(maze[0]), maze[0], 'row')        
    solid_wall(len(maze[len(maze)-1]), maze[len(maze)-1], 'row')
     
    # TODO: replace following while loops with the solid_wall function        
    i = 0
    while i < len(maze):
        maze[i][0] = 1
        i+=1
        
    i = 0
    while i < len(maze):
        maze[i][len(maze[i])-1] = 1
        i+=1        
    
    return maze
            


if __name__ == '__main__':
    pass