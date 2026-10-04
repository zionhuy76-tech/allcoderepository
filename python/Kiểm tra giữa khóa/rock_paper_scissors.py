#=================================
# Rock Paper Scissors Lizard Spock
#=================================

import random


print("Rock Paper Scissors Lizard Spock")

weapons = {
    1: "🤚",   # Rock
    2: "✋",   # Paper
    3: "✌️",   # Scissors
    4: "🦎",   # Lizard
    5: "🖖",   # Spock
}

print("Welcome to Rock Paper Scissors Lizard Spock!")
print(f"1) {weapons[1]}")
print(f"2) {weapons[2]}")
print(f"3) {weapons[3]}")
print(f"4) {weapons[4]}")
print(f"5) {weapons[5]}")

# Các cặp (A, B) nghĩa là A thắng B
win_conditions = [
    (3, 2), 
    (2, 1),  
    (1, 4),  
    (4, 5),  
    (5, 3),
    (3, 4), 
    (4, 2), 
    (2, 5), 
    (5, 1),  
    (1, 3), 
]

You = int(input("Pick a number: "))
Robot = random.randint(1, 5)

print(f"You chose: {weapons[You]}")
print(f"Robot chose: {weapons[Robot]}")

if You == Robot:
    print("It's a tie!")
elif (You, Robot) in win_conditions:
    print("You win!")
else:
    print("Robot wins!")