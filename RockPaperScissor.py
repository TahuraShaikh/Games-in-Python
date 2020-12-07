import random
#  Rock Paper Scissors game
def game(comp, you):
    # When two values are equal, declare a tie!
    if comp == you:
        return None

    # for all possibilities if computer choose r
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    # for all possibilities if computer choose p
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    # for all possibilities if computer choose s
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Computer Turn: Rock(r), Paper(p) or Scissor(s)?")
num = random.randint(1, 3)
if num == 1:
    comp = 'r'
elif num == 2:
    comp = 'p'
elif num == 3:
    comp = 's'

you = input("Your Turn: Rock(r), Paper(p) or Scissor(s)?")
a = game(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")