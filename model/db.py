import pymysql
# while True:
#     user=input("用户名：")
#     if user.upper()=="Q":
#         break
#     id=input("号码：")
#     pwd=input("密码：")
#     rid=input("叫密码：")
#
#
#     conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='czh204627', charset='utf8',db='web')
#     cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#     sql="insert into user(id,username,password_hash,role_id) values(%s,%s,%s,%s)"
#
#     cursor.execute(sql,[id,user,pwd,rid])
#     conn.commit()
#
#     cursor.close()
#     conn.close()

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='czh204627', charset='utf8',db='web')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

sql="insert into user(id,username,password_hash,role_id) values(%s,%s,%s,%s)"

cursor.execute("delete from user where id>1")
conn.commit()
cursor.execute("select * from user")
data=cursor.fetchall()
for row in data:
    print(data)

cursor.close()
conn.close()