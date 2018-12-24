from redis import StrictRedis

#数据库连接方式 因为就算我自己使用的，所有没有设置密码
redis=StrictRedis(host='localhost',port=6379,db=0,password=None)
#redis.set('age',20)
print(redis.get('name'))

print(redis.exists('name')) #是否存在name这个键

print(redis.type('name'))  #判断name的类型

print(redis.keys('n*'))  #获取所有以n开头的键

print(redis.randomkey())  #获取随机一个键

print(redis.dbsize()) #获取当前数据库中的键的数目



