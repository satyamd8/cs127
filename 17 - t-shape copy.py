#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 10, 2022
#This program prints: t-shape in array

import matplotlib.pyplot as plt
import numpy as np

output = input ("Enter output file name: ")

img = np.ones( (30, 30, 3) )
img[:,:,0] = 1
img[:,:,1] = 1
img[:,:,2] = 0

for i in range(5, 8, 1):
    for j in range(5, 25, 1):
        img[i, j, 0] = 0
        img[i, j, 1] = 0
        img[i, j, 2] = 1

for i in range(8, 25, 1):
    for j in range(13, 16, 1):
        img[i, j, 0] = 0
        img[i, j, 1] = 1
        img[i, j, 2] = 0

#plt.imshow(img)
#plt.show()

plt.imsave(output,img)
