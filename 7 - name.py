#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 5, 2022
#This program prints: name and email information

fullName = input("Enter name in format firstName lastName: ")
n = fullName.split()
print ("name in LASTNAME, firstName format: "+n[1].upper()+ "," , n[0])
       
hEmail = input("Enter user name of email: ")
h = hEmail.lower()
print ("email: {}@hunter.cuny.edu".format(h))
