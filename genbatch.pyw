#! python3

import sys, shutil, os

batchFolder = 'W:\\PyBatches'

def stripExtension(fileName):
    return '.'.join(fileName.split('.')[:-1])

def doesBatchFileExist(fileName):
    if ('.py' in fileName):
        fileName = stripExtension(fileName)
    os.chdir(batchFolder)
    return os.path.exists(fileName + '.bat')

def generateBatchFile(fileName, relPath):
    fileNameWithoutExt = stripExtension(fileName)
    absFileName = os.path.join(batchFolder, relPath, fileName)
    os.chdir(batchFolder)
    batchFile = open(fileNameWithoutExt + '.bat', 'w')
    exeFileName = 'py.exe'
    if ('.pyw' in fileName):
        exeFileName = 'pyw.exe'    
    batchFile.write('@%s %s %%*' % (exeFileName, absFileName))

for folderName, subFolders, fileNames in os.walk(batchFolder):
    for fileName in fileNames:
        if '.py' in fileName and not doesBatchFileExist(fileName):
            relPath = os.path.relpath(folderName, batchFolder)
            generateBatchFile(fileName, relPath)
