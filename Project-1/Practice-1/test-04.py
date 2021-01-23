print("This is just a simple game!")
tem = input("Please choose a number:")
answer = int(tem)
while answer != 6:
    if answer > 6:
        print("You'd better choose a litter one.")
    else:
        print("You'd better choose a bigger one.")
    tem = input("Please choose a number:")
    answer = int(tem)
print("Congratulations! You choose a right one")
print("Game Over!")