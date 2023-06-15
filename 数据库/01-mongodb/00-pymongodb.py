import pymongo

conn = pymongo.MongoClient(host='localhost', port=27017)
# 切换数据库
py = conn['python']
# 登录该数据库(需要的话)
# py.authenticate("python_admin", '123456')
# 简单来个查询
result = py["stu"].find()
for r in result:
    print(r)
