#make a program that is going to print 1-5
#create a variable starting at 1
#umber=1 #this is our starting point

#want to keep looping while number is less than or equal to five
#hile number<=5: #this is essentially where it will stop
 #      print(number)
 #      number+=1 #add 1 to number after each loop

# I want to start counting at 0 count to 50 and get there by increments of 5
 #mber2=0
#hile number2<=50:
 #      print(number2)
 #    number2+=5
 #a while loop is useful when you want to keep asking until the user gives a valid answer
#ask the user for their age
#ge=int(input("Enter your age: "))

#keep looping if the age is less than 1 or greater than 120
#ile age <1 or age >120: #the loop only runs if one of the conditions is true
            #tell user, invalid input
 #          print("Invalid age ")
            #ask the user to enter their age again
#           age=int(input("Enter your age: "))
            #this runs after the loop finishes
#print("Thank you")



#create a list containing 3 games
games=["Minecraft", "Mario", "Zelda"]
cars=["Honda", "toyota", "Nissan"]
#take one item from the games list at a time
for game in games:
    #print the current game
    print(game)




    #each time the loop repeats, game holds the next item in the list
    #range() creates a sequence of numbers
    #starts at 2 and stops right before 8
for number in range(2,8): #2 is starting number stop right before this number
    print(number)
    #remember: the ending number in range() is not included 

#we can also perform calculations inside the loop:
#loop through numbers 2 through 7
for number in range(2,8):
    #multiply the number by itself
    square=number*number
    #print the squared number
    print(square)



#looping through a string
#store a name inside the string
name="Daniel"
#take one character from the string at a time
for letter in name:
    print(letter)
#this works very similiar to how we loop through a list



#using break
#break stops a loop early
#loop through numbers 1-10
for number in range(1,11):
    #print the current number 
    print(number)
    #break the loop when number hits 
    if number==5:  #everything after the : runs only if the condition is true
        #once number is equal to 5 it will stop (break)
        break



    #nested loop
    #nested loop is a loop inside another loop

    #outer loop run through 1 2 3
    for number in range(1,4):
        #inner loop also runs through 1 2 3
        for number2 in range (1,4):
            print(number,number2)



#choosing the right loop?
#use a while loop when repitiion depends on a condition
#keep looping while answer is not yes
while answer !="yes":
    #ask the user again
    answer=input("Enter yes: ")

#use a for loop when working through item#
#go thorugh each item in the list
item=["apples", "oranges", "bananas"]
for item in items:
    print(item)
    #print the current item

    #use FOR with RANGE() when working through numbers

    #loop throug 1-10
for number in range(1,11):
    #print the current number
    print(number)

    