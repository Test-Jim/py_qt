#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb,sys
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

class Mysql():

    @staticmethod
    def connet():
        #连接数据库
        DB=ConfigParser.ConfigParser()
        DB.read('DBconfig.ini')
        host=DB.get('DB','DBhost')
        port=DB.get('DB','DBport')
        user=DB.get('DB','DBuser')
        passwd=DB.get('DB','DBpassword')
        name=DB.get('DB','DBname')
        charset=DB.get('DB','DBcharset')

        conn=MySQLdb.connect(host=host,port=int(port),user=user,passwd=passwd,db=name,charset=charset)
        handle=conn.cursor()
        return handle,conn

    @classmethod
    def inster(cls,handle,mobile,name,password):
        #插入注册用户
        strsql="insert into user (mobile,name,password) values('%s','%s','%s')"%(mobile,name,password)
        handle.execute(strsql)

    @classmethod
    def select_user(cls,handle):
        #搜索用户，判断用户是否已经注册
        strsql="select mobile from user"
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup

    @classmethod
    def select_mobi_pas(cls,handle,mobile):
        #用户登录，判断是否已经注册
        strsql="select mobile,password from user where mobile='%s'"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup

    @classmethod
    def insert_worknumber(cls,handle,bugnum,casenum,gubnum,mobile,day):
        #判断今日工作量是否已经存在，不存在则插入今日工作量
        strsql_1="select * from  worknumber WHERE  mobile='%s' and day='%s'"%(mobile,day)
        handle.execute(strsql_1)
        tup=handle.fetchall()
        if tup:
            return True
        else:
            strsql_2="insert INTO worknumber (bugnum,casenum,gubnum,mobile,day) values('%s','%s','%s','%s','%s')"%(bugnum,casenum,gubnum,mobile,day)
            handle.execute(strsql_2)
            return False

    @classmethod
    def init_data(cls,handle,mobile,day):
        #初始化工作台数据
        strsql_1="select bugnum,casenum,gubnum from worknumber where mobile='%s' and day like '%s%%'"%(mobile,day[0:6])
        handle.execute(strsql_1)
        tup_mouth=handle.fetchall()

        strsql_2="select bugnum,casenum,gubnum,score from worknumber where mobile='%s'"%mobile
        handle.execute(strsql_2)
        tup_all=handle.fetchall()
        return tup_mouth,tup_all

    @classmethod
    def init_user_data(cls,handle,mobile):
        #获取各个成员的名字和分数
        strsql="select name,sum(b.bugnum) as bugsum,sum(b.casenum) as casesum,sum(b.gubnum) as gubsum,sum(b.score)as scoresum " \
               "from user as a INNER JOIN worknumber as b on a.mobile=b.mobile and a.mobile!='%s' GROUP BY  a.name"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup

    @classmethod
    def insert_learn_plan(cls,handle,content,mobile):
        #插入学习计划
        strsql="insert into plan (content,mobile) values ('%s','%s')"%(content,mobile)
        handle.execute(strsql)

    @classmethod
    def select_learn_plan(cls,handle,mobile):
        #查询学习计划
        strsql="select content from plan where mobile='%s'order by id desc limit 2"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup

    @classmethod
    def insert_need(cls,handle,need_id,need_name,need_status,need_day,need_url):
        #插入或者更新需求
        strsql="select need_id from need "
        handle.execute(strsql)
        tup=handle.fetchall()
        id_list=[]
        for index in tup:
            id_list.append(str(index[0]))
        for index in range(len(need_id)):
            if need_id[index] in id_list:
                strsql_1="update need set need_name='%s',need_status='%s',need_day='%s',need_url='%s' where need_id='%s'"\
                    %(need_name[index],need_status[index],need_day,need_url[index],need_id[index])
                handle.execute(strsql_1)
            else:
                strsql_1="insert into need (need_id,need_name,need_status,need_day,need_url,finish_test) VALUES ('%s','%s','%s','%s','%s','%s')"\
                   %(need_id[index],need_name[index],need_status[index],need_day,need_url[index],'未完成')
                handle.execute(strsql_1)
    @classmethod
    def select_need(cls,handle,need_tester):
        #查询需求
        strsql="select need_id,need_name,need_status,need_day,need_url,finish_test from need where need_tester='%s' ORDER BY  finish_test DESC limit 10"%need_tester
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup
    @classmethod
    def select_tester_name(cls,handle,mobile):
        #查询测试人员姓名
        strsql="select name from user where mobile='%s'"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return str(tup[0][0])

    @classmethod
    def select_all_user(cls,handle):
        #查询用户数量
        strsql="select count(*) from user"
        handle.execute(strsql)
        tup=handle.fetchall()
        return int(tup[0][0])

    @classmethod
    def select_score_reason(cls,handle,mobile):
        #查询加减分原因
        strsql="select score,score_reason FROM worknumber WHERE mobile='%s'and score!=0"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup

    @classmethod
    def update_need(cls,handle,idls,endls):
        #更新需求测试状态
        for index in range(len(idls)):
            strsql="update need set finish_test='%s' where need_id='%s'"%(endls[index],idls[index])
            handle.execute(strsql)

    @classmethod
    def select_duty(cls,handle,mobile):
        #每个人的负责模块
        strsql="select duty from user where mobile='%s'"%mobile
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup[0][0]

    @classmethod
    def select_all_need(cls,handle,need_tester):
        #选择所有的个人需求
        strsql="select need_id,need_name,need_status,finish_test from need where need_tester='%s' order by need_id asc"%need_tester
        handle.execute(strsql)
        tup=handle.fetchall()
        return tup






    @classmethod
    def close(cls,handle,conn):
        handle.close()
        conn.close()
