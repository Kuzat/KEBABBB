import sys
import urllib.request
import os

def main():
    if (len(sys.argv) >= 3):
        filename = sys.argv[1]
        directory = sys.argv[2]
        if not os.path.exists(directory):
            os.makedirs(directory)
        f = open(filename, "r")
        i = 0
        urls = f.readlines()
        for url in urls:
            filenameToCreate = directory + "/" + "{:08d}".format(i) + ".jpg"
            print(url)
            print(filenameToCreate)
            try:
                urllib.request.urlretrieve(url, filenameToCreate)
                i += 1
            except:
                print(url + " can't be downloaded")
    else:
        print("Arguments are missing")

#to run the program
#python3 scriptname.py filenameForData DirectoryNameToSavePictures
main()
