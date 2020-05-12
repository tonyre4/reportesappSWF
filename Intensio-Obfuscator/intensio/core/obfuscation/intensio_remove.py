# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import colorama
import os
import sys
from progress.bar import Bar

from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE, ERROR_FILE_NOT_FOUND
from core.utils.intensio_utils import Utils

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PROGRESS_COLOUR = colorama.Fore.BLUE + colorama.Style.BRIGHT 

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Remove:


    def __init__(self):
        self.utils = Utils()


    def LinesSpaces(self, outputArg=None, verboseArg=None):
        checkLinesSpace     = {}
        checkEmptyLine      = 0
        countRecursFiles    = 0
        numberLine          = 0

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for file in recursFiles:
            countRecursFiles += 1

        # -- Remove all empty lines -- #
        with Bar(PROGRESS_COLOUR + "Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.FileInput(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if eachLine == "\n":
                            pass
                        else:
                            sys.stdout.write(eachLine)
                bar.next(1)
            bar.finish()

        with Bar(PROGRESS_COLOUR + "Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLine = 0
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if eachLine == "\n":
                            checkLinesSpace[numberLine] = file
                            checkEmptyLine += 1
                bar.next(1)
            bar.finish()

        if checkEmptyLine == 0:
            return EXIT_SUCCESS
        else:
            if verboseArg:
                print("\n[!] Empty line that not been removed... :\n")
                for key, value in checkLinesSpace.items():
                    print("\n-> File : {0}".format(value))
                    print("-> Line : {0}".format(key))
            return EXIT_FAILURE


    def Comments(self, outputArg=None, verboseArg=None):
        checkRemoved            = {}
        countLineOutput         = 0
        countLineInput          = 0
        noComments              = 0
        multipleLinesComments   = 0
        countRecursFiles        = 0
        numberLine              = 0
            
        commentsBeginLine               = r"^\#.*"
        quoteOfCommentsEndLines         = r".*[\'\|\"]{3}\s*$"
        quoteInRegex                    = r"={1}\s*r[\"|\']{3}"
        quoteOfCommentsMultipleLines    = r"^\s+[\"|\']{3}|^[\"|\']{3}"
        quoteOfCommentsOneLine          = r".*[\"]{3}.*[\"]{3}|.*[\']{3}.*[\']{3}\s*$"
        quoteIntoVariableOrPrint        = r"s*print.*\(?[\"|\']{3}|.*\=\s*[\"|\']{3}"
        commentsAfterLine               = r"\s*\#[^\"|^\'|^\.|^\?|^\*|^\!|^\]|^\[|^\\|^\)|^\(|^\{|^\}].*"

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1
        
        # -- Remove comments and Count comments will be removed -- #            
        print("\n[+] Running remove comments in {0} file(s)...\n".format(countRecursFiles))

        with Bar(PROGRESS_COLOUR + "Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                # -- Remove comments -- #
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if "coding" in eachLine or "#!" in eachLine:
                            sys.stdout.write(eachLine)
                            continue
                        if multipleLinesComments == 1 or noComments == 1:
                            if re.match(quoteOfCommentsEndLines, eachLine):
                                if re.match(quoteInRegex, eachLine):
                                    countLineInput += 1
                                    continue
                                elif re.match(quoteIntoVariableOrPrint, eachLine):
                                    countLineInput += 1
                                    continue
                                else:
                                    if multipleLinesComments == 1:
                                        multipleLinesComments = 0
                                        countLineInput += 1
                                    else:
                                        noComments = 0
                                        sys.stdout.write(eachLine)
                                    continue
                            else:
                                if noComments == 1:
                                    sys.stdout.write(eachLine)
                                else:
                                    countLineInput += 1
                                continue
                        elif multipleLinesComments == 0:
                            if re.match(quoteOfCommentsMultipleLines, eachLine):   
                                if re.match(quoteOfCommentsOneLine, eachLine):
                                    countLineInput += 1
                                    continue
                                else:
                                    countLineInput += 1
                                    multipleLinesComments = 1
                                    continue
                            elif re.match(quoteIntoVariableOrPrint, eachLine):
                                noComments = 1
                                sys.stdout.write(eachLine)
                                continue
                            else:
                                sys.stdout.write(eachLine)
                        else:
                            sys.stdout.write(eachLine)
                bar.next(0.5)

                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if "coding" in eachLine or "#!" in eachLine:
                            sys.stdout.write(eachLine)
                            continue
                        searchCommentsAfterLine = re.search(commentsAfterLine, eachLine)
                        searchCommentsBeginLine = re.search(commentsBeginLine, eachLine)
                        if searchCommentsBeginLine:
                            countLineInput += 1
                            eachLine = eachLine.replace(searchCommentsBeginLine.group(0), "")
                            sys.stdout.write(eachLine)
                        elif searchCommentsAfterLine:
                            eachLine = eachLine.replace(searchCommentsAfterLine.group(0), "")
                            countLineInput += 1
                            sys.stdout.write(eachLine)
                        else:
                            sys.stdout.write(eachLine)
                bar.next(0.5)
            bar.finish()


        # -- Check if all comments are removed -- #
        noComments              = 0
        multipleLinesComments   = 0

        with Bar(PROGRESS_COLOUR + "Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    numberLine = 0
                    for eachLine in readF:
                        numberLine += 1
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        else:
                            if multipleLinesComments == 1 or noComments == 1:
                                if re.match(quoteOfCommentsEndLines, eachLine):
                                    if re.match(quoteInRegex, eachLine):
                                        countLineOutput += 1
                                        continue
                                    elif re.match(quoteIntoVariableOrPrint, eachLine):
                                        countLineOutput += 1
                                        continue
                                    else:
                                        if multipleLinesComments == 1:
                                            multipleLinesComments = 0
                                            checkRemoved[numberLine] = "{0} ( multiple lines comments )".format(file)
                                            countLineOutput += 1
                                        else:
                                            noComments = 0
                                        continue
                                else:
                                    if noComments == 1:
                                        pass
                                    else:
                                        countLineOutput += 1
                                    continue
                            elif multipleLinesComments == 0:
                                if re.match(quoteOfCommentsMultipleLines, eachLine):   
                                    if re.match(quoteOfCommentsOneLine, eachLine):
                                        checkRemoved[numberLine] = file
                                        countLineOutput += 1
                                        continue
                                    else:
                                        countLineOutput += 1
                                        multipleLinesComments = 1
                                        continue
                                elif re.match(quoteIntoVariableOrPrint, eachLine):
                                    noComments = 1
                                    continue
                                else:
                                    pass
                            else:
                                pass
                bar.next(0.5)
                  
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    numberLine = 0
                    for eachLine in readF:
                        numberLine += 1
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        else:
                            searchCommentsAfterLine = re.search(commentsAfterLine, eachLine)
                            searchCommentsBeginLine = re.search(commentsBeginLine, eachLine)
                            if searchCommentsBeginLine:
                                checkRemoved[numberLine] = file
                                countLineOutput += 1
                            elif searchCommentsAfterLine:
                                checkRemoved[numberLine] = file
                                countLineOutput += 1
                            else:
                                pass
                bar.next(0.5)
            bar.finish()

        if countLineOutput == 0:
            print("\n-> {0} lines of comments removed\n".format(countLineInput))            
            return EXIT_SUCCESS
        else:
            if verboseArg:
                print("\n[!] Comments that not been removed... :\n")
                for key, value in checkRemoved.items():
                    print("\n-> File : {0}".format(value))
                    if "multiple lines comments" in value:
                        print("-> Line : {0} ( This is the end line of multiple lines comments )".format(key))
                    else:
                        print("-> Line : {0}".format(key))
                print("\n-> {0} lines of comments no removed\n".format(countLineOutput))
            return EXIT_FAILURE


    def TrashFiles(self, outputArg=None, verboseArg=None):
        countRecursFiles    = 0
        removeFiles         = 0
        checkPycFile        = []
        currentPosition     = os.getcwd()

        detectPycFiles  = r".*\.pyc$"
        removePycFiles  = r"\w+\.pyc$"

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="pyc", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        if countRecursFiles == 0:
            print("[!] No .pyc file(s) found in {0}".format(outputArg))
            return EXIT_SUCCESS

        print("\n[+] Running remove {0} .pyc file(s)...\n".format(countRecursFiles))

        # -- Check if .pyc file(s) exists and remove it -- #
        with Bar(PROGRESS_COLOUR + "Setting up  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                if re.match(detectPycFiles, file):
                    removeFiles += 1
                    checkPycFile.append(file)
                bar.next(1)
            bar.finish()

        # -- Remove pyc file(s) -- #
        with Bar(PROGRESS_COLOUR + "Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:   
                if re.match(detectPycFiles, file):
                    extractPycFiles = re.search(removePycFiles, file)
                    moveFolder      = re.sub(removePycFiles, "", file)
                    os.chdir(moveFolder)
                    os.remove(extractPycFiles.group(0))
                    os.chdir(currentPosition)
                bar.next(1)
            bar.finish()
        
        checkRecursFiles = self.utils.CheckFileDir(
                                                    output=outputArg, 
                                                    detectFiles="pyc", 
                                                    blockDir="__pycache__", 
                                                    blockFile=False,
                                                    dirOnly=False
        )

        if checkRecursFiles != []:
            if verboseArg:
                for pycFile in checkRecursFiles:
                    print("-> .pyc file no removed : {0}".format(pycFile))
            return EXIT_FAILURE
        else:
            if verboseArg:
                for pycFile in checkPycFile:
                    print("-> .pyc file removed : {0}".format(pycFile))
        print("\n-> {0} .pyc file(s) removed".format(removeFiles))
        return EXIT_SUCCESS
