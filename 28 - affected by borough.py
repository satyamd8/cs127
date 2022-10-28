#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 26, 2022
#This program prints: affected per borough

import matplotlib.pyplot as plt
import pandas as pd

choice = input("Enter a choice: \na. group by borough \nb. group by year \n")

chart = pd.read_csv('children_lead.csv')
if choice == "a":
    print(chart.groupby('borough')['affected_children'].mean())
    
    borough = input("Enter a borough: ")
    boroughGroup = chart.groupby('borough').get_group(borough)
    
    print("average number of affected children of", borough, "is", boroughGroup['affected_children'].mean())
    print("min number of affected children of", borough, "is", boroughGroup['affected_children'].min())
    print("max number of affected children of", borough, "is", boroughGroup['affected_children'].max())
if choice == "b":
    print(chart.groupby('year')['affected_children'].mean())
    
    year = int(input("Enter a year (2005 - 2016): "))
    yearGroup = chart.groupby('year').get_group(year)
    
    print("average number of affected children in", year, "is", yearGroup['affected_children'].mean())
    print("min number of affected children in", year, "is", yearGroup['affected_children'].min())
    print("max number of affected children in", year, "is", yearGroup['affected_children'].max())
elif choice != "a" and choice != "b":
    print("wrong choice")
