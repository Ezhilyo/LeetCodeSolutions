from typing import List


class Solution:
    asd = []

    def get_combinations(self, num_dict, digits, temp):

        if digits == "":
            self.asd.append("".join(temp))
            return

        for letter in num_dict[int(digits[0])]:
            temp.append(letter)
            new_digits = digits[1:len(digits)] if len(digits) > 1 else ""
            self.get_combinations(num_dict, new_digits, temp)
            temp.pop()

    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        self.asd = []

        num_dict = {}

        num_dict[2] = "abc"
        num_dict[3] = "def"
        num_dict[4] = "ghi"
        num_dict[5] = "jkl"
        num_dict[6] = "mno"
        num_dict[7] = "pqrs"
        num_dict[8] = "tuv"
        num_dict[9] = "wxyz"

        self.get_combinations(num_dict, digits, [])

        a = self.asd

        self.asd = []

        return a

