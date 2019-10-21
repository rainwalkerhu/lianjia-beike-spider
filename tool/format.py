import pandas as pd
import os.path
import fnmatch
import glob


def recursiveSearchFiles(dirPath, partFileInfo): 
    fileList = []
    pathList = glob.glob(os.path.join('\\', dirPath, '*'))
    for mPath in pathList:
        if fnmatch.fnmatch(mPath, partFileInfo):
            fileList.append(mPath)
        elif os.path.isdir(mPath):
            fileList += recursiveSearchFiles(mPath, partFileInfo)
        else:
            pass
    return fileList

def get_csv_data(path):
  print(path)
  # house=pd.read_csv(path)
  # print(house)


def start():
  files = recursiveSearchFiles(os.path.abspath('.') + '/data', '*.csv')
  for file in files:
    get_csv_data(file)

if __name__ == "__main__":
  start()