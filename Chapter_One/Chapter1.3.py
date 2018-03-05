# coding=utf-8
import cPickle as  pickle

# coding=utf-8
# IO  and  Serialization
# Reader

try:
    # open file
    f = open('/Users/Mike/Documents/Android/DBB_RASP的2.5.7/codesign/mapping.txt', 'r')
    # read file
    print f.read()
finally:
    if f:
        f.close()

# To Simplify try...finally
with open('/Users/Mike/Documents/Android/DBB_RASP的2.5.7/codesign/mapping.txt', 'r') as fileReader:
    print(fileReader.read())

# Reader bigger DOC with for
with open('/Users/Mike/Documents/Android/DBB_RASP的2.5.7/codesign/mapping.txt', 'r') as fileReaderWithFor:
    for line in fileReaderWithFor.readlines():
        print('-' + line.strip())

# Write

with open('/Users/Mike/PycharmProjects/PyCrawer/Chapter_One/TestReaderFile', 'w') as fileWrite:
    fileWrite.write('Tom And Jerry')

# Serialization

d = dict(url='http://www.baidu.com', title='BaiDu', content='MainPager')
f = open('/Users/Mike/PycharmProjects/PyCrawer/Chapter_One/TestReaderFile', 'w')
pickle.dump(d, f)
f.close()

f = open('/Users/Mike/PycharmProjects/PyCrawer/Chapter_One/TestReaderFile', 'rb')
read = pickle.load(f)
f.close()
print(read)
