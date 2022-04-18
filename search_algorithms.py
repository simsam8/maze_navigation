import maze_generator as mg
import math
import time

# Refrence for A* search
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

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
            

class CellNode:
    def __init__(self, pos, start, end) -> None:
        self.pos = tuple(pos)
        self.g_cost = math.sqrt((pos[0]-start[0])**2 + (pos[1]-start[1])**2)
        self.h_cost = math.sqrt((pos[0]-end[0])**2 + (pos[1]-end[1])**2)
        self.f_cost = self.g_cost + self.h_cost
        self.parent = None
        

# TODO: Fix the algorithm to not infinitely add cells to open_list
def A_star(map):
    start = start_pos(map)
    end = end_pos(map)
    
    open_list = []
    closed_list = []
    
    # Adds starting cell to the open list
    current_cell = CellNode(start, start, end)
    
    open_list.append(current_cell)
    
    
    
    #return [x.pos for x in open_list]
    
    # Loop untill end
    while open_list != []:
        
        # Look for the lowest F cost node in the open list
        # Switch it to the closed list
        open_list.sort(key=lambda x: x.f_cost)
        print([x.pos for x in open_list])
        current_cell = open_list.pop(0)
        closed_list.append(current_cell)
        
        print(current_cell.pos)
        
        # Goal check
        if current_cell.pos == end:
            break
        
        # Possible child nodes
        try: adj_top = CellNode((current_cell.pos[0]-1, current_cell.pos[1]), start, end)
        except: adj_top = current_cell
        adj_bot = CellNode((current_cell.pos[0]+1, current_cell.pos[1]), start, end)
        adj_left = CellNode((current_cell.pos[0], current_cell.pos[1]-1), start, end)
        adj_right = CellNode((current_cell.pos[0], current_cell.pos[1]+1), start, end)
        
        adjacent = [adj_top, adj_bot, adj_left, adj_right]
        
        
        for cell in adjacent:
            #print('In for loop')
            if cell in closed_list or map[cell.pos[0]][cell.pos[1]] == 1:
                continue
            if cell not in open_list:
                cell.parent = current_cell
                
            cell.g_cost = current_cell.g_cost + math.sqrt((cell.pos[0]-current_cell.pos[0])**2 + (cell.pos[1]-current_cell.pos[1])**2)
            
            if cell in open_list:
                if cell.g_cost > open_list[0]:
                    continue
                
            open_list.append(cell)
        
        print(len(open_list)) 
        time.sleep(1)
    
    return closed_list        
    
    
A_star(maze) 

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
    
#calc_distance(maze, start_pos(maze), end_pos(maze))
#print(maze)