def do_default(score):
    print("This is a poor result.")

def do_two(score):
    print("This is an acceptable result.")

def do_three(score):
    print("This is a very good result.")

def do_four(score):
    print("This is an excellent result.")

print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    print("Exiting quiz...")
    quit()

print("Sure lets play!!")
score = 0

answer = input("What does CPU stand for? ->")
if answer.lower() == "central processing unit":
    print('-Correct!')
    score += 1
else:
    print('-Incorrect!')

answer = input("What does GPU stand for? ->")
if answer.lower() == "graphics processing unit":
    print('-Correct!')
    score += 1
else:
    print('-Incorrect!')

answer = input("What does RAM stand for? ->")
if answer.lower() == "random access memory":
    print('-Correct!')
    score += 1
else:
    print('-Incorrect!')

answer = input("What does PSU stand for? ->")
if answer.lower() == "power supply unit":
    print('-Correct!')
    score += 1
else:
    print('-Incorrect!')


print(f"You got {score} questions correct with an accuracy of {(score/4)*100}%.")

remarks = {2: do_two, 3: do_three, 4: do_four}
remark = remarks.get(score, do_default)
remark(score)

