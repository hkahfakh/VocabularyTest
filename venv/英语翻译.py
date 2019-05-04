# import xlrd
import json
# import  jieba
import random
import os
import test

# #获取目标EXCEL文件sheet名
# table = workbook.sheets()[1]
# nrows = table.nrows #行数
# ncols = table.ncols #列数
# count ={}
#
# for i in range(0,nrows):
#     s=[""]
#     hang= table.row_values(i) #某一行数据for item in rowValues:print item
#     s[0] = hang[1]
#     count[hang[0]] = s
#
# print(count)
#
# with open('CET4.json', 'w') as f:
#     json_str = json.dump(count,f)
inpath = {"apple": ["\u82f9\u679c", 0.5, 1, 2, 'ture', 'false', "2019.05.02.18.23.10"],
          "peach": ["\u6843", 0.0, 0, 0, 'ture', 'ture', "2019.05.02.18.23.10"],
          "pear": ["\u68a8", 0.0, 0, 0, 'false', 'false', "2019.05.02.18.23.10"],
          "grape": ["\u8461\u8404", 0.0, 0, 0, 'false', 'false', "2019.05.02.18.23.10"],
          "dim": ["\u93c6\u6941\u8d30", 0.0, 0, 0, 'false', 'false', "2019.05.02.18.23.10"]}
outpath = ("key.txt")
keys = []
panduanjg = []
zuizhong = []
i = 0
j = 0
yisi = ''

outpath=""
def pach(name):
    global outpath
    outpath = (name + ".txt")
    open(outpath, "w")
def write(key):
    with open(outpath, "w") as f:
        f.writelines(key)

def key(inpath):
    global outpath
    biaozhi=os.path.exists(outpath)
    if(biaozhi==True):
         keys = list(inpath.keys())
         write(keys)
    jieguo = random.sample(keys, 4)
    daan = []
    daan = []
    list1 = []
    for i in jieguo[::1]:
        value = inpath[i][0]
        panduan = inpath[i][4]
        # print(panduan)
        list2 = [i, value, panduan]
        list1.append(list2)
        panduanj = [panduan]
        panduanjg.extend(panduanj)
        # print(panduanjg)
    for i in panduanjg:
        while ('ture' == i):
            inex = panduanjg.index('ture')
            del (keys[inex])
            write(outpath, keys)
            jieguo = random.sample(keys, 1)
            break
    suiji = random.sample(list1, 1)
    yingyu = suiji[0][0]
    daan.append(yingyu)
    fanyi = suiji[0][1]
    daan.append(fanyi)
    inex = keys.index(yingyu)
    del (keys[inex])
    write(keys)
    for i in list1:
        daan1 = i[1]
        daan.append(daan1)
    return daan


def geshi(xianshi):
    daansuiji = []
    yingyu = xianshi[0]
    yisi = xianshi[1]
    daansuiji.append(xianshi[2])
    daansuiji.append(xianshi[3])
    daansuiji.append(xianshi[4])
    daansuiji.append(xianshi[5])
    da = random.sample(daansuiji, 4)
    asq = da.index(yisi)
    da.append(yingyu)
    da.append(asq)
    return da


def repley(inpath):
    zhi = geshi(key(inpath))
    return zhi


if __name__ == '__main__':
    zhi = geshi(key(inpath))
    print(zhi)
