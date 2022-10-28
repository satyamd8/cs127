#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: October 20, 2022
#This program prints: list of words and info

list = input("Enter a list of words, separated by a space: ").split()

print("number of words:", len(list))
counter = 0
for word in list:
    if (word[-1] == "a") or (word [-1] == "b"):
        counter += 1
print("number of words ending with a or b:", counter)
print("fraction of words ending with a or b:", round(counter/len(list),2))
