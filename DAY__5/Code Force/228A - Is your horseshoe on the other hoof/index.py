
def shoeToBuy():
    hash = {}

    arr = list(map(int, input().split()))
    count = 0 

    for i in range(len(arr)):

        if arr[i] in hash:
            count +=1 
        else:
            hash[arr[i]] = 1 
    
    print(count)

if __name__ == "__main__":
    shoeToBuy()