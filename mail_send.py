#-*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import time

PATH='/usr/local/mail_error'
_user = "xxxx@domain.com"
_pwd  = "****"
_to   = ["xxx@domain.com","yyyyy@domain.com",]
 
CurrentTime=time.strftime('%Y%m%d-%H:%M:%S',time.localtime(time.time()))
msg_titile='error_msg'+CurrentTime
msg_text='xxxx error send'

#通过dir 批量加载文件#
def Mime_dir_list(part,path):
    filelist = os.listdir(path)
    for filename in filelist:
        part = MIMEApplication(open(os.path.join(path,filename),'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)
    return filelist

#删除文件
def rm_file(filelist,path):
    if len(filelist)>20:
        return
    else:
        for filename in filelist:
            os.remove(os.path.join(path,filename))



#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] =  msg_titile
msg["From"]    = _user
msg["To"]      = ','.join(_to)

#---这是文字部分---
part = MIMEText(msg_text)
msg.attach(part)

#---这是附件部分---
filelist= Mime_dir_list(part ,PATH)


try :
    s = smtplib.SMTP("mail.domain.com", timeout=30)#连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)#登陆服务器
    s.sendmail(_user, _to, msg.as_string())#发送邮件
    rm_file(filelist,PATH)
    s.close()
except Exception
    print(e)
finally:
        s.close()

