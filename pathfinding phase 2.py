import numpy as np
import heapq

#pathfinding using a* algorithm

#create the grid, is flipped on y=x
grid = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]])



start = (0,0)
end = (9,9)
step = 0

#heuristic function (straight line distance)
def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

#a* path algorithm
def astar(array, start, end,step):
    #possible neighbours
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    #list of nodes no longer considered
    closed_list = set()
    #previous path
    previous = {}
    #
    gscore = {start:0}
    #heuristic score
    fscore = {start:heuristic(start, end)}

    #open list
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))

    #loop until no more in open list
    while oheap:
        current = heapq.heappop(oheap)[1]

        #end of current
        if current == end:
            data = []
            data.append('number of steps: '+ str(step))
            while current in previous:
                data.append(current)
                current = previous[current]
            return data
            
        #add current to closed list
        closed_list.add(current)

        #check heuristic of neigbours and choose next position
        for i, j in neighbors:
            step = step + 1
            neighbor = current[0] + i, current[1] + j
            temp_gscore = gscore[current] + heuristic(current, neighbor)
            
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    
                    continue
            else:
                
                continue
 
            if neighbor in closed_list and temp_gscore >= gscore.get(neighbor, 0):
                continue

            if  temp_gscore < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                previous[neighbor] = current
                gscore[neighbor] = temp_gscore
                fscore[neighbor] = temp_gscore + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False


#main code calling a* function
route = astar(grid,start,end,step)

route = route + [start]
route = route[::-1]
print(route)