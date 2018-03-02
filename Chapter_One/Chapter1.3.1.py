# coding=utf-8

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
    print(f.read())
