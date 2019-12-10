import sys
import time
import os
import Find_dup_files
import Delete_Files
import os, pathlib


def main():
    print("Delete repeted files from root..........")
    print("Application name:" + sys.argv[0])

    if len(sys.argv) != 2:
        print("Error : Invalid number of arguments")
        exit()
    if sys.argv[1] == "-h" or sys.argv[1] == "_H":
        print("This Script is used to traverse specific diretory and display checksum of files")
        exit()
    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory Extention")
        exit()
    try:
        brr = {}
        arr = {}
        startTime = time.time()
        #os.getpid()
        #print("OS getpid",os.path.abspath(''))
        #print("OS path",os.path.abspath(os.sep))
        #print("OS222",os.getcwd())
        #relpath=os.path.abspath(os.sep)
        #print("relpath",relpath)
        #print("root===",os.system('set systemroot'))
        #print(os.path.expandvars("%SystemRoot%"))     # work on windows
        home = pathlib.Path(os.path.expanduser("~"))
        print(home.drive)

        #my_path = pathlib.Path(pathlib.Path.home())  # this is work on windows as well as linux
        #print("my_path",my_path.drive)
        arr = Find_dup_files.findDup(home.drive)
        print("arr===",arr)
        #Delete_Files.DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.' % (endTime - startTime))


    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input", E)
    # file.close()


if __name__ == "__main__":
    main()
