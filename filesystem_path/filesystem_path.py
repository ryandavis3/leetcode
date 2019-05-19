from typing import Dict

# https://leetcode.com/problems/longest-absolute-file-path/

S = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
S = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

paths = S.split('\n')

fs = dict()

def getPath(fs: Dict, path_str: str):
    """
    Navigate in dictionary representing filesystem to 
    path represented by path_str
    """
    subs = path_str.split("/")
    d_ret = fs
    for sub_i in subs:
        d_ret = d_ret[sub_i]
    return d_ret

def getFilesystemDict(S: str) -> Dict:
    """
    Get dictionary representation of filesystem.
    """
    # Constuct several different paths
    paths = S.split('\n')
    fs = dict()
    # Maintain previous paths as stack
    prev_paths = list()
    prev_tabs = list()
    # List of file paths
    file_paths = list()
    # Iterate through sub-paths
    for i, path in enumerate(paths):
        print(prev_tabs)
        print(prev_paths)
        tabs = path.count('\t')
        print(path)
        print(tabs)
        path = path.replace('\t', '')
        is_file = "." in path
        if not i:
            fs[path] = dict()
            prev_dir = path
            prev_paths.append(path)
            prev_tabs.append(0)
            continue
        # Deeper level
        if tabs > prev_tabs[-1]:
            # A file; value is None
            path_above = getPath(fs, prev_paths[-1])
            if is_file:
                path_above[path] = None
                file_paths.append(prev_paths[-1] + '/' + path)
            # Not a file; value is dict
            else:
                path_above[path] = dict()
                prev_paths.append(prev_paths[-1] + '/' + path)
                prev_tabs.append(tabs)
        # Same level
        elif tabs == prev_tabs[-1]:
            if is_file:
                path_above = getPath(fs, prev_paths[-1])
                path_above[path] = None
                file_paths.append(prev_paths[-1] + '/' + path)
            # Not a file; value is dict
            else:
                path_above = getPath(fs, prev_paths[-1])
                path_above[path] = dict()
                prev_paths.append(prev_paths[-1] + '/' + path)
            prev_tabs.append(tabs)
        # Shallower level
        elif tabs < prev_tabs[-1]:
            while tabs <= prev_tabs[-1]:
                prev_paths.pop()
                prev_tabs.pop()
            if is_file:
                path_above = getPath(fs, prev_paths[-1])
                path_above[path] = None
                file_paths.append(prev_paths[-1] + '/' + path)
            # Not a file; value is dict
            else:
                path_above = getPath(fs, prev_paths[-1])
                path_above[path] = dict()
                prev_paths.append(prev_paths[-1] + '/' + path)
            prev_tabs.append(tabs)
    return [fs, file_paths]


def getFilesystemDict2(S: str) -> Dict:
    """
    Get dictionary representation of filesystem.
    """
    # Constuct several different paths
    paths = S.split('\n')
    fs = dict()
    # Maintain previous paths as stack
    prev_paths = list()
    prev_tabs = list()
    # List of file paths
    file_paths = list()
    # Iterate through sub-paths
    for i, path in enumerate(paths):
        tabs = path.count('\t')
        path = path.replace('\t', '')
        is_file = "." in path
        if not i:
            fs[path] = dict()
            prev_dir = path
            prev_paths.append(path)
            prev_tabs.append(0)
            continue
        # Shallower level
        if tabs < prev_tabs[-1]:
            while tabs <= prev_tabs[-1]:
                prev_paths.pop()
                prev_tabs.pop()
        path_above = getPath(fs, prev_paths[-1])
        # Path represents a file; add to file paths 
        if is_file:
            file_paths.append(prev_paths[-1] + '/' + path)
        # Path represents a directory; value is dict
        else:
            path_above[path] = dict()
            prev_paths.append(prev_paths[-1] + '/' + path)
            prev_tabs.append(tabs)

    return [fs, file_paths]
