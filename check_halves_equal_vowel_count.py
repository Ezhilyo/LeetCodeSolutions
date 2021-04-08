class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l_count = 0
        for i in range(0, int(n / 2)):
            if s[i] in vowels:
                l_count += 1

        r_count = 0
        for i in range(n // 2, n):
            if s[i] in vowels:
                r_count += 1

        print(l_count)
        print(r_count)

        return l_count == r_count
