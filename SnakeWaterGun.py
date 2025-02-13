import random
def game():
    list1=["Snake","Water","Gun"]
    
    
    computer=random.choice(list1)
    user=input("ENter your choice: ")
    if computer=="Snake":
        if user=="S":
            print("Match draw")
            return
        elif user=="W":
            print("You loose")
            return
        else:
            print("You win")
            return
    elif computer=="Water":
        if user=="S":
            print("You win")
            return
        elif user=="W":
            print("Match draw")
            return
        else:
            print("You loose")
            return
    else:
        if user=="S":
            print("You loose")
            return
        elif user=="W":
            print("You win")
            return
        else:
            print("Match draw")
            return
time=int(input("How many time you want to play: "))
while(time>0):
    game()
    time-=1

    