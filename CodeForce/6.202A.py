def largest_palindromic_subsequence(s: str) -> str:
    max_char = max(s)
    count = s.count(max_char)
    print(max_char * count)
    return max_char * count


largest_palindromic_subsequence(input())

