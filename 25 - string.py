#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 19, 2022
#This program prints: strings

string = input("Enter a string with 0 or 1 only: ")

num = 0
base = 2
weight = 1
length = len(string)
stringReverse = string[::-1]

for i in stringReverse:
    ch = ""
    ch += i
    if ch == "1":
        num += weight
    elif ch != "0":
        print("Letter", ch, "is not allowed in binary string")
        exit
    weight *= base

print("num =", num)
