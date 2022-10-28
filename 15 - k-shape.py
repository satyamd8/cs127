#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 24, 2022
#This program prints: words in a k-shape

ask = input ("Enter a phrase: ")
askList = ask.split(" ")
n = len(askList)
h = len(askList)

for item in range(n):
    print(' '.join(askList[:n]))
    n -= 1

n += 2
    
for item in range(h-1):
    print(' '.join(askList[:n]))
    n += 1
