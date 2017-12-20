# -*- coding: UTF-8 -*-

from com.crawling.config.readConfig import ReadConfig
import pymysql
import time

class SqlHelper:
    def __init__(self):
        config = ReadConfig()
        self.__db = config.getDatabase()["log"]

    # 根据sql进行 增删改
    def sqlExecute(self,sql):
        try:
            with self.__db.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql);
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.__db.commit()
        except Exception as e:
            # 错误回滚
            self.__db.rollback()
        finally:
            print('sqlExecute在'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'被执行'+'||'+sql)
            #self.__db.close();

    # 根据sql和list中的参数进行 增删改
    def sqlExecute(self,sql,list):
        try:
            with self.__db.cursor() as cursor:
                cursor.execute(sql,list);
                self.__db.commit();
        except Exception as e:
            self.__db.rollback();
        finally:
            print('sqlExecute在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '被执行' + '||' + sql)
            #self.__db.close();

    #根据sql进行查询
    def sqlQuery(self,sql):
        try:
            with self.__db.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql);
                return cursor.fetchall();
        except Exception as e:
            raise e;
        finally:
            print('sqlQuery在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '被执行' + '||' + sql)
            #self.__db.close();

    def insertByTable(self,table,map):
        sql = '';
        columns = '';
        values = '';

        for key in map:
            columns += key + ',';
            values += "'" + map[key] + "',";
        if columns != '':
            columns = columns.RTrim(',');
        if values != '':
            values = columns.RTrim(',');
        sql += 'insert ' + table + '('+columns+') ' + ' values('+values+')'

        try:
            with self.__db.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql);
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.__db.commit();
        except Exception as e:
            # 错误回滚
            self.__db.rollback();
        finally:
            print('insertByTable在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '被执行' + '||' + table + ' || ' + sql)
            #self.__db.close();

    def updateByTableId(self,table,map,id):
        sql = 'update ' + table + ' set ';

        for key in map:
            sql += key + "= '" + map[key] + "' , ";

        if len(map) > 0:
            sql=sql.RTrim(',');

        sql += " where id = %d";

        try:
            with self.__db.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql % (int(id)));
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.__db.commit();
        except Exception as e:
            # 错误回滚
            self.__db.rollback();
        finally:
            print('insertByTable在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '被执行' + '||' + table + ' || ' + sql)
            #self.__db.close();

    def deleteByTableId(self,table,id):
        sql = "delete from "+ table +" where id = %d";
        try:
            with self.__db.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql % (int(id)));
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.__db.commit();
        except Exception as e:
            # 错误回滚
            self.__db.rollback();
        finally:
            print('deleteByTableId在' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '被执行' + '||' + table + ' || ' + sql)
            #self.__db.close();