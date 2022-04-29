# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/19 14:13
# @Author   :Administrator
# @File :db.py
# @Description:
# ------------------------------
import logging
from AutoTestProject.tools.readconfig import ReadConfig




class DB:
    @classmethod
    def getConn(cls):
        import psycopg2
        contents = ReadConfig.read_configAsjson('../config/config.json')
        return psycopg2.connect(database=contents['postgreSQL']['database'],
                                user=contents['postgreSQL']['user'],
                                password=contents['postgreSQL']['password'],
                                host=contents['postgreSQL']['host'],
                                port=contents['postgreSQL']['port'])


    '''
    description:        query_one_forsql
                        查询一条数据库记录
    '''


    @classmethod
    def query_one_forsql(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            result = cur.fetchone()[0]
        except Exception as e:
            conn.rollback()
            logging.exception(e)
            result = None
        finally:
            cur.close()
            conn.close()
        return result


    '''
    description:        query_all_forsql
                        查询多条数据库记录
    '''


    @classmethod
    def query_all_forsql(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            result = cur.fetchall()
        except Exception as e:
            conn.rollback()
            logging.exception(e)
            result = None

        finally:
            cur.close()
            conn.close()
        return result


    '''
    description:        update_data
                        增删改操作
    '''


    @classmethod
    def update_data(cls, sql):
        flag = False
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            flag = True
        except Exception as e:
            conn.rollback()
            logging.exception(e)
            flag = False
        finally:
            cur.close()
            conn.close()
            return flag