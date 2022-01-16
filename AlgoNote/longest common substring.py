def longest_substring(s1, s2):  # O(n^2)
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s2) == 0:
        return 0
    max_len = 0
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            j = i
            while j < len(s1) and s1[j] == s2[0]:
                j += 1
            if j - i > max_len:
                max_len = j - i
    return max_len


def main():
    print(longest_substring('abcde', 'ace'))
    print(longest_substring('abc', 'abc'))
    print(longest_substring('abc', 'def'))
    print(longest_substring('abc', 'cde'))
    print(longest_substring('abc', 'c'))
    print(longest_substring('abc', 'abcd'))
    print(longest_substring('abc', 'ab'))
    print(longest_substring('abc', 'b'))
    print(longest_substring('abc', 'a'))
    print(longest_substring('abc', ''))
    print(longest_substring('', 'abc'))
    print(longest_substring('', ''))


if __name__ == '__main__':
    main()
