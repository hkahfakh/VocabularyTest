'''
param
mean 英语翻译
correctRate 正确率
correctNum 正确次数
occurrenceNum 出现次数
passStat 太简单标志位
correctSign 本次正确标志位
importTime 入库时间
'''
# -*- coding: utf-8 -*-
import json
import time
import os
import importPiece


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
    myLib = open("UserData\\" + UserLib + ".json", "r")
    myDict = json.load(myLib)
    myLib.close()

    if word not in myDict:
        myDict[word] = []
        myDict[word].append(translation)
        myDict[word].append(0.0)
        myDict[word].append(0)
        myDict[word].append(0)
        myDict[word].append(False)
        myDict[word].append(False)
        myDict[word].append(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))
    myLib = open("UserData\\" + UserLib + ".json", "w")
    json.dump(myDict, myLib)
    myLib.close()


def addDict(UserLib, libDict):
    myLib = open("UserData\\" + UserLib + ".json", "r")
    myDict = json.load(myLib)
    myLib.close()

    for i in libDict.keys():
        if i not in myDict:
            myDict[i] = libDict[i]
            myDict[i].append(0.0)
            myDict[i].append(0)
            myDict[i].append(0)
            myDict[i].append(False)
            myDict[i].append(False)
            myDict[i].append(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))
    myLib = open("UserData\\" + UserLib + ".json", "w")
    json.dump(myDict, myLib)
    myLib.close()


def addLib(UserLib, libName):
    myLib = open("UserData\\" + UserLib + ".json", "r")
    lib = open("VocabularyLib\\" + libName, "r")
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
            myDict[i].append(False)
            myDict[i].append(False)
            myDict[i].append(time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time())))
    myLib = open("UserData\\" + UserLib + ".json", "w")
    json.dump(myDict, myLib)
    myLib.close()


def importP(UserLib):
    path = input("请输入路径+文件")
    if os.path.exists(path):
        addDict(UserLib, importPiece.pieceProcess(path))


def viewLib(libName):
    lib = open("VocabularyLib\\" + libName + ".json", "r")
    libDict = json.load(lib)
    for i in libDict.keys():
        print(i + "  " + str(libDict[i]))
    lib.close()


def viewMyLib(UserLib):
    lib = open("UserData\\" + UserLib + ".json", "r")
    myDict = json.load(lib)
    for i in myDict.keys():
        print(i + "  " + str(myDict[i]))
    lib.close()


def correctRate(UserLib):
    total = 1
    Correctnumber = 0

    lib = open("UserData\\" + UserLib + ".json", "r")
    myDict = json.load(lib)
    content = myDict.items()
    total = len(content)
    # total = content.len()
    for i in content:
        print(i[1][-2])
        if i[1][-2]==True:
            Correctnumber = Correctnumber + 1
    print("正确单词数："+str(Correctnumber))
    print("总单词数：" + str(total))
    print("正确率:" + str(Correctnumber / total))
    lib.close()


if __name__ == "__main__":
    # addLib("myLib", "test")
    correctRate("zhai")
    # addWord("application", "应用", "myLib")
