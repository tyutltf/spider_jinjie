from redis import StrictRedis,ConnectionPool

pool=ConnectionPool(host='localhost',port=6379,db=0,password=None)
redis=StrictRedis(connection_pool=pool)

#print(redis.sadd('tags','Book','Tea','Coffee'))  #返回集合长度 3

#print(redis.srem('tags','Book'))  返回删除的数据个数

#print(redis.spop('tags'))   #随机删除并返回该元素

#print(redis.smove('tags','tags1','Coffee'))

print(redis.scard('tags'))  #获取tags集合的元素个数

print(redis.sismember('tags','Book'))   #判断Book是否在tags的集合中

print(redis.sinter('tags','tags1'))    #返回集合tags和集合tags1的交集

print(redis.sunion('tags','tags1'))    #返回集合tags和集合tags1的并集

print(redis.sdiff('tags','tags1'))     #返回集合tags和集合tags1的差集

print(redis.smembers('tags'))     #返回集合tags的所有元素

print(redis.srandmember('tags'))   #返回tags的一个随机元素