import os
import Calculate_file_checksum
import time


def findDup(path, file="Log"):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    print(exits)
    dups = {}

    if not os.path.exists(file):
        try:
            os.mkdir(file)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(file, " file %s.log" % (time.time()))
    f = open(log_path, 'w')

    if exits:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:" + dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = Calculate_file_checksum.hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                    #print("Append")
                else:
                    dups[file_hash] = [path]
                    #print("ADDDD")


        f.write(dups+"\n")
        f.write("\n")
        f.close()
        return dups
    else:
        print("Invalid Path")
