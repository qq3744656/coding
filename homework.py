import pymysql

#  新建数据库对象 （建立链接）
connect = pymysql.connect(host="127.0.0.1", user="root", password="root", database="books", autocommit=True,
                          port=3306, charset="utf8")
cursor = connect.cursor()
# 插入一本书，书名为‘python从入门到放弃’，# 阅读量为50，评论量为0，发布日志为：2020-01-01
insert_data_book = """insert into t_book VALUES (DEFAULT,"python从入门到放弃","2020-01-01",50,0,0)"""
cursor.execute(insert_data_book)
# 测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的 值：250
update_data="""UPDATE t_book set `comment` = 250 WHERE title = "python从入门到放弃" """
cursor.execute(update_data)
# 老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
delete_data = """DELETE FROM t_book WHERE title = "python从入门到放弃" """
cursor.execute(delete_data)
# 你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？
select_data = """ SELECT * FROM t_book"""
cursor.execute(select_data)
for i in cursor.fetchall():
    print(i)

cursor.close()

connect.close()