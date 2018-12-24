from redis import StrictRedis

redis=StrictRedis(host='localhost',port=6379,db=0,password=None)

#print(redis.rpush('list',1,2,3)) #向键名为list的列表尾部添加1,2,3 返回长度

#print(redis.lpush('list',0))   #向键名为list的列表头部添加0 返回长度

print(redis.llen('list'))   #返回列表的长度

print(redis.lrange('list',1,3))  #返回起始索引为1 终止索引为3的索引范围对应的列表

print(redis.lindex('list',1))   #返回索引为1的元素-value

#print(redis.lset('list',1,5))  #将list的列表索引为1的重新赋值为5

#print(redis.lpop('list'))  #删除list第一个元素

#print(redis.rpop('list'))   #删除list最后一个元素

#print(redis.blpop('list'))   #删除list第一个元素

#print(redis.brpop('list'))    #删除最后一个元素

print(redis.rpoplpush('list','list1'))   #删除list的尾元素并将其添加到list1的头部