# -*- coding: UTF-8 -*-
import os, re
import random,readJSON
data = readJSON.jsonread("data.json")
#名人名言
quotes = data["famous"] # a 代表前面垫话，b代表后面垫话
#前面垫话

commencement = data["before"] # 在名人名言前面弄点废话
#后面垫话
fin = data['after']  # 在名人名言后面弄点废话
#废话
fadaise = data['bosh'] # 代表文章主要废话来源

xx = "大概掀翻小池塘"

#重复度
multplicity= 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

def shuffleDraw(table):
    global multplicity
    pool=list(table)*multplicity
    while True:
        random.shuffle(pool)
        for elem in pool:
            yield elem

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        print(tmp)