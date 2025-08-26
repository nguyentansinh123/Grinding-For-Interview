def read_input():
    n = int(input())
    problems = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        problems.append((a, b, c))
    return n, problems


def main():
    n, problems = read_input()
    res = 0
    for i in range(n):
        if sum(problems[i]) < 2:
            continue
        else:
            res += 1
    print(res)
    return res


if __name__ == "__main__":
    main()

