def solution(s):
    for length in range(1, len(s)):
        pattern = s[0:length + 1]

        for count in range(length, len(s), length):
            iter = s[(count * length):((count + 1) * length + 1)]
            print((count * length), ((count + 1) * length + 1)))
            if pattern == iter:
                print(pattern)
            else:
                break


solution("abccbaabccbaabccba")
