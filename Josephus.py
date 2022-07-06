from datetime import datetime 

# Set the number of people in the seats
number_of_people = 20000

# Luke's power version

started_at = datetime.now()
print(f"now = {started_at}")
i = 0
closest_power = 0
while (pow(2, i) <= number_of_people):
    closest_power = pow(2, i)
    i = i + 1
    
winner = (number_of_people - closest_power) * 2 + 1
duration = datetime.now() - started_at
print(f"The winner is {winner} in {duration} (optimised version)")


started_at = datetime.now()
# Brute force game playing version
people = list(range(1, number_of_people + 1))

while len(people) > 1:
    for index, value in enumerate(people):
        
        # Figure out who the next victim is going to be
        if (index < len(people) - 1):
            victim = people[index + 1]            
        else:
            victim = people[0]
            
        #print(str(value) + " is about to murder " + str(victim))
        people.remove(victim)

original_winner = people[0]
duration = datetime.now() - started_at
print(f"{original_winner} is still alive in {duration} (original version)")
