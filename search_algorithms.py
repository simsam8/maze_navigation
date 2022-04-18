import maze_generator as mg
import math

maze = mg.generate_maze(5,5)

def start_pos(map):
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 3:
                return [j, i]
            else:
                continue
            
def end_pos(map):
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 4:
                return [j, i]
            else:
                continue

def calc_distance(map, start, end):
    start_to_node = []
    end_to_node = []
    total_cost = []
    current_pos = start
    print(end)
    print(start)
    
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] != 0:
                pass
            else:
                #print('start_to_node', start, (i,j) ,(math.sqrt((i-start[0])**2 + (j-start[1])**2)))
                start_to_node.append((math.sqrt((i-start[0])**2 + (j-start[1])**2)))
                end_to_node.append((math.sqrt((i-end[0])**2 + (j-end[1])**2)))
    
    for i in range(0, len(start_to_node)):
        total_cost.append(start_to_node[i]+end_to_node[i])
        
    print(start_to_node)
    print(end_to_node)    
    print(total_cost)
    #print(start_to_node)
    #distance = (math.sqrt((end[0]-current_pos[0])**2 + (end[1]-current_pos[1])**2))
    #print(distance)
    
calc_distance(maze, start_pos(maze), end_pos(maze))
print(maze)