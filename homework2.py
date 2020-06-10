import pymysql

connect = pymysql.connect(host="127.0.0.1", user="root", password="root", database="books", autocommit=True,
                          port=3306, charset="utf8")
cursor = connect.cursor()
# .使用pymysql操作MySQL数据库，具体操作如下： 1).在“books”数据库中，新增评论表t_comment， 包含字段：主键、图书id、评论人名称、评论内容、评论时间。
cursor.execute("""
    CREATE TABLE `t_comment`  (
  `id` int(11) NOT NULL ,
  `comment_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `comment_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `comment_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) """)
# 2).在评论表中新增一条数据，并更新图书表t_book中的评论量comment字段。
id = 2
insert_data_book = 'insert into t_comment VALUES (%s,"zhj","好看","1980-11-11") ' % id
cursor.execute(insert_data_book)
update = """ UPDATE t_book set `read` = `read`+1 WHERE id = %s """ % id
cursor.execute(update)
cursor.close()

connect.close()