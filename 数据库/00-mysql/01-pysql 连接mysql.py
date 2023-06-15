import pymysql

# 1.创建链接对象
conn = pymysql.Connect(
    host='127.0.0.1',  # 数据库服务器主机地址
    port=3306,  # mysql的端口号
    user='root',  # 数据库的用户名
    password='boboadmin',  # 数据库密码
    db='AnHui',  # 数据仓库的名称
    charset='utf8')
# 创建一个游标对象
cursor = conn.cursor()
# 2.增加记录操作
# sql = 'insert into emp(name,sex,age,dep_id)values(&quot;%s&quot;,&quot;%s&quot;,%d,%d)'%('haha','female',20,200)
# cursor.execute(sql)
# conn.commit() #对数据进行整改后，记得进行事物的提交

# 3.删除记录
# sql = 'delete from emp where name = &quot;%s&quot;'%'haha'
# print(sql)
# cursor.execute(sql)
# conn.commit()

# 4.修改操作
# new_age = input('enter a new age:')
# new_age = int(new_age)
# sql = 'update emp set age = %d where id = 3'%new_age
# print(sql)
# cursor.execute(sql)
# conn.commit()

# 查询操作
sql = 'select * from emp where age &gt; 30'
cursor.execute(sql)  # 负责执行sql语句
# fetchall返回的是一个元组，元组元素又为一个元素，该元组中存储的是查询到的一条记录
# all_data = cusor.fetchall() #获取查询到所有的数据，如果没有查询到数据返回一个空元组
# print(all_data)

# fetchone只会返回查询到的第一条数据
one_data = cursor.fetchone()  # 如果没有查询到数据返回None
print(one_data)

# 关闭打开的资源对象
cursor.close()
conn.close()
