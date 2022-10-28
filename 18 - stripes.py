#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 11, 2022
#This program prints: striped blue and green pattern

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size:"))
file = input("Enter output file:")

x = np.zeros( (size, size, 3) )

x[:, ::2, 2] = 1.0
x[:, 1::2, 1] = 1.0

#plt.imshow(x)
#plt.show

plt.imsave(file, x)
