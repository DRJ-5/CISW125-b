with open ("WEEK9/LAB.txt","w",) as file:
  file.write("Hello this is the lab file txt")

with open ("WEEK9/LAB.txt","a") as file:
   file.write("\n I am from the future and adding some more txt\n What I came to warn you about is [CONNECTION LOST]")

with open("WEEK9/LAB.txt", "r") as file:
   contents=file.read()
   print(contents)


