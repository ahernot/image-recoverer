import posix
import os

def process (dirEntry: posix.DirEntry):

    suffix = ''  # '-recovered'

    with open (dirEntry.path, 'r', encoding='utf-8') as inputFile:
        inputText = inputFile.read()

    fileBytes = bytes.fromhex(inputText)

    inputHead, inputTail = os.path.split(dirEntry.path)
    fileName, extension = os.path.splitext(inputTail)

    outputHead = 'output'
    outputTail = f'{fileName}{suffix}{extension}'
    outputPath = os.path.join (outputHead, outputTail)

    with open (outputPath, 'wb') as outputFile:
        outputFile.write(fileBytes)

    ## Add read EXIF and change file dateTime


for dirEntry in os.scandir ('input/'):
    process(dirEntry)
