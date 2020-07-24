def solution(s):
    for length in range(1, len(s)):
        list = [i for i in range(1, len(s) + 1) if len(s) % i == 0]


solution("abccbaabccbaabccba")
