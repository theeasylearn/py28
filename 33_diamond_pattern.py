'''# Diamond pattern using asterisks
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n = 5  # Size of the diamond
# Top half of the diamond
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Bottom half of the diamond
for i in range(n - 1, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
