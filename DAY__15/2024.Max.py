class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest(target: str) -> int:
            flips = 0
            max_count = 0
            left = 0

            for right in range(len(answerKey)):
                if answerKey[right] == target:
                    flips += 1
                while flips > k:
                    if answerKey[left] == target:
                        flips -= 1
                    left += 1
                max_count = max(max_count, right - left + 1)

            return max_count

        case1 = longest("F")
        case2 = longest("T")

        return max(case1, case2)

