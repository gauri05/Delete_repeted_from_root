import hashlib

def hashfile(path, blocksize=1024):
    try:
        afile = open(path, 'rb')
        # print("PATH HH::::",path)
        hasher = hashlib.md5()

        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        # print("BUF   " + )
        afile.close()
        return hasher.hexdigest()
    except PermissionError as E:
        print(E)
    except Exception as EX:
        print(EX)
