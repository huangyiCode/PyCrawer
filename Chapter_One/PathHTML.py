# pattern
import re

# the 'r' means the following just a string.

pattern = re.compile(r'\d+')
result = pattern.match('aa123')
if result:
    print result.group()
else:
    print 'match defeat'

search = re.search(pattern, 'aa123')
if search:
    print search.group()
else:
    print 'search defeat'

patternSplit = re.compile(r'\d')
split = re.split(pattern, 'bb1bbabb2babbbabb3ba')
print split
