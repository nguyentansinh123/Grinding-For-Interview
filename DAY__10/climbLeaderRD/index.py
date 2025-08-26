def climbingLeaderboard(ranked, player):
    unq_rank = sorted(set(ranked), reverse=True)
    result = []
    n = len(unq_rank)

    for point in player:
        l, r = 0, n

        while l < r:
            middle = (l + r) // 2

            if unq_rank[middle] <= point:
                r = middle
            else:
                l = middle + 1
        result.append(l + 1)
    return result


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5]
print(climbingLeaderboard(ranked, player))
