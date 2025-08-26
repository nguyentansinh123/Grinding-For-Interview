def read_input():
    string = input()
    return string


def main():
    string = read_input()
    nwStr = set(string)

    if len(nwStr) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()
