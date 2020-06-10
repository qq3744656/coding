import pymysql

#  新建数据库对象 （建立链接）
mysql = pymysql.connect("127.0.0.1","root","root","books")

#  创建游标对象（获取游标）
cursor = mysql.cursor()
# 使用游标对象执行sql查询命令
cursor.execute("select version();")       # select version()查询sql版本

# 打印结果
print(cursor.fetchone())

# 关闭游标
cursor.close()
# 关闭链接
mysql.close()