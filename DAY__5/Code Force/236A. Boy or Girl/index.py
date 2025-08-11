
def BoyOrGirl():

    username = input().lower()
    store = []

    for i in range(len(username)):
        if username[i] in store:
            continue
        else:
            store.append(username[i])
    if len(store) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")



if __name__ == "__main__":
    BoyOrGirl()