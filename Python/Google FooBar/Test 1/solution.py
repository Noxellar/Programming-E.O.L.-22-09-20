def solution(s):
    # Generate a list of factors from length of string
    list = [factor for factor in range(1, len(s) + 1) if len(s) % factor == 0]

    for factor in list:
        # Possible pattern configuration
        pattern = s[0:factor]
        # Maximum number of iterations possible without going
        # past string length
        max_iter = int(len(s) / factor)

        # Loop through the string and compare with
        # possible configuration
        for count in range(1, max_iter):
            # Splicing from factor * count
            # Don't want to compare configuration with itself
            iter_text = s[factor * count:factor * (count + 1)]

            if pattern != iter_text:
                # Exit loop immediately if match doesn't work
                break
        else:
            # If all iterations are the same, return max number
            # of cake slices
            return max_iter
    else:
        # Code is set not to compare configuration with itself
        # So if the M&Ms are "abcdefg" then it won't work
        # Just return whole string back
        return s
