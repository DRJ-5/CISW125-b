inventory={
    "apples":5,
    "bananas":7,
    "oranges":4,
    "greek yogurt":11,
    "almonds":65,
}
print(inventory.keys())
inventory["grapes"]=8
inventory["apples"]+=5
print(inventory.keys())
print(inventory.values())
for inventory, values in inventory.items():
 print(f"{inventory}: {values}")





customer={
"person1": {
"name":"jason",
"items bought":["banana","almonds"],
"total spent":50.00
},

"person2": {
"name":"Cassandra",
"items bought":"orange",
"total spent":7.00
 },

}

print(customer["person1"]["items bought"])