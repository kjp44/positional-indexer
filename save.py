import os
import collections


def saveFile(fileName, fileType, fileContent):
    f = open(fileName + fileType, 'w', encoding='utf-8', errors='ignore')
    f.write(fileContent)
    f.close()


def sortIndex(index):
    sortedIndex = collections.OrderedDict(sorted(index.items()))
    return sortedIndex


def arrayToSave(array):
    array.sort()
    arrayToSave = ''
    count = 0
    for item in array:
        count += 1
        arrayToSave += str(count) + ': ' + item + '\n'
    return arrayToSave
