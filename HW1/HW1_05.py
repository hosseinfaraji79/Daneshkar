
user_input = int(input("How many laptops do you want to compare?  "))

laptops = {}

for laptop in range (user_input):
    print("Laptop number", laptop+1, "cost: ", end='')
    input_cost = int(input())
    print("Laptop number", laptop+1, "quality: ", end='')
    input_quality = int(input())
    laptops.update({input_cost:input_quality})

costs = sorted(laptops.keys())
flag = False
for i in range (len(laptops)-1):
    if laptops[costs[i]] >= laptops[costs[i+1]]:
        flag = True
        break

print("Not Founded" if flag == False else "Founded")