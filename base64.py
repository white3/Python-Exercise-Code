import base64
def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32 # 取ASC码表数亦或于32，如果是 + 32，否则不变
        x = x + 16
        s += chr(x) # 还原ASC码
    return base64.b64encode(s)
'''------------------------------- de -------------------------------'''
def run(deep, len, List, result, resultList):
    if deep==len:resultList.append(result);print result;return;
    x = List[deep]
    while x<127:
        temp = result
        result = temp + chr(x)
        run(deep+1, len, List, result, resultList)
        x += 32
def decode(message):
    s = base64.b64decode(message)
    resultList = []
    numList = []
    for i in xrange(len(s)):
        numList.append(ord(s[i])-16)
    run(deep=0,len=len(s),List=numList,result='',resultList=resultList)
    return resultList


correct = "d3tzhHZrVCNTIF1gWVwhXimPgGlt"
test = encode("A3a1")
print test
print decode(test)
flag = ''
'''
print 'Input flag:'
flag = raw_input()
if encode(flag) == correct:
    print 'correct'
else:
    print 'wrong'
'''