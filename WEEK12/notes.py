#Lists: Storing multiple values in order


#Index a list ?
#Indexing a list just means to target a specific value from the list
# print(favgames[0])
# print(favgames[1])
# print(favgames[2])

# #Using Len() with a list
# #We can use Len() to find out how many total items are in a list
# print(len(favgames))

#adding items to a list
#append() adds to the end of the list
# insert() adds an item at a specific position
# favgames.append("Dark Souls")


# #Inserting into a list
# favgames.insert(0,"Marvel Rivals")
# print(favgames)

#Common List methods

#Count(), counts how many times a value appears
#remove(), removes a specific item
#sort(), puts the list in a sorted order
#reverse(), flips the current order of the list



#Count example
#favgames.count("List item you want counted")

#Remove Example
# favgames.remove("Mario Kart")
# favgames.remove("Mario Kart")
# print(favgames)


#Sort example
# favgames.sort()
# print(favgames)

#Reverse Example
# favgames.reverse()
# print(favgames)

# favgames=["Halo","Mario Kart", "Elden Ring","Mario Kart"]

# #loop through the items within my list
# for games in favgames:
# print(games)





#Dictionaries: Storing labeled information
#A dictionary stores data in key value pairs
#Dictionaries are useful when a label matters more than a position


#make a dictionary that is called player_stats
player_stats={
#Dictionary values must be health, mana, level, gold
# word:value
"Health": 100,
"Mana": 40,
"Level":15,
"Gold": 25
}

#Lists vs Dictionaries
#Use a list when order matters and you want a collection of items
#Dictionary is used when labels matter and you want to look things up by name


#Accessing a dictionary?
# print(player_stats["Health"])


#Add and update dictionary values ?
#You can add a new key-value pair by assigning a value to a new key
#You can also update an existing value or increase it


# player_stats["Strength"]=15
# player_stats["Health"]=200
# player_stats["Health"]+=50
# print(player_stats)


#Keys() and Values()

#keys() show all dictionary values
#Values() shows all dictionary values

print(player_stats.keys())
print(player_stats.values())

#How we can loop through our dictionaries?
#We can loop through the keys or the values or both
#Items() is often the most readable way to show everything in a dictionary

#Loop through the keys
for stats in player_stats.keys():
    print(stats)

# #Loop through the values
for values in player_stats.values():
    print(values)

#Loop through both keys and values
for stats, values in player_stats.items():
    print(f"{stats}: {values}")

#Nested Dictionaries
students={
"Blue eyes white dragon":{
"Name": "Ana",
"Major": "Programming",
"Credits": 6

}


}

#Access nested dictionary Values?
#To access nested data, go one level at a time
#File directories

#print(students["002"]["Major"])


#Nested structures can mix lists and dictionaries
#Programs oftern combine multiple data structures together
#An inner dictionary can contain a list as one of its values

students={
"005":{
"Name":"Sebastian",
"Classes":["Math","Hacking","Linux"],
"GPA":2.8
}

}


print(students["005"]["GPA"])