import nmapTest
import os
import time

print('ip文件名为ip.txt，且在当前目录，结果保存到nmapResult文件夹下')
nmapTest.makedir('nmapResult')
os.chdir('nmapResult')
filePath = '../ip.txt'
ipList = nmapTest.getIpList(filePath)

if (len(ipList) > 0):
    for ip in ipList:
        ip = str(ip)
        command = 'nmap.exe -n -P0 -sS -sV -p1-65535 -oX '+ ip +'.xml ' + ip
        print('当前命令为： ',command)
        nmapTest.log('执行nmap命令: '+command + '    ' +  '时间：' + time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))
        nmapTest.nmapComondExecute(command)

