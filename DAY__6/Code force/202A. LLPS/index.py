def llpsCacl():
    myS = input().lower()

    impStr = max(myS)
    count = 0
    result = ""
    for i in myS:
        if i == impStr:
            count +=1
    
    for i in range(count):
        result += impStr
    print(result)
         

if __name__ == "__main__":
    llpsCacl()