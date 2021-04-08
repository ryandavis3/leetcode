from typing import List, Dict
from collections import Counter

def hashd(d: Dict) -> str:
    s = ""
    for k, v in d.items():
        s += k
        s += str(v)
    return s


def minStickers(stickers: List[str], target: str) -> int:

    s = set("".join(stickers))
    tg = set(target)
    if len(tg - s) > 0:
        return -1

    stickers_letters = [dict(Counter(w)) for w in stickers]
    target_letters = dict(Counter(target))

    memo = {}

    def backtrack(N: int, t: Dict[str, int]):
   
        t = {k: v for k, v in t.items() if v > 0}

        key = (N, hashd(t)) 
        if key in memo:
            return memo[key]

        # Remove cases with zero letters
        if len(t) == 0:
            return 0
    
        sub = []
        for word in stickers_letters:
            tc = t.copy()
            if len(set(word) & set(tc)) == 0:
                continue
            for letter, _ in tc.items():
                if letter in word:
                    tc[letter] = max(tc[letter] - word[letter], 0)
            sub += [1 + backtrack(N+1, tc)]
        result = min(sub)
        memo[key] = result
        return min(sub)

    return backtrack(0, target_letters)


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        return minStickers(stickers, target)


if __name__ == "__main__":
    stickers = ["with", "example", "science"] 
    target = "thehat"
    result = minStickers(stickers, target)
    print(result)
    stickers = ["notice", "possible"] 
    target = "basicbasic"
    result1 = minStickers(stickers, target)
    print(result1)
    stickers = ["slave","doctor","kept","insect","an","window","she","range","post","guide"]
    target = "supportclose"
    result2 = minStickers(stickers, target)
    print(result2)
    stickers = ["love","color","dollar","son","feet","held","star","still","children","wonder","sell","city","law","eye","loud","prepare","opposite","except","should","music","tell","white","several","roll","then","we","oil","led","huge","act","but","coast","warm","five","atom","world","hand","cool","lost","these","plain","solution","bird","leave","turn","pick","mouth","voice","root","original"]
    target = "feltmillion"
    result3 = minStickers(stickers, target)
    print(result3)
    stickers = ["right","ten","year","share","period","paper","expect","village","home","happen","ring","sat","even","afraid","paint","self","range","camp","note","read","paragraph","run","basic","fill","week","his","star","power","any","colony","object","free","dark","said","chick","true","glad","child","room","lost","am","cry","quiet","crease","while","race","fun","found","dream","once"]
    target = "materialhalf"
    result4 = minStickers(stickers, target)
    print(result4)
