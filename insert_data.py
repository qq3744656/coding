import pymysql

#  新建数据库对象 （建立链接）
connect = pymysql.connect(host="127.0.0.1", user="root", password="root", database="books", autocommit=True,
                          port=3306, charset="utf8")
#  创建游标对象（获取游标）
cursor = connect.cursor()

# 使用游标对象执行新增操作
delete_data = """DELETE FROM t_book WHERE title = "阿里嘎多" """
cursor.execute(delete_data)

# 关闭游标
cursor.close()

# 关闭链接
connect.close()
