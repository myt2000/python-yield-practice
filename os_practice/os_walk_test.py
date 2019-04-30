import os
from os.path import join, getsize
def walk_test():
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end=" ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories