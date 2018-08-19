#encoding=utf-8

#import os 
#mypath = os.path.exists("K:\TMP\wechat_callback_msg")
#print(mypath)
#os.mkdir("K:\\TMP\\wechat_callback_msg\\abc")

#import time
#curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#print(curr_time)

import itchat
from itchat.content import *

@itchat.msg_register([PICTURE,TEXT])
def simple_reply(msg):
	#print("Content:" + msg["Content"])
	#itchat.send_msg('nice to meet you',msg['FromUserName'])
	msg.user.send('%s: %s' % (msg.type, msg.text))
	return msg.text

itchat.auto_login(hotReload=True)
#itchat.auto_login(enableCmdQR=True)
#itchat.run()
users=itchat.search_friends(name=u'微信通信录备注')
userName = users[0]['UserName']
print(userName)
for num in range(1,200):   # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:     # 确定第一个因子
            j=num/i        # 计算第二个因子
            #print '%d 等于 %d * %d' % (num,i,j)
            itchat.send('%d 等于 %d * %d ' % (num,i,j),toUserName = userName)
            break          # 跳出当前循环
    else:                  # 循环的 else 部分
        itchat.send('%d 是一个质数' % num,toUserName = userName)
        #print num, '是一个质数'
#itchat.send('...',toUserName = userName)
