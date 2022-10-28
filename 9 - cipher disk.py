#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 14, 2022
#This program prints: a cipher disk output based on user input

message = input("Enter an all-small-letter string: ")
shiftValue = int(input("Enter a non-negative int to shift: "))

cipheredNumber = " "
cipherOutput = " "

for i in (message):
    if ord(i) + shiftValue > ord("z"):
        cipheredNumber = (ord(i)+shiftValue) - 26
    else:
        cipheredNumber = ord(i)+shiftValue
    cipherOutput += (chr(cipheredNumber))

print("ciphered string:" +cipherOutput)

