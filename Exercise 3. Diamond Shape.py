def print_diamond():
# Prompts user for odd integer input.
    n = int(input("Enter an odd integer: "))
# Error tracking for non-odd integer input.
    if n % 2 == 0:
        print ("Please enter an odd integer.")
        return

# Creates the upper part of the diamond that covers line 1 to line 3.
    for i in range(n // 2 + 1):
        spaces, stars = n // 2 - i, i * 2 + 1
        print(' ' * spaces + '*' * stars)
        
# Creates the lower part of the diamond that covers line 4 to line 5
    for i in range(n // 2 - 1, -1, -1):
        spaces, stars = n // 2 - i, i * 2 + 1
        print(' ' * spaces + '*' * stars)

print_diamond()
        