import pymysql

connect = pymysql.connect(host="127.0.0.1", user="root", password="root",database="books", charset="utf8", port=3306)
   # autocommit=True 自动提交事务
cursor = connect.cursor()
# 定义要执行的sql语句
insert_data_book = """insert into t_book VALUES (DEFAULT,"feiren","1980-11-11",30,50,0)"""
insert_data_hero = """insert into t_hero VALUES (DEFAULT,"张海某",1,"飞龙在天",0,1)"""

try:
    cursor.execute(insert_data_book)
    cursor.execute(insert_data_hero)
    # 如果没有异常 执行提交事务
    connect.commit()
except Exception as e:
    print(e)
    # 如果发生异常 回滚操作
    connect.rollback()
# 手动提交事务


cursor.close()
connect.close()