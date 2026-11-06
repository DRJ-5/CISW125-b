def file1():
    with open ("Project4/n.txt","r") as file:
        contents=file.read()
        print(contents)
file1()



def writefile():
    with open ("Project4/n.txt","a") as file:
        file.write(input("What would you like to add to the file? ") + "\n")
    choice = input("Would you like to add more? Y or N").upper()
    if choice =="Y":
        writefile()
    elif choice =="N":
        file1()
    else:
        print("Invalid please try again.")

writefile()