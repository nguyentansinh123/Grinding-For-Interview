# Great! Let’s step it up a bit. Here’s a slightly harder backtracking problem that introduces more logic:

# Problem: Generate all strings of length n using 'a' and 'b', but no two 'a's can be adjacent

# Example:

# n = 3 → valid strings: bab, baa, abb, bba, bbb


def printString(n, currentStrg):
    if n == len(currentStrg):
        print(currentStrg)
        return

    if not currentStrg or currentStrg[-1] != "a":
        printString(n, currentStrg + "a")

    printString(n, currentStrg + "b")


printString(3, "")
