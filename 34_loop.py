# Hollow square with single asterisk in center
size = 7  # Size of the square (odd number for center)

for i in range(size):
    for j in range(size):
        # Print asterisk for border or center
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        elif i == size // 2 and j == size // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()