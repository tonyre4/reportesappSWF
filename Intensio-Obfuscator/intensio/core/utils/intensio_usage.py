# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import argparse

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#
class Args:

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="intensio_obfuscator.py")
        
        self.parser.add_argument(
                                "-i", "--input",
                                help="source file or directory - if multiple files indicate a directory that contain all your files"
        )
        self.parser.add_argument(
                                "-o", "--output",
                                help="output file or directory that will be obfuscated - if multiple file indicate a empty directory that will contain all your files"
        )
        self.parser.add_argument(
                                "-m", "--mixerlevel",
                                choices=["lower", "medium", "high"],
                                default="medium",
                                help="generate random strings of [lower:32 | medium:64 | high:128] chars when 'replacetostr' - 'paddingscript' - 'replacefilename'\
                                    - 'replacetohex' features are specified, default value: [medium], possible values: [lower, medium, high]"
        )
        self.parser.add_argument(
                                "-rts", "--replacetostr",
                                action="store_true",
                                default=False,
                                help="activate the 'replace string to string mixed' obfuscation feature"
        )
        self.parser.add_argument(
                                "-ps", "--paddingscript",
                                action="store_true",
                                default=False,
                                help="activate the 'padding script' obfuscation feature"
        )
        self.parser.add_argument(
                                "-rfn", "--replacefilename",
                                action="store_true",
                                default=False,
                                help="activate the 'replace file name' obfuscation feature"
        )
        self.parser.add_argument(
                                "-rth", "--replacetohex",
                                action="store_true",
                                default=False,
                                help="activate the 'replace string to hex' obfuscation feature"
        )
        self.parser.add_argument(
                                "-v", "--verbose",
                                action="store_true",
                                default=False,
                                help="improve verbosity"
        )


    def GetArgHelp(self):
        return self.parser.print_help()

    
    def GetArgsValue(self):
        return self.parser.parse_args()
