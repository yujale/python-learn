import redis

# 创建链接对象
conn = redis.Redis(host='127.0.0.1', port=6379)
# 插入数据
# result = conn.sadd('class','num4')
# print(result)

# result = conn.lpush('hobby','haha')
# print(result)

# 查询set集合里的数据
print(conn.smembers('class'))
