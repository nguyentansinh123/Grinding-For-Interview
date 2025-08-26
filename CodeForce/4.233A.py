def read_input():
    num = int(input())
    return num


def main():
    myNum = read_input()
    l = 1

    if myNum % 2 != 0:
        print(-1)
        return
    else:
        arr = list(range(myNum + 1))

        for r in range(2, len(arr), 2):
            arr[l], arr[r] = arr[r], arr[l]
            l += 2
        for i in range(1, len(arr)):
            print(arr[i])
        return


if __name__ == "__main__":
    main()
