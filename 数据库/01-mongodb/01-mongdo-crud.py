import pymongo
from pymongo import MongoClient

#创建返回链接对象
def get_db(database):
    client = MongoClient(host="localhost", port=27017)
    db = client[database]
    return db


# 增删改查
# 增加数据
def add_one(table, data):
    db = get_db("python")
    result = db[table].insert_one(data)
    return result


def add_many(table, data_list):
    db = get_db("python")
    result = db[table].insert_many(data_list)
    return result.inserted_ids


def upd(table, condition, data):#condition条件
    db = get_db("python")
    result = db[table].update_many(condition, {'$set':data})
    return result


def delete(table, condition):#condition条件
    db = get_db("python")
    result = db[table].delete_many(condition)
    return result


if __name__ == '__main__':
    # r = add_one("stu", {"name": "西瓜", "age":18})
    # print(r.inserted_id)
    # r = add_many("stu", [{"name": "嘎嘎"},{"name": "咔咔"}])
    # print(r)

    # result = upd("stu", {"name": '西瓜'}, {"age": 100})
    # print(result)

    result = delete("stu", {"name": "嘎嘎"})
    print(result)