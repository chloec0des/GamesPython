playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Yay! Let's play! ")

score=0

q1= input("what does CPU stands for? ").lower()
if q1 == "central processing unit":
    print("correct! ")
    score+=1
    print(f'score: {score}')
else: 
    print("incorect!")

q1= input("what does GPU stands for? ").lower()
if q1 == ("graphic processing unit"):
    print("correct! ")
    score+=1
    print(f'score: {score}')
else: 
    print("incorect!")

q1= input("what does PSU stands for? ").lower()
if q1 == "power supply" or "power supply unit":
    print("correct! ")
    score+=1
    print(f'score: {score}')
else: 
    print("incorect!")

q1= input("what does RAM stands for? ").lower()
if q1 == "random access memory":
    print("correct! ")
    score+=1
    print(f'score: {score}')
else: 
    print("incorect!")

print(f'Your total score is {score}.' + "You got" + str(score) + "questions correct")
#if we want to display the score in percentage, you would write:
#str(score/ (number of questions)*100)
