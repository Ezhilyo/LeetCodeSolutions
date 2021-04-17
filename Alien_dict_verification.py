class Solution:

    def is_sorted(self, word1, word2):
        min_length = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(0, min_length):
            if self.rank[word1[i]] < self.rank[word2[i]]:
                return True
            elif self.rank[word1[i]] > self.rank[word2[i]]:
                return False
        return len(word1) <= len(word2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.rank = {}
        max_length = max([len(word) for word in words])
        i = 0
        for alpha in order:
            self.rank[alpha] = i
            i += 1
        for i in range(0, len(words) - 1):
            if not self.is_sorted(words[i], words[i + 1]):
                return False
        return True
