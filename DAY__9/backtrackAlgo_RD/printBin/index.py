# Print all binary strings of length n

# Example: n = 3 → 000, 001, 010, 011, 100, 101, 110, 111

# Goal: Recursively decide at each step whether to place 0 or 1.


def generate_binary(n, current=""):
    if n == len(current):
        print(n)
        return

    generate_binary(n, current + "0")

    generate_binary(n, current + "1")


n = 3
generate_binary(n)
