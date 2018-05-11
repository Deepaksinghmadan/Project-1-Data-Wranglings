import re
    re.findall('.', 'abcd')   # match any character
    ['a', 'b', 'c', 'd']
    re.findall('^a', 'abcd')  # match only if 'a' is at start of line
    ['a']
    re.findall('^d$', 'abcd') # match if 'd' is the only character in a line.
    []