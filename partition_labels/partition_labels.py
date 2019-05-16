def strToDict(s: str) -> dict:
    """
    Convert string to dictionary. Keys are characters
    and values are lists of indices where the character
    appears.
    """
    d = dict()
    for i, char in enumerate(s):
        if char not in d:
            d[char] = list()
        d[char].append(i)
    return d

def getLetterExtend(letters: set, end_i: int, d: dict):
    """
    Get letter by which to extend substring. Return None
    if we do not need to extend substring.
    """
    for letter in letters:
        if d[letter][-1] > end_i:
            return letter
    return None

def getSmallestSubstring(start_i:int, s: str, d: dict) -> int:
    """
    Get smallest substring starting at start_i so all letters
    in substring appear only once in the larger string.
    """
    letter = s[start_i]
    end_i = d[letter][-1]
    substr = s[start_i:end_i+1]
    letter_miss = getLetterExtend(substr, end_i, d)
    while letter_miss is not None:
        end_i = d[letter_miss][-1]
        substr = s[start_i:end_i+1]
        letter_miss = getLetterExtend(substr, end_i, d)
    return end_i

def getPartitions(s: str):
    """
    Get legnths of partitions. 
    """
    l_partitions = list()
    d = strToDict(s)
    l = len(s)
    i = -1
    while i < l-1:
        j = getSmallestSubstring(i+1, s, d)
        l_partitions.append(j-i)
        i = j
    return l_partitions 


