#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 26, 2022
#This program prints: borough map

import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
output = input("Enter output name: ")

case = pd.read_csv(file)

print("Min:", round(case[borough].min(), 3))
print("Max:", round(case[borough].max(), 3))
print("Mean:", round(case[borough].mean(), 3))
print("Median:", round(case[borough].median(), 3))
print("Standard Deviation:",round(case[borough].std(), 3))
      
case['Fraction'] = case[borough]/case['case_count']
case.plot(x = 'Date of Interest', y = 'Fraction')

fig = plt.gcf()
fig.savefig(output)
