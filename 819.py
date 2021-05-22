class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        removed = ''.join([ch.lower() if ch.isalnum() else ' ' for ch in paragraph])
        words = removed.split()
        counter = collections.Counter(words)
        for word, _ in counter.most_common():
            if word not in banned:
                return word