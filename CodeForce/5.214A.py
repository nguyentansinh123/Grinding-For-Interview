def read_input():
    num = list(map(int, input().split()))
    return num


def main():
    n, m = map(int, input().split())

    count = 0

    for a in range(int(n**0.5) + 1):
        b = n - a**2
        if b >= 0 and a + b**2 == m:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
