# -*- coding: utf-8 -*-

import sys
import re

withDoubleSpans = open("tagged.html", "r")
spansSeparated = open("unseparatedSpans.html", "w")

for line in withDoubleSpans:
    if line.find("</span><span") == -1:
        spansSeparated.write(line)
    else:
        splitChunks = line.split("<span")
        spansSeparated.write("<span" + splitChunks[1] + "\n<span" + splitChunks[2])
withDoubleSpans.close()
spansSeparated.close()

inFile = open("unseparatedSpans.html", "r")
outFile = open("outPutToManicure.html", "w")

spaceIsAllowed = True



for line in inFile:
    outputLine = ""
    mdashInd = line.find("&amp;mdash;")
    htmlTagInd = line.find("&lt;")
    tagOtherInd = line.find("tagOther")

    if mdashInd != -1: # word is an mdash...
        outputLine = " " + u'\u2014'
    elif htmlTagInd >= 1: # word is actually an HTML tag
        htmlTagEndInd = line.find("&gt;")
        outputLine = "\n" + ("<" + line[htmlTagInd + 4 : htmlTagEndInd] + ">").replace("&nbsp;", " ")
    elif tagOtherInd >= 1: # word is tagged "other" part of speech
        punctuationEnd = line.find("</")
        contentOfOther = line[tagOtherInd + 10:punctuationEnd]
        if contentOfOther.isalnum(): # is a plain ol english word
# gross, just copying and pasting this cuz i don't understand python syntax
            stringStartInd = line.find(">")
            tagStartInd = line.find("taggedWord tag") + 13
            tagEndInd = line.find('">')
            if line[stringStartInd + 1].isupper():
                outputLine = (" " if spaceIsAllowed else "") + line[tagStartInd + 1 : tagEndInd]
                spaceIsAllowed = True
            else:
                outputLine = (" " if spaceIsAllowed else "") + line[tagStartInd + 1 : tagEndInd].lower()
                spaceIsAllowed = True
        else: # is punctuation
            if line.find(u'\u201c') != -1: # curly double quote
                outputLine = (" " if spaceIsAllowed else "") + contentOfOther
                spaceIsAllowed = False
            elif line.find(u'\u2018') != -1: # curly single quote
                outputLine = (" " if spaceIsAllowed else "") + contentOfOther
                spaceIsAllowed = False
            elif contentOfOther == "-":
                outputLine = contentOfOther
                spaceIsAllowed = False
            elif contentOfOther == "(":
                outputLine = (" " if spaceIsAllowed else "") + contentOfOther
                spaceIsAllowed = False
            elif contentOfOther == "[":
                outputLine = (" " if spaceIsAllowed else "") + contentOfOther
                spaceIsAllowed = False
            elif contentOfOther == "$":
                outputLine = (" " if spaceIsAllowed else "") + contentOfOther
                spaceIsAllowed = False
            else:
                if contentOfOther == ",":
                    outputLine = contentOfOther
                elif contentOfOther == ".":
                    outputLine = contentOfOther
                elif contentOfOther == "?":
                    outputLine = contentOfOther
                elif contentOfOther == ";":
                    outputLine = contentOfOther
                elif contentOfOther == ":":
                    outputLine = contentOfOther
                elif contentOfOther == "!":
                    outputLine = contentOfOther
                elif contentOfOther == ")":
                    outputLine = contentOfOther
                elif contentOfOther == "]":
                    outputLine = contentOfOther
                elif line.find(u'\u2014') != -1:
                    outputLine = contentOfOther + "asdfasdf"
                elif line.find(u'\u201d') != -1:
                    outputLine = contentOfOther
                elif line.find(u'\u2019') != -1:
                    outputLine = contentOfOther
                elif line.find(u'\u2026') != -1:
                    outputLine = contentOfOther
                else:
                    outputLine = (" " if spaceIsAllowed else "") + contentOfOther + " othercontent"
                    # outputLine = line
                    spaceIsAllowed = False
    else:
# gross, just copying and pasting this cuz i don't understand python syntax
        stringStartInd = line.find(">")
        tagStartInd = line.find("taggedWord tag") + 13
        tagEndInd = line.find('">')
        if line[stringStartInd + 1].isupper():
            outputLine = (" " if spaceIsAllowed else "") + line[tagStartInd + 1 : tagEndInd]
            spaceIsAllowed = True
        else:
            outputLine = (" " if spaceIsAllowed else "") + line[tagStartInd + 1 : tagEndInd].lower()
            spaceIsAllowed = True
    outFile.write(outputLine)
inFile.close()
outFile.close()
