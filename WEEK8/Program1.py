#Had to search up a loop that would repeat until the right input was entered which was "while true"
while True:
    answer = input("What is 4 + 4?: ")
    if answer == "8":
        print ("Correct")
        break
    print("Wrong answer try again")
        