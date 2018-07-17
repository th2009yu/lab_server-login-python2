#!/usr/bin/env python  
# -*- coding:utf-8 -*-
# 北邮校园网自动登录
import getpass
import urllib2
import urllib
import re


class Loginer():
    def __init__(self, username, password):
        self.loginUrl = 'http://10.3.8.211/'
        self.username = username
        self.password = password
        self.openner = urllib2.build_opener()


    @staticmethod
    def error_fun(Msg):
        if Msg == 1:
            print u"账户名或者密码错误"
        elif Msg == 2:
            print u"该帐号正在其他机子上使用"
        elif Msg == 4:
            print u"费用超出"
        else:
            print u"未知错误，请用浏览器登录！"

    def login(self):
        postdata = {
            'DDDDD': self.username,
            'upass': self.password,
            'savePWD': 0,
            '0MKKey': ''
        }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)

        result = self.openner.open(myRequest).read()
        # result = urllib2.urlopen(myRequest).read()
        unicodePage = result.decode('gb2312')

        self.state(unicodePage)

        # msg = re.findall('<title>(.*?)</title>', unicodePage)[0]
        # if msg.encode('utf-8') == '登录成功窗':
        #     print u'账号：', self.username, u'    登录成功！'
        # else:
        #     print u'账号：', self.username, u'    登录失败！'

    def state(self, result):
        title = re.findall('<title>(.*?)</title>', result)[0]
        if title.encode('utf-8') == '登录成功窗':
            print u'账号：', self.username, u'    登录成功！'
        else:
            pattern_msg = re.compile(r'Msg=(\d{1,2})')
            pattern_xip = re.compile(r"xip='((\d{1,3}.){3}\d{1,3})")
            Msg = int(re.search(pattern_msg, result).group(1))
            self.error_fun(Msg)
            if Msg == 2:
                xip = re.search(pattern_xip,result).group(1)
                print u'请下线: '+xip


def main():
    username = raw_input("Input your username:   ")
    passwd = getpass.getpass("Input your passwd :   ")
    l = Loginer(username, passwd)
    l.login()


if __name__ == '__main__':
    main()