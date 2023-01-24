import os


def find_files(path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    found = list()

    if not os.path.exists(path):
        return found

    current = os.listdir(path)

    for file in current:
        filepath = (f"{path}/{file}")
        if os.path.isfile(filepath):
            found.append(filepath)
        if os.path.isdir(filepath):
            files = find_files(filepath)
            found.append(files)

    return found

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files("./testdir/subdir1"))

# Test Case 2
print(find_files("./testdir"))

# Test Case 3
print(find_files(" "))

# Test Case 4
print(find_files("./fake/path"))
