name=input("What is your name? ")
print(name)

with open ("WEEK9/LAB.txt","a") as file:
    file.write(f"\n {name}")
