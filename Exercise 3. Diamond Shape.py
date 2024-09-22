def print_diamond(n):
# Prompts user for odd integer input.
    if n % 2 == 0:
        print ("Please enter an odd integer. ")
        return
# Creates the upper part of the diamond that covers line 1 to line 3.
    for i in range(1, n, 2):
        print(" " * (n // 2 - i // 2), "*" * i)
# Creates the lower part of the diamond that covers line 4 to line 5
    for i in range(n, 0, -2):
        print(" " * (n // 2 - i // 2), "*" * i)

print_diamond(5)
        