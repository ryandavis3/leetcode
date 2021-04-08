from typing import Dict, List
from collections import Counter

def empty(collection):
    for _, ct in collection.items():
        if ct > 0:
            return False
    return True


def numTilePossibilities(tiles: str) -> int:
    
    count = dict(Counter(tiles))
    
    def backtrack(string: str, collection: Dict) -> List[str]:
        
        if empty(collection):
            return [string]

        sub = []
        for char, _ in collection.items():
            sub += [string + char]
        
        for char, ct in collection.items():
            coll_sub = collection.copy()
            coll_sub[char] -= 1
            if coll_sub[char] == 0:
                del coll_sub[char]
            sub += backtrack(string+char, coll_sub)

        return sub

    substrings = backtrack("", count)
    return len(set(substrings))


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return numTilePossibilities(tiles)


if __name__ == "__main__":
    tiles = "AAB"
    result1 = numTilePossibilities(tiles)
    tiles = "AAABBC"
    result2 = numTilePossibilities(tiles)
