#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 16, 2022
#This program prints: reverse phrase in upper case and acronyms

phrase = input("input: ")

print("user reverse:", phrase[::-1])
print("user reverse upper:", phrase[::-1].upper())

acList = phrase.split(" ")
acronym = ""

for word in(acList):
    acronym += word[0].upper()

print("user abbreviation:",acronym)
