def fill_in_blank():
    print("Answer the question below.")
    with open("Project4/question.txt", "r") as file:
     contents=file.read()
    print(contents)
    
    answer = input("What is your answer? ")
    if answer == "Mount Everest".lower():
        print("Answer was correct!")
    else:
        print (f"Wrong answer, the correct answer is Mount Everest. Your answer was {answer}")

fill_in_blank()