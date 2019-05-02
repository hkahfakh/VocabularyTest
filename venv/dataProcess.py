'''
param
correctRate 正确率
correctNum 正确次数
occurrenceNum 出现次数
passStat 太简单标志位
importTime 入库时间
'''
# -*- coding: utf-8 -*-
import json
import time
import os


def creattestjson():
    dict = {
        "apple": ["苹果"],
        "peach": ["桃"],
        "pear": ["梨"],
        "grape": ["葡萄"],
    }
    f = open("VocabularyLib//test.json", "w")
    json.dump(dict, f)
    f.close()


def addWord(word, translation, UserLib):
    myLib = open(UserLib + ".json", "r")
    myDict = json.load(myLib)
    myLib.close()

    if word not in myDict:
        myDict[word] = []
        myDict[word].append(translation)
        myDict[word].append(0.0)
        myDict[word].append(0)
        myDict[word].append(0)
        myDict[word].append(True)
        myDict[word].append(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))
    myLib = open(UserLib + ".json", "w")
    json.dump(myDict, myLib)
    myLib.close()


def addLib(UserLib, libName):
    myLib = open(UserLib + ".json", "r")
    lib = open("VocabularyLib//" + libName + ".json", "r")
    myDict = json.load(myLib)
    libDict = json.load(lib)
    lib.close()
    myLib.close()

    for i in libDict:
        if i not in myDict:
            myDict[i] = libDict[i]
            myDict[i].append(0.0)
            myDict[i].append(0)
            myDict[i].append(0)
            myDict[i].append(True)
            myDict[i].append(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))
    myLib = open(UserLib + ".json", "w")
    json.dump(myDict, myLib)
    myLib.close()


def viewLib(libName):
    lib = open("VocabularyLib//" + libName + ".json", "r")
    libDict = json.load(lib)
    for i in libDict.keys():
        print(i + "  " + str(libDict[i]))
    lib.close()


def viewMyLib(UserLib):
    lib = open(UserLib + ".json", "r")
    myDict = json.load(lib)
    for i in myDict.keys():
        print(i + "  " + str(myDict[i]))
    lib.close()


if __name__ == "__main__":
    # addLib("myLib","test")
    addWord("application", "应用", "myLib")
