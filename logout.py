#!/usr/bin/env python  
# -*- coding=utf-8 -*-
# 北邮校园网自动注销
import getpass
import urllib2
import urllib
import re


class Logouter():
    def __init__(self):
        self.logoutUrl = 'http://10.3.8.211/F.htm'
      

    def logout(self):
       
      
        result = urllib2.urlopen(self.logoutUrl).read()
        unicodePage = result.decode('gb2312')

        self.state(unicodePage)


    def state(self, result):
        pattern_msg = re.compile(r'Msg=(\d{1,2})')
        pattern_time = re.compile(r"time='(\d+)")
        pattern_flow =  re.compile(r"flow='(\d+)")
        pattern_fee =  re.compile(r"fee='(\d+)")
        Msg = int(re.search(pattern_msg, result).group(1))
        time =int( re.search(pattern_time,result).group(1))
        flow = int(re.search(pattern_flow,result).group(1))
        fee = int(re.search(pattern_fee,result).group(1))
        flow0=flow%1024
        flow1=flow-flow0
        flow0=flow0*1000
        flow0=flow0-flow0%1024
        flow3='.'
        fee1=fee-fee%100;
        
        if Msg == 14:
            print u'注销成功'
            print u"已使用时间 Used time : " ,time, " Min"
            print u"已使用校外流量 Used internet traffic : ", flow1/1024, '.' , flow0/1024  ," MByte"
            print u"本账号余额  Balance : RMB",float(fee1)/10000
                
        else:
            print u'未登录或出错'


def main():
    l = Logouter()
    l.logout()


if __name__ == '__main__':
    main()