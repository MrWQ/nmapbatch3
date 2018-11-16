

import os
import linecache
import time



# 命令执行
def nmapComondExecute(command ):
    os.system(command)

# 每次返回一个ip列表
def getIpList(filePath):
    lineNumber = len(linecache.getlines(filePath))
    ipList = []
    for count in range(1,lineNumber+1):
        ip = linecache.getline(filePath, count)
        ip = ip.replace('\n','') #去掉换行符
        ip = ip.replace('\r', '')  # 去掉换行符
        ip = ip.replace(' ','') #去掉空格
        if len(ip) < 8 and len(ip) > 0: #如果长度小于8 说明不是ip ,简单判断ip
            print('ip.txt第',str(count),'行 有错误。','内容为：',ip)
            log(filePath + '文件 第 ' + str(count) + ' 行有错误。  内容为：' + ip + '    '+ time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))
        elif len(ip) ==0:
            pass
        else:
            if ip in ipList:
                pass
            else:
                ipList.append(ip)
    return ipList

# 创建文件夹
def makedir(dirname):
    if os.path.lexists(dirname):
        pass
    else:
        os.makedirs(dirname)

def log(log):
    with open('nmapTest.log','a') as logFile:
        logFile.write(log)
        logFile.write('\n')




