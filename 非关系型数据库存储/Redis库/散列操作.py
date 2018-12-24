from redis import StrictRedis,ConnectionPool

pool=ConnectionPool(host='localhost',port=6379,db=0,password=None)
redis=StrictRedis(connection_pool=pool)

#print(redis.hset('price','cake',5))  # 向键名为price的散列表添加映射关系，返回1 即添加的映射个数

#print(redis.hsetnx('price','book',6)) # 向键名为price的散列表添加映射关系，返回1 即添加的映射个数

print(redis.hget('price','cake'))  #获取键名为cake的值 返回5

#print(redis.hmset('price',{'banana':2,'apple':3,'pear':6,'orange':7}))   #批量添加映射

print(redis.hmget('price',['apple','orange']))   #查询apple和orange的值 输出 b'3',b'7'

#print(redis.hincrby('price','apple',3))   #apple映射加3 为6

print(redis.hexists('price','banana'))    #在price中banana是否存在  返回True

#print(redis.hdel('price','banana'))    #从price中删除banana 返回1

print(redis.hlen('price'))   #输出price的长度

print(redis.hkeys('price'))  #输出所有的映射键名

print(redis.hvals('price'))  #输出所有的映射键值

print(redis.hgetall('price'))  #输出所有的映射键对