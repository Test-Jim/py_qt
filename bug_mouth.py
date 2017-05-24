#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time,re,xlwt
from bs4 import  BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class bug_mouth(object):
    def __init__(self):
        self.driver=webdriver.PhantomJS()
        self.driver.get("http://project.kuaiqiangche.cc/index.php?m=bug&f=browse&productID=5&branch=0&browseType=bySearch&queryID=myQueryID")
        self.driver.maximize_window()
    def bug_mouth_spider(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('account').send_keys('jinzhangshuang')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('password').send_keys('jin@#123')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#field1 > option:nth-child(29)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#operator1 > option:nth-child(4)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#value1').send_keys('2016-11-01')
        self.driver.implicitly_wait(30)
        #上面是条件1，下面是条件2
        self.driver.find_element_by_css_selector('#field4 > option:nth-child(29)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#operator4 > option:nth-child(5)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#value4').send_keys('2016-12-01')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(30)
        idls,namels,lvls,stals,authorls,recels,solvels=[],[],[],[],[],[],[]
        pagenum=self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > strong:nth-child(3)').text
        pagenum=pagenum.split('/')[1]
        for i in range(int(pagenum)):
            page = self.driver.page_source
            soup=BeautifulSoup(str(page),"lxml")
            #bugID
            templist=soup.find_all('a',href=re.compile('m=bug&f=view&bugID='),style=None)
            for index in templist:
                idls.append(index.string)
            #bug标题
            templist=soup.find_all('a',style='color: ')
            for index in templist:
                namels.append(index.string)
            #bug等级
            templist=soup.find_all('span',class_=re.compile('severity'))
            for index in templist:
                lvls.append(index.string)
            #bug状态
            templist=soup.find_all('td',class_=re.compile('bug-'),text=True)
            for index in templist:
                stals.append(index.string)
            #（创建者、指派给、bug解决状态）
            parr=re.compile('style="color: ">.*?<td class="bug-.*?">.*?</td>.*?<td>(.*?)</td>\s*<td>.*?</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>',re.S)
            templist=re.findall(parr,str(page))
            for index in range(len(templist)):
                authorls.append(templist[index][0])
                recels.append(templist[index][1])
                solvels.append(templist[index][2])
            if i<int(pagenum)-1:
                self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > a:nth-child(6) > i').click()
                self.driver.implicitly_wait(30)
        self.driver.close()

        excel=xlwt.Workbook(encoding = 'utf-8')
        sheet1=excel.add_sheet(u'当月bug统计',cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = 'SimSun'
        style.font = font
        row0=['bugID','bug标题','bug等级','bug状态','bug作者','bug开发者','结果状态']
        for index in range(0,len(row0)):
            sheet1.write(0,index,row0[index],style)


        for index in range(len(idls)):
            sheet1.write(index+1,0,idls[index],style)
            sheet1.write(index+1,1,namels[index],style)
            sheet1.write(index+1,2,lvls[index],style)
            sheet1.write(index+1,3,stals[index],style)
            sheet1.write(index+1,4,authorls[index],style)
            sheet1.write(index+1,5,recels[index],style)
            sheet1.write(index+1,6,solvels[index],style)
        day=time.strftime('%Y%m',time.localtime(time.time()))
        excel.save(day+'bugs'+'.xlsx')


if __name__=='__main__':
    aa=bug_mouth()
    aa.bug_mouth_spider()