#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    
    #print all the moves here
    # I will implement a breadth first search
#     Search for the index in the 2 do list using matrix notation
    def grid_index(grid, item):
        x = [x for x in grid if item in x][0]
#         The tird element represents the distance from the initial state.Fourth emelnet represents the path from initual sate.
        return (grid.index(x), x.index(item), 0, [])

#      Convert the numerical path to directions
    def calc_path(directions):
        path=""
        if len(directions) != 0:
            for i in range(len(directions)):
                if directions[i] == 0:
                    path +="Up" +"\n"
                elif directions[i] == 1:
                    path +="Down" +"\n"
                elif directions[i] == 2:
                    path +="Left" +"\n"
                else:
                    path +="Right" +"\n"
        return path
                
                      
            
    
    
    initial_state = grid_index(grid, 'm')
    goal_state = grid_index(grid, 'p')
    path_cost =0
    # // 0 - Up, 1 - Donw, 2 - Left, 3 - Right
    actions =[0, 1, 2, 3] 
    if initial_state == goal_state:
        return calc_path(child[3])
    else:
        frontier=[]
        frontier.append(initial_state)
        explored =[]
        while len(frontier) >0:
            node =frontier.pop(0)
            explored.append(node)
            for action in range(len(actions)):
                if action == 0:
                    # /Moving up reduces the x coordinate by 1
                    move = list.copy(node[3])
                    move.append(action)
                    child =(node[0] -1, node[1], node[2] + 1, move)   
                elif action ==1:
                    move = list.copy(node[3])
                    move.append(action)
                    child =(node[0] + 1, node[1], node[2] + 1, move) 
                elif action ==2:
                    move = list.copy(node[3])
                    move.append(action)
                    child =(node[0], node[1] - 1, node[2] + 1, move) 
                else:
                    move = list.copy(node[3])
                    move.append(action)
                    child =(node[0], node[1] + 1, node[2] + 1, move) 
                if child not in frontier and child not in explored:
                    if goal_state[0] == child[0] and goal_state[1] == child[1]:
                        # print(child[3])
                        path = calc_path(child[3])
                        print(path)
                        return(0)
                        # break                    
                    else:
                        frontier.append(child)
                        # print(frontier)
                    
            
        



m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)