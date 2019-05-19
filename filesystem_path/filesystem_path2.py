from typing import Dict, List

# https://leetcode.com/problems/longest-absolute-file-path/

def getPath(fs: Dict, path_str: str):
    """
    Navigate in dictionary representing filesystem to 
    path represented by path_str
    """
    if not path_str:
        return fs
    subs = path_str.split("/")
    d_ret = fs
    for sub_i in subs:
        d_ret = d_ret[sub_i]
    return d_ret

def newPath(path1: str, path2: str) -> str:
    """
    Append path1 and path2 a new path.
    """
    if not path1:
        char = ''
    else:
        char = '/'
    return path1 + char + path2

def getFilesystemDict(S: str) -> List[str]:
    """
    Get dictionary representation of filesystem.
    """
    # Constuct several different paths
    paths = S.split('\n')
    # Dictionary represents nested paths
    fs = dict()
    # Maintain previous paths and tabs as stack
    dirs = ['']
    dirs_tabs = [-1]
    # List of file paths
    file_paths = list()
    # Iterate through sub-paths
    for i, path in enumerate(paths):
        tabs = path.count('\t')
        path = path.replace('\t', '')
        is_file = "." in path
        # Shallower or equal level
        if tabs <= dirs_tabs[-1]:
            while tabs <= dirs_tabs[-1]:
                dirs.pop()
                dirs_tabs.pop()
        path_above = getPath(fs, dirs[-1])
        new_path = newPath(dirs[-1], path)
        # Path represents a file; add to file paths
        if is_file:
            file_paths.append(new_path)
        # Path represents a directory; value is dict
        else:
            path_above[path] = dict()
            dirs.append(new_path)
            dirs_tabs.append(tabs)
    return file_paths

def getLenLongestStr(strs: List[str]) -> List[str]:
    """
    Get longest string in list of strings. 
    """
    L = dict()
    for s in strs:
        L[s] = len(s)
    if not L: # Empty sequence
        return 0
    longest = max(L, key=lambda k: L[k])
    return L[longest]

def longestPath(S: str) -> int:
    """
    Get length of longest path in filesystem represented by S.
    """
    # No files -> return zero
    if not S.count('.'):
        return 0
    # Only a single path with a file -> return its length
    if not S.count('\t') and not S.count('\n'):
        return len(S)
    file_paths = getFilesystemDict(S)
    longest = getLenLongestStr(file_paths)
    return longest

class Solution:
    def lengthLongestPath(self, S: str) -> int:
        return longestPath(S)
