import random 

user_wins = 0
pc_wins = 0
draws = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_answer = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_answer == "q":
        break
    
    if user_answer not in options:
        continue

    random_num = random.randint(0,2)
    #rock:0, paper:1, scissors:2

    pc_pick = options[random_num]
    print(f"Computer picked {pc_pick}.")

    if user_answer == 'rock' and pc_pick == 'scissors':
        print("You won!")
        user_wins += 1
        continue
    
    elif user_answer == 'paper' and pc_pick == 'rock':
        print("You won!")
        user_wins += 1
        continue

    elif user_answer == 'scissors' and pc_pick == 'paper':
        print("You won!")
        user_wins += 1
        continue 

    elif user_answer == pc_pick:
        print("Its a draw.")
        draws += 1

    else:
        print("You lost!")
        pc_wins += 1

print(f"You won {user_wins} times.")
print(f"The PC won {pc_wins} times.")

if draws >= 1:
    print(f"DRAWS : {draws}")





    


