import pymysql

#  新建数据库对象 （建立链接）
mysql = pymysql.connect(host="127.0.0.1", user="root", password="root", database="books", charset="utf8")

#  创建游标对象（获取游标）
cursor = mysql.cursor()
# 使用游标对象执行sql查询命令
cursor.execute("select version();")  # select version()查询sql版本
print(cursor.fetchone())

# 输出游标指针行数据
cursor.execute("select * from t_hero;")
print(cursor.fetchone())

# 输出游标指针下一行数据
# 打印结果
# print(cursor.fetchone())

# 输出剩余的全部游标指针
# 打印结果
# print(cursor.fetchall())
#
# sql语句中 read和comment为关键字 需要使用`read`,`comment` （`）符号标识出这是一个普通字段
cursor.execute("select id,title,`read`,`comment` from t_book;")
for i in cursor.fetchall():
    print(i)

# 关闭游标
cursor.close()
# 关闭链接
mysql.close()
