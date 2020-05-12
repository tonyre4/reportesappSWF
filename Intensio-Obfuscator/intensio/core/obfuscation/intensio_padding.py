# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import fileinput
import random
import textwrap
import re
import colorama
import sys
from progress.bar import Bar

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PROGRESS_COLOUR = colorama.Fore.BLUE + colorama.Style.BRIGHT 
ERROR_COLOUR    = colorama.Back.RED + colorama.Style.BRIGHT

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Padding:
    

    def __init__(self):
        self.mixer  = Mixer()
        self.remove = Remove()
        self.utils  = Utils()

        # -- Len of spaces -- #
        self.space0  = ""                                                                       
        self.space4  = "    "
        self.space8  = "        "
        self.space12 = "            "
        self.space16 = "                "
        self.space20 = "                    "
        self.space24 = "                        "
        self.space28 = "                            "
        self.space32 = "                                "
        self.space36 = "                                    "
        self.space40 = "                                        "
        self.space44 = "                                            "
        self.space48 = "                                                "
        self.space52 = "                                                    "
        self.space56 = "                                                        "
        self.space60 = "                                                            "
        self.space64 = "                                                                "


    def ScriptsGenerator(self, mixerLevelArg=None):
        varRandom1   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom2   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom3   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom4   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom5   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom6   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom7   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom8   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom9   = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom10  = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom11  = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom12  = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom13  = self.mixer.GetStringMixer(lenght=mixerLevelArg)
        varRandom14  = self.mixer.GetStringMixer(lenght=mixerLevelArg)

        # ---------- Python random scripts ---------- #
        rand = random.randint(1, 7)

        # -- script 1 -- #
        if rand == 1:
            scriptAssPadding1 = textwrap.dedent("""
                                                {0} = '{5}'
                                                {1} = '{6}'
                                                {2} = '{7}'
                                                {3} = '{8}'
                                                {4} = '{9}'
                                                if {0} in {1}:
                                                    {0} = {4}
                                                    if {1} in {2}:
                                                        {1} = {3}
                                                elif {1} in {0}:
                                                    {2} = {1}
                                                    if {2} in {1}:
                                                        {1} = {4}
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                            varRandom6, varRandom7, varRandom8, varRandom9, varRandom10)
            return scriptAssPadding1

        # -- script 2 -- #
        elif rand == 2:
            scriptAssPadding2 = textwrap.dedent("""
                                                {0} = '{2}'
                                                {1} = '{3}'
                                                if {0} != {1}:
                                                    {0} = '{3}'
                                                    {1} = {0}
                                                    {0} = '{2}'
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4)
            return scriptAssPadding2

        # -- script 3 -- #
        elif rand == 3:
            scriptAssPadding3 = textwrap.dedent("""
                                                {0} = '{6}'
                                                {1} = '{7}'
                                                {2} = '{8}'
                                                {3} = '{9}'
                                                {4} = '{10}'
                                                {5} = '{11}'
                                                if {0} != {3}:
                                                    {1} = {2}
                                                    for {5} in {3}:
                                                        if {5} != {2}:
                                                            {1} = {1}
                                                        else:
                                                            {4} = {0}
                                                else:
                                                    {2} = {0}
                                                    {0} = {4}
                                                    if {2} == {0}:
                                                        for {5} in {0}:
                                                            if {5} == {2}:
                                                                {2} = {0}
                                                            else:
                                                                {2} = {4}
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                            varRandom6, varRandom7, varRandom8, varRandom9, varRandom10, \
                                                            varRandom11, varRandom12)
            return scriptAssPadding3

        # -- script 4 -- #
        elif rand == 4:
            scriptAssPadding4 = textwrap.dedent("""
                                                {0} = '{3}'
                                                {1} = '{4}'
                                                {2} = '{5}'
                                                if {0} == {1}:
                                                    {2} = '{5}'
                                                    {2} = {0}
                                                else:
                                                    {2} = '{5}'
                                                    {2} = '{3}'
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, \
                                                            varRandom5, varRandom6,)
            return scriptAssPadding4

        # -- script 5 -- #
        elif rand == 5:
            scriptAssPadding5 = textwrap.dedent("""
                                                {0} = '{6}'
                                                {1} = '{7}'
                                                {2} = '{8}'
                                                {3} = '{9}'
                                                {4} = '{10}'
                                                {5} = '{11}'
                                                if {2} == {3}:
                                                    for {5} in {4}:
                                                        if {5} == {3}:
                                                            {4} = {0}
                                                        else:
                                                            {3} = {1}
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8, varRandom9, \
                                                            varRandom10, varRandom11, varRandom12)
            return scriptAssPadding5
    
        # -- script 6 -- #
        elif rand == 6:
            scriptAssPadding6 = textwrap.dedent("""
                                                {0} = '{4}'
                                                {1} = '{5}'
                                                {2} = '{6}'
                                                {3} = '{7}'
                                                if {1} == {0}:
                                                    for {0} in {1}:
                                                        if {1} == {1}:
                                                            {2} = '{3}'
                                                        elif {2} == {3}:
                                                            {3} = {0}
                                                        else:
                                                            {0} = {1}
                                                elif {2} == {2}:
                                                    for {2} in {1}:
                                                        if {3} == {1}:
                                                            {2} = '{3}'
                                                        elif {2} == {3}:
                                                            {3} = {0}
                                                        else:
                                                            {0} = {1}
                                                            for {2} in {1}:
                                                                if {3} == {1}:
                                                                    {2} = '{3}'
                                                                elif {2} == {3}:
                                                                    {3} = {0}
                                                                else:
                                                                    {0} = {3}
                                                else:
                                                    {0} = {1}
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8)
            return scriptAssPadding6
        
        # -- script 7 -- #
        elif rand == 7:
            scriptAssPadding7 = textwrap.dedent("""
                                                try:
                                                    {0} = '{7}'
                                                    {1} = '{8}'
                                                    {2} = '{9}'
                                                    {3} = '{10}'
                                                    {4} = '{11}'
                                                    {5} = '{12}'
                                                    {6} = [
                                                            '{7}',
                                                            '{9}',
                                                            '{11}',
                                                            '{13}'
                                                    ]
                                                    for {0} in {5}:
                                                        for {1} in {2}:
                                                            if {3} == {4}:
                                                                {1} = {0}
                                                            elif {4} == {1}:
                                                                {1} = {5}
                                                            else:
                                                                {4} = {5}
                                                                for {1} in {6}:
                                                                    {2} = {1}
                                                except Exception:
                                                    pass
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8, varRandom9, \
                                                            varRandom10, varRandom11, varRandom12, \
                                                            varRandom13, varRandom14)
            return scriptAssPadding7


    def AddRandomScripts(self, outputArg=None, mixerLevelArg=None, verboseArg=None):
        countScriptsAdded       = 0
        countLineAdded          = 0
        countLine               = 0
        checkLine               = 0
        checkQuotePassing       = 0
        checkCharPassing        = 0
        checkOtherCharPassing   = 0
        countRecursFiles        = 0

        addIndentScript         = r".*\:{1}\s+$|.*\:{1}\s*$"
        quotesIntoVariable      = r".*={1}\s*[\"|\']{3}"
        quotesEndMultipleLines  = r"^\s*[\"|\']{3}\)?\.?"
        quotesInRegex           = r"={1}\s*r{1}[\"|\']{3}"
        noAddScript             = r"^\@|\s+\@|\s+return|\s*def\s+.+\s*\:{1}|^class\s+.+\s*\:{1}|.*[\{|\[|\(|\)|\]|\}|,|\\|^]\s*$|\s+yield.*|\s+raise.*"
        quoteIntoVariable       = r".*\={1}\s*\w*\.?\w*[\(|\.]{1}[\']{3}|.*\={1}\s*\w*\.?\w*[\(|\.]{1}[\"\"\"]{3}|.*\={1}\s*[\"]{3}|.*\={1}\s*[\']{3}"

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running add of random scripts in {0} file(s)...\n".format(countRecursFiles))

        # -- Count the number of lines that will be checked before filling -- #
        with Bar(PROGRESS_COLOUR + "Setting up  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue
                        countLine += 1
                bar.next(1)
            bar.finish()

        # -- Padding scripts added -- #
        with Bar(PROGRESS_COLOUR + "Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        sys.stdout.write(eachLine)
                        if eachLine == "\n":
                            continue
                        else:
                            spaces = len(eachLine) - len(eachLine.lstrip())

                            # -- Detect code into 3 quotes excepted comments -- #
                            if re.match(quotesIntoVariable, eachLine):
                                if re.match(quotesInRegex, eachLine):
                                    pass
                                else:
                                    checkQuotePassing += 1
                                    continue
                            elif re.match(quotesEndMultipleLines, eachLine):
                                if re.match(quotesInRegex, eachLine):
                                    pass
                                else:
                                    checkQuotePassing += 1
                                    if checkQuotePassing == 2:
                                        checkQuotePassing = 0
                                    continue
                            if checkQuotePassing == 1:
                                continue
                            elif checkQuotePassing == 2:
                                checkQuotePassing = 0
                                pass
                            else:
                                pass
                            
                            # -- Check dict, list, tuple in multiple lines -- #
                            if checkCharPassing == 1:
                                if re.match(r".*[\"|\'|\)|\]|\}|\w]\s*$", eachLine):
                                    checkCharPassing = 0
                                    continue
                                else:
                                    continue
                            elif checkOtherCharPassing >= 1:
                                if re.match(r".*[\"|\'|\)|\]|\}|\w]\s*$", eachLine):
                                    checkOtherCharPassing -= 1
                                    continue
                                else:
                                    if re.match(r".*[\(|\{|\[]\s*$", eachLine):
                                        checkOtherCharPassing += 1
                                        continue
                            else:
                                pass
                            if re.match(noAddScript, eachLine):
                                if re.match(r".*[\\|,]\s*$", eachLine):
                                    if checkCharPassing == 1:
                                        continue
                                    else:
                                        checkCharPassing = 1
                                        continue
                                elif re.match(r".*[\(|\{|\[]\s*$", eachLine):
                                    checkOtherCharPassing += 1
                                    continue
                                else:
                                    continue
                            # -- Adding scripts -- #
                            elif re.match(addIndentScript, eachLine):
                                if spaces == 0:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space4))
                                    countScriptsAdded += 1                                                                
                                elif spaces == 4:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space8))
                                    countScriptsAdded += 1
                                elif spaces == 8:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space12))
                                    countScriptsAdded += 1
                                elif spaces == 12:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space16))
                                    countScriptsAdded += 1
                                elif spaces == 16:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space20))
                                    countScriptsAdded += 1
                                elif spaces == 20:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space24))
                                    countScriptsAdded += 1
                                elif spaces == 24:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space28))
                                    countScriptsAdded += 1
                                elif spaces == 28:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space32))
                                    countScriptsAdded += 1
                                elif spaces == 32:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space36))
                                    countScriptsAdded += 1
                                elif spaces == 36:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space40))
                                    countScriptsAdded += 1
                                elif spaces == 40:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space44))
                                    countScriptsAdded += 1
                                elif spaces == 44:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space48))
                                    countScriptsAdded += 1
                                elif spaces == 48:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space52))
                                    countScriptsAdded += 1
                                elif spaces == 52:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space56))
                                    countScriptsAdded += 1
                                elif spaces == 56:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space60))
                                    countScriptsAdded += 1
                                elif spaces == 60:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space64))
                                    countScriptsAdded += 1
                                else:
                                    continue
                            else:
                                if spaces == 0:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space0))
                                    countScriptsAdded += 1
                                elif spaces == 4:                                                                       
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space4))
                                    countScriptsAdded += 1
                                elif spaces == 8:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space8))
                                    countScriptsAdded += 1
                                elif spaces == 12:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space12))
                                    countScriptsAdded += 1
                                elif spaces == 16:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space16))
                                    countScriptsAdded += 1
                                elif spaces == 20:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space20))
                                    countScriptsAdded += 1
                                elif spaces == 24:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space24))
                                    countScriptsAdded += 1
                                elif spaces == 28:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space28))
                                    countScriptsAdded += 1
                                elif spaces == 32:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space32))
                                    countScriptsAdded += 1
                                elif spaces == 36:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space36))
                                    countScriptsAdded += 1
                                elif spaces == 40:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space40))
                                    countScriptsAdded += 1
                                elif spaces == 44:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space44))
                                    countScriptsAdded += 1
                                elif spaces == 48:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space48))
                                    countScriptsAdded += 1
                                elif spaces == 52:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space52))
                                    countScriptsAdded += 1
                                elif spaces == 56:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space56))
                                    countScriptsAdded += 1
                                elif spaces == 60:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(self, mixerLevelArg=mixerLevelArg), self.space60))
                                    countScriptsAdded += 1
                                else:
                                    continue
                bar.next(1)
            bar.finish()

        # -- Check if padding has added in output script -- #
        with Bar(PROGRESS_COLOUR + "Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue    
                        checkLine += 1
                bar.next(1)
            countLineAdded = checkLine - countLine
            bar.finish()
        
        if checkLine > countLine:    
            print("\n-> {0} scripts added in {1} file(s)\n".format(countScriptsAdded, countRecursFiles))
            print("-> {0} lines added in {1} file(s)\n".format(countLineAdded, countRecursFiles))
            return EXIT_SUCCESS
        else:
            return EXIT_FAILURE
    
    
    def EmptyClasses(self, outputArg=None, mixerLevelArg=None, verboseArg=None):
        countRecursFiles        = 0
        counterToCheckIndent    = 0
        numberLine              = 0
        numberLineInFile        = 0
        emptyClassInfo          = {}
        emptyClassInfoCheck     = {}

        detectClass     = r"^class\s+\w+|\s+class\s+\w+"
        classDefined    = r"class\s+(\w+)"
        
        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        with Bar(PROGRESS_COLOUR + "Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLineInFile    = 0
                numberLine          = 0
                # -- Count all line(s) in file -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLineInFile += 1
                bar.next(0.2)

                # -- Find and put empty class(es) in dict -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if counterToCheckIndent == 1: 
                            spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterClass == spacesClass:
                                if search:
                                    emptyClassInfo[search.group(1)] = file
                                    numberLineInFile += 1 # Adding one line because padding will be added
                                    numberLine += 1 # Adding one line because padding will be added
                        if re.match(detectClass, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                search = re.search(classDefined, eachLine)
                                if search:
                                    emptyClassInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(classDefined, eachLine)
                bar.next(0.3)
                
                # -- Add padding in empty class(es) -- #
                numberLine = 0
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterClass == spacesClass:
                                paddingVar1 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                paddingVar2 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                finalVarPadding = "{0} = '{1}'\n".format(paddingVar1, paddingVar2)
                                if spacesClass == 0:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space4))                                                                
                                elif spacesClass == 4:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space8))
                                elif spacesClass == 8:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space12))
                                numberLine += 1
                        sys.stdout.write(eachLine)
                        if re.match(detectClass, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                paddingVar1 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                paddingVar2 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                finalVarPadding = "{0} = '{1}'\n".format(paddingVar1, paddingVar2)
                                if spacesClass == 0:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space4))                                                                
                                elif spacesClass == 4:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space8))
                                elif spacesClass == 8:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space12))
                            else:
                                counterToCheckIndent += 1
                bar.next(0.5)
            bar.finish()

        # -- Check if class(es) is still empty -- #
        if emptyClassInfo != {}:
            with Bar(PROGRESS_COLOUR + "Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                for file in recursFiles:
                    numberLineInFile    = 0
                    numberLine          = 0
                    with open(file, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            numberLine += 1
                            if counterToCheckIndent == 1:
                                spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                                counterToCheckIndent = 0
                                if spacesAfterClass == spacesClass:
                                    if search:
                                        emptyClassInfo[search.group(1)] = file
                                        numberLineInFile += 1
                                        numberLine += 1
                            if re.match(detectClass, eachLine):
                                spacesClass = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile:
                                    search = re.search(classDefined, eachLine)
                                    if search:
                                        emptyClassInfo[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(classDefined, eachLine)
                    bar.next(1)
                bar.finish()

        
            if emptyClassInfoCheck == {}:
                for key, value in emptyClassInfo.items():
                    print("\n-> File : {0}".format(value))
                    print("-> Padding added in : {0} ( empty class )".format(key))
                return EXIT_SUCCESS    
            else:
                if verboseArg:
                    print("\n[!] No padding added to empty class(es)... :\n")
                    for key, value in emptyClassInfoCheck.items():
                        print("\n-> File : {0}".format(value))
                        print("-> Class : {0}".format(key))
                return EXIT_FAILURE
        else:
            print("[!] No empty class found in {0}".format(outputArg))
            return EXIT_SUCCESS

    
    def EmptyFunctions(self, outputArg=None, mixerLevelArg=None, verboseArg=None):
        countRecursFiles        = 0
        counterToCheckIndent    = 0
        numberLine              = 0
        numberLineInFile        = 0
        emptyFuncInfo           = {}
        emptyFuncInfoCheck      = {}

        detectFunction  = r"^def\s+\w+|\s+def\s\w+"
        functionDefined = r"def\s+(\w+)"   

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        with Bar(PROGRESS_COLOUR + "Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLineInFile    = 0
                numberLine          = 0
                # -- Count all line(s) in file -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLineInFile += 1
                bar.next(0.2)

                # -- Find and put empty function(s) in dict -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterFunc == spacesFunc:
                                if search:
                                    emptyFuncInfo[search.group(1)] = file
                                    numberLineInFile += 1 # Adding one line because padding will be added
                                    numberLine += 1 # Adding one line because padding will be added
                        if re.match(detectFunction, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                search = re.search(functionDefined, eachLine)
                                if search:
                                    emptyFuncInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(functionDefined, eachLine)
                bar.next(0.3)

                # -- Add padding in empty function(s) -- #
                numberLine = 0
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterFunc == spacesFunc:
                                paddingVar1 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                paddingVar2 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                finalVarPadding = "{0} = '{1}'\n".format(paddingVar1, paddingVar2)
                                if spacesFunc == 0:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space4))                                                                
                                elif spacesFunc == 4:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space8))
                                elif spacesFunc == 8:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space12))
                                elif spacesFunc == 12:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space16))
                                elif spacesFunc == 16:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space20))
                                elif spacesFunc == 20:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space24))
                                numberLine += 1 
                        sys.stdout.write(eachLine)
                        if re.match(detectFunction, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                paddingVar1 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                paddingVar2 = self.mixer.GetStringMixer(lenght=mixerLevelArg)
                                finalVarPadding = "{0} = '{1}'\n".format(paddingVar1, paddingVar2)
                                if spacesFunc == 0:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space4))                                                                
                                elif spacesFunc == 4:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space8))
                                elif spacesFunc == 8:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space12))
                                elif spacesFunc == 12:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space16))
                                elif spacesFunc == 16:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space20))
                                elif spacesFunc == 20:
                                    sys.stdout.write(textwrap.indent(finalVarPadding, self.space24))
                            else:
                                counterToCheckIndent += 1
                bar.next(0.5)
            bar.finish()

        # -- Check if function(s) is still empty -- #
        if emptyFuncInfo != {}:
            with Bar(PROGRESS_COLOUR + "Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                for file in recursFiles:
                    numberLineInFile    = 0
                    numberLine          = 0
                    with open(file, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            numberLine += 1
                            if counterToCheckIndent == 1:
                                spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                                counterToCheckIndent = 0
                                if spacesAfterFunc == spacesFunc:
                                    if search:
                                        emptyFuncInfoCheck[search.group(1)] = file
                                        numberLineInFile += 1
                                        numberLine += 1
                            if re.match(detectFunction, eachLine):
                                spacesFunc = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile:
                                    search = re.search(functionDefined, eachLine)
                                    if search:
                                        emptyFuncInfoCheck[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(functionDefined, eachLine)
                    bar.next(1)
                bar.finish()

            if emptyFuncInfoCheck == {}:
                for key, value in emptyFuncInfo.items():
                    print("\n-> File : {0}".format(value))
                    print("-> Padding added in : {0} ( empty function )".format(key))
                return EXIT_SUCCESS
            else:
                if verboseArg:
                    print("\n[!] No padding added to empty function(s)... :\n")
                    for key, value in emptyFuncInfoCheck.items():
                        print("\n-> File : {0}".format(value))
                        print("-> Function : {0}".format(key))
                return EXIT_FAILURE
        else:
            print("[!] No empty function found in {0}".format(outputArg))
            return EXIT_SUCCESS