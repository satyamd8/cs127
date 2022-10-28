#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 5, 2022
#This program prints: an input's ASCII code and next second letter

phrase = input ("Enter a phrase: ")
print("letter ASCII next_two_letter")
for i in (phrase):
    print("%6c %5i %15c"%(i, ord(i), chr(ord(i)+2)))
