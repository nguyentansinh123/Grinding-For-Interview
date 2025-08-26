def read_input():
    problems = list(map(int, input().split()))
    return problems


def main():
    shoes = read_input()
    un_shoe = set(shoes)

    print(4 - len(un_shoe))

    return 4 - len(un_shoe)


if __name__ == "__main__":
    main()
