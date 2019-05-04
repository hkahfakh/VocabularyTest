import json
import time
import os
import dataProcess as dp
import 英语翻译 as msy

UserName = "default"
Path = ""
MYDict = {}


def welcome():
    str = '''*                                                                           *
*__      __             _           _                    _______        _   *
*\ \    / /            | |         | |                  |__   __|      | |  *
* \ \  / /__   ___ __ _| |__  _   _| | __ _ _ __ _   _     | | ___  ___| |_ *
*  \ \/ / _ \ / __/ _` | '_ \| | | | |/ _` | '__| | | |    | |/ _ \/ __| __|*
*   \  / (_) | (_| (_| | |_) | |_| | | (_| | |  | |_| |    | |  __/\__ \ |_ *
*    \/ \___/ \___\__,_|_.__/ \__,_|_|\__,_|_|   \__, |    |_|\___||___/\__|*
*                                                 __/ |                     *
*                                                |___/                      *
*                                                                           *'''
    print("-" * 77)
    print(str)
    print("-" * 77)


def init():
    global MYDict, UserName
    welcome()

    UserName = input("请输入你的姓名")

    msy.pach("UserData\\" + UserName)
    Path = os.getcwd()
    if UserName + ".json" not in os.listdir(Path + "\\UserData"):
        file = open(Path + "\\UserData" + "\\" + UserName + '.json', 'w')
        file.write("{}")
        file.close()

        path = Path + "\\VocabularyLib"
        files = os.listdir(path)
        for i in range(files.__len__()):
            print(i, files[i])

        number = input("请选择你要添加的库")

        for i in number.split(","):
            dp.addLib(UserName, files[int(i)])

    f = open("UserData\\" + UserName + ".json", 'r')
    MYDict = json.load(f)
    f.close()

    os.system("cls")


def option():
    print("-" * 77)
    print("1.进入单词量检测")
    print("2.添加单词")
    print("3.查看我的库")
    print("-" * 77)
    return int(input("输入你要进行的操作"))


# [选项一，选项二，选项三，选项四，英语，正确选项]
def create_question(element):
    print(element[4])
    print("-" * 77)
    for i in element[0:4]:
        print(i)
    print("-" * 77)
    return element[4], element[5]


def correctJudgment():
    while True:
        question_param = msy.repley(MYDict)
        correct = create_question(question_param)
        MYDict[correct[0]][3] = MYDict[correct[0]][3] + 1
        if input("请输入正确答案") == str(correct[1]):
            print("回答正确")
            MYDict[correct[0]][2] = MYDict[correct[0]][2] + 1
        else:
            print("回答错误")
        MYDict[correct[0]][1] = round(MYDict[correct[0]][2] / MYDict[correct[0]][3], 2)
        MYDict[correct[0]][5] = True

        s = input("回车继续")
        if s == "exit":
            break
        elif s == "s":
            MYDict[correct[0]][4] = True

        os.system("cls")


# 还需添加keys列表保存
def exit_Process():
    f = open("UserData\\" + UserName + ".json", "w")
    json.dump(MYDict, f)
    f.close()


if __name__ == '__main__':
    init()
    while True:
        choice = option()
        if choice == 1:
            correctJudgment()
            exit_Process()
            os.system("cls")
        elif choice == 2:
            word = input("输入单词")
            translation = input("输入单词释义")
            dp.addWord(word, translation, UserName)
            os.system("cls")
        elif choice == 3:
            dp.viewMyLib(UserName)
        else:
            print("无效选择请重新输入")
            os.system("cls")
