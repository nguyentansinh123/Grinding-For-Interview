# Problem: Generate all strings of length n using characters 'a' and 'b'

# It’s basically the same as the binary string problem, but now with letters:

# Example:

# n = 2 → aa, ab, ba, bb


def generateString(n, currentStr):
    if n == len(currentStr):
        print(currentStr)
        return

    generateString(n, currentStr + "a")
    generateString(n, currentStr + "b")
