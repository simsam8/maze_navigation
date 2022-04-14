import random

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
        

def gm(width, height):
    cell = 0
    wall = 1
    maze = []

    # Generates maze with only walls
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(wall)
        maze.append(line)
    
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