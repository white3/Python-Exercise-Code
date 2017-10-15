# coding=utf-8
'''
单词计数
在相对目录下 \in 有一些文本文件，要求统计出这些文本文件所有出现的单词的出现次数
代码实现：
'''
import re
txtPath = "test/foo.txt"
outPath = "test/out.txt"
maps = {}
with open(txtPath,"r") as fi:
    while True:
        line = fi.readline()
        if not line:   break
        if line == "":  pass
        words = re.compile("\W+").split(line)
        for word in words:
            if word and len(word)>1:
                maps[word] = maps.get(word,0)+1
its = maps.items()
its.sort(key=lambda x:x[1],reverse=True)
its = its[0:9]
with open(outPath, "w") as fo:
    for (name, time) in its:
        fo.write(name + " " + str(time) + "\n")
# test
with open(outPath,"r") as fo:
    for line in fo.readlines():
        print line.strip()