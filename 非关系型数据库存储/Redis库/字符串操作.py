from redis import StrictRedis,ConnectionPool

#另一种连接方式
pool=ConnectionPool(host='localhost',port=6379,db=0,password=None)
redis=StrictRedis(connection_pool=pool)

#redis.set('name','Bob')
print(redis.get('name'))

#print(redis.getset('name','Mike'))  #赋值name为Mike并返回上一次的value

print(redis.mget(['name','age']))   #输出name键和age键的value

#print(redis.setnx('newname','james'))  #如果键值不存在，则赋值

#print(redis.mset({'name1':'smith','name2':'curry'}))  #批量赋值

#print(redis.msetnx({'name3':'ltf','name4':'lsq'}))    #不存在才批量赋值

#print(redis.incr('age',1))   #age对应的value 加1
#print(redis.decr('age',5))   #age对应的value 减5

#print(redis.append('name4','is a sb'))   #在name4的value后追加 is a sb 返回字符串长度

print(redis.substr('name',1,4))   #截取键 name
print(redis.getrange('name',0,-1))  #截取键 name

