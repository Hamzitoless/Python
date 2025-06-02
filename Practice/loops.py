#---------LOOPS----------

#-----While loops-----

name=input("Enter your name:")
age=int(input("Enter your age:"))
while age  =="":
    print("You haven't entered your age")
    age=input("Enter your age lil bro:")

while age < 18:
        print("Grow up lil nigga")

        break

while age > 18:
        print(f"Hello {name}, you are {age} years old and you can enter the party")    

         
            
        break

while age<0:
       print("Please anter an age greater than 0 ")
       age=int(input("Enter your age:"))

       break

'''
#------------For loop------------
Example 1

'''


import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Wait for 1 second

print("Ramadhan Mubarak")


