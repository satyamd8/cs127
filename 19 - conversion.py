#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 12, 2022
#This program prints: conversion

import math

print("(a) convert centimeters to feet \n(b) convert centimeters to feet and inches \n(c) convert feet and inches to centimeters")
choice = input("Enter a or b or c: ")

if choice == "a":
    cm = float(input("Enter height in centimeters: "))
    print("height is", round(cm/30.48, 2), "feet")

if choice == "b":
    cm = float(input("Enter height in centimeters: "))
    feet = math.floor(cm/30.48)
    inches = round((cm%30.48)/2.54)
    if inches == 0:
        print("height is", feet, "feet")
    else:
        print("height is", feet, "feet and", inches, "inches")

if choice == "c":
    feet, inch = input("Enter height in feet and inches, separated by a space: ").split()
    ft = int(feet)
    i = int(inch)
    cm = round((ft*30.48) + (i*2.54))
    print("height is", cm, "cm")

elif choice != "a" "b" "c":
    print("Wrong choice, please enter only a or b or c")
    
    
