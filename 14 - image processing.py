#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 24, 2022
#This program prints: processed image with no red

import matplotlib.pyplot as plt
import numpy as np

h = input("Enter name of the input file: ")
m = input("Enter name of the output file: ")

img = plt.imread(h)

img2 = img.copy()
img2[:, :, 0] = 0

#plt.imshow(img2)
#plt.show()

plt.imsave(m, img2)
