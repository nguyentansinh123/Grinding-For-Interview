
def equations():
    n, m = map(int, input().split())
    count = 0

    for a in range(0, 101):  
        for b in range(0, 101):
            if a*a + b == n and a + b*b == m:
                count += 1
    print(count)


if __name__ == "__main__":
    equations()