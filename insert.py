#!/usr/bin/python
# -*- coding: UTF-8 -*-

splitStr = '<!--contentBegin-->'
if __name__ == '__main__':
    #写入网页源码以及插入字段
    fo = open("wrote.txt", "r")
    foHtml = open("index.html","r")
    strHtml = foHtml.read()
    strType = fo.readline()
    pos = strHtml.split(splitStr,1)
    str = fo.read()
    str = str.decode(strType)
    str = str.encode('utf-8')
    print "Read successfully!"
    fo.close()
    foHtml.close()

    #写入网页字段
    if pos!=-1:
        strHtml = pos[0] + splitStr + '\n' + str + pos[1]
        foo = open("index.html", "w")
        foo.write(strHtml)
        foo.close()
        print "Write successfully!"


        