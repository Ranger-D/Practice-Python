print("This is just a simple game!")
tem = input("Please choose a number:")
answer = int(tem)
if answer == 6:
    print("Congratulations! You choose the right one!")
else:
    if answer > 6:
        print("You'd better choose a litter one.")
    else:
        print("You'd better choose a bigger one.")
print("Game Over!")