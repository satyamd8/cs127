#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 10, 2022
#This program prints: t-shape in array

import matplotlib.pyplot as plt
import numpy as np

output = input ("Enter output file name: ")

img = np.empty( (30, 30, 3) )
img[:,:,0] = 255
img[:,:,1] = 255
img[:,:,2] = 0

img[5:8, 5:25] = (0, 0, 255)
img[8:25, 13:16] = (0, 255, 0)

plt.imshow(img)
plt.show()

plt.imsave(output,img)
