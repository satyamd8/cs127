#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 27, 2022
#This program prints: list of words

askPhrase = input("Enter a list of names, separated by semicolon: ")
nameList = askPhrase.split(";")

for name in nameList:
    temp = name.split(" ")
    print(temp[0][0]+ ".", temp[1])
    
