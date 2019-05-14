import requests
import json
import re


def translateWord(word):
    i = json.loads(
        (requests.get("http://fy.iciba.com/ajax.php?a=fy&f=en-US&t=zh-CN", params={'w': str(word)})).text).get(
        "content").get("word_mean")
    return i


def remove_punctuation(line):
    rule = re.compile("[^a-zA-Z]")
    line = rule.sub('', line)
    return line

#返回的文章分割后的字典
def pieceProcess(path):
    result = dict()
    f = open(path, 'r')
    content = f.read()
    words = content.split()
    for word in words:
        if word != None and len(word) != 1:
            transWord = translateWord(remove_punctuation(word))[0]
            if transWord != None:
                r = list()
                r.append(transWord)
                result[word] = r
    f.close()
    return result


if __name__ == '__main__':
    print(translateWord("piece"))
    # print(pieceProcess('your_file.txt'))
    # print(remove_punctuation("22!@#$dd%%This,"))
