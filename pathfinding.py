
import numpy as np

#create a 10 by 10 grid
x = np.ones((10, 10))

#define start and end point
x[0,0] = 'Start'
x[9,9] = 'End'

#define the obstacles
x[9,7] = 'Obstacle'
x[8,7] = 'Obstacle'
x[6,7] = 'Obstacle'
x[6,8] = 'Obstacle'



