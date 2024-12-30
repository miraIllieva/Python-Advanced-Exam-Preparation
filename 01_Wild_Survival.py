
from collections import deque

bees = deque(int(x) for x in input().split()) 
bee_eaters = [int(x) for x in input().split()] 

bees_killer = 7

while bees and bee_eaters:
    current_bees = bees.popleft()  
    current_eaters = bee_eaters.pop()

    while current_bees > 0 and current_eaters > 0:
        current_bees -= bees_killer
        if current_bees >= 0 :
            current_eaters -= 1
    
    if current_bees > 0:
        bees.append(current_bees)
    elif current_eaters > 0:
        bee_eaters.append(current_eaters)

print("The final battle is over!")

if bees:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")
else:
    print("But no one made it out alive!")
