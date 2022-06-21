
import numpy as np
import heapq

#pathfinding using a* algorithm

#create the grid
grid = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0]])

start = (0,0)
end = (9,9)

#heuristic euclidean function
def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def astar(array, start, end):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    previous = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, end)}

    oheap = []
    heapq.heappush(oheap, (fscore[start], start))
 
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == end:
            data = []

            while current in previous:
                data.append(current)
                current = previous[current]
            return data

        close_set.add(current)

        for i, j in neighbors:
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
 
            if neighbor in close_set and temp_gscore >= gscore.get(neighbor, 0):
                continue

            if  temp_gscore < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                previous[neighbor] = current
                gscore[neighbor] = temp_gscore
                fscore[neighbor] = temp_gscore + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

route = astar(grid, start, end)
route = route + [start]
route = route[::-1]
print(route)
