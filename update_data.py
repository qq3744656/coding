import pymysql

connect = pymysql.connect(host="127.0.0.1", user="root", password="root",database="books", charset="utf8",
                          autocommit=True, port=3306)

cursor = connect.cursor()

update_data="""UPDATE t_book set `read` = `read`+30 WHERE id = 4"""

cursor.execute(update_data)

cursor.close()
connect.close()