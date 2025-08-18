n, k = map(int, input().split())

scores = list(map(int, input().split()))

validScore = scores[k -1]
res = 0
for i in range(len(scores)):
    if scores[i] >= validScore and scores[i] != 0:
        res += 1

print(res) 