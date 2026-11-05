#learn how to writE, read, and edit files using python
#common modes when using files
#"r" read only
#you can read this file but cant change it
#Error if file doesnt exist

#"w" write 
#create the file if it doesnt exist
#overwrites the file if it does exist (deletes old content)


# "a"=append
#creates the file if it doesnt exist 
#adds new text to the file, does not delete existing content

#with open("foldername/filename","mode")
#with open("WEEK9/Stuff.txt", "r") as file:
#    contents=file.read()
#    print(contents)


#I want to completely overwrite the content in stuff.txt
with open ("WEEK9/Stuff.txt","w") as file:
    file.write("Hello\n this line appears underneath")
#Once we leave the indentation block the file is automatically closed


#reading from a file
# Method A: Read the whole file at once
#with open("WEEK(/Stuff.txt","r") as file:
 #   contents=file.read()
 #   print(contents)

#Method B: Read line by line using a loop
with open("WEEK9/Stuff.txt","r") as file:
    for line in file:
        print(line)

#Appending to a file (Adding to a file)
#appending adds to the end of a file without deleting whats already there
with open("WEEK9/Stuff.txt","a") as file:
    file.write("\n")
    file.write("THIS should appear at the very end, cause we used mode A")

#we use r mode to verify if a file exists
