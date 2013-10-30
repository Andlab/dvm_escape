import os
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python %s <message>'
        exit(1)
    
    s = sys.argv[1]
    for x in xrange(0, len(s), 100):
        os.system('adb shell input text ' + s[x:x+100])