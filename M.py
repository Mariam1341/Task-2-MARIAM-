for row in range(7):
    for col in range(15):
        if col == 0 or col == 1 or col == 2 or col == 12 or col == 13 or col == 14:
            print("*", end="")
        elif row == 1 and (col == 4 or col == 5 or col == 9 or col == 10 ):
              print("*", end="")
        elif row == 2 and (col == 5 or col == 6 or col == 8 or col == 9 ):
              print("*", end="")
        elif row == 3 and col == 7 :
              print("*", end="")
        else:
            print( end=" ")
    print()