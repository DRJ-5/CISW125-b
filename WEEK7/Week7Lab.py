number=[1,5]
for number in range(1,6):
        print(number)



age=int(input("Enter your age: "))
while age <1 or age >65:
        print("Invalid age ")
        age=int(input("Enter your age: "))
print("You are at an appropriate age")



item=["Bananas", "Oranges", "Power Drill"]
for item in item:
        print(item)




for number in range(2,8):
        print(number)


for number in range(2,8):
    square=number*number
    print(square)


name="Alonzo Juarez Estrada Gallardo Sanchez"
for letter in name:
       print(letter)


for number in range(5,20):
       print (number)
       if number==17:
              break



for number in range(1,4):
       for number2 in range(1,4):
              print(number,number2)