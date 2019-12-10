import os
import Calculate_file_checksum
def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    print(exits)
    dups = {}

    if exits:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:" + dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = Calculate_file_checksum.hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                    print("Append")
                else:
                    dups[file_hash] = [path]

                    print("ADDDD")
        return dups
    else:
        print("Invalid Path")
