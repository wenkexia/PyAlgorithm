import itertools


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        le = len(word)
        end = 0
        ans = 1
        tf = False

        def get(word):
            for j in itertools.cycle(word):
                yield j

        for i in list(sequence):
            if tf:
                if i == get_num.__next__():
                    ans += 1
                else:
                    end = ans // le if ans // le > end else end
                    tf, ans = False, 1
            else:
                if i == word[0]:
                    get_num = get(sequence)
                    get_num.__next__()
                    tf = True
        return end


S = Solution()
sequence = "ababc"
word = "ab"
print(S.maxRepeating(sequence, word))
