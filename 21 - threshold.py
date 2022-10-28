#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 16, 2022
#This program prints: white pixel count

import numpy as np
import matplotlib.pyplot as plt

file = input("Enter file name: ")
t = float(input("Enter threshold: "))

img = plt.imread(file)
whitePixels = 0
totalPixels = 0

for i in range(img.shape[0]):
     for j in range(img.shape[1]):
          if (img[i,j,0] > t) and (img[i,j,1] > t) and (img[i,j,2] > t):
              whitePixels += 1
          totalPixels +=1

print("number of white pixels:", whitePixels)

percent = round((whitePixels/totalPixels)*100, 2)
print("percent of white pixels:", percent, "%")
