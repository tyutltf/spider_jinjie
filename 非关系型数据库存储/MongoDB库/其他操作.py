import pymongo

#连接 MongoDB
client=pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db=client.test
#指定集合
collection=db.students

#计数
count=collection.find().count()
print(count)   #统计所有数量

count=collection.find({'age':'20'}).count()
print(count)   #统计年龄为20的数量

#排序
results=collection.find().sort('name',pymongo.ASCENDING)
print([result['name']for result in results])  #升序

results=collection.find().sort('name',pymongo.DESCENDING)
print([result['name']for result in results])  #降序

#偏移
results=collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name']for result in results])  #升序偏移2 即从第三个数据开始输出

results=collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(8)
print([result['name']for result in results])  #升序偏移2 即从第三个数据开始输出 limit限制8个

#更新
condition={'name':'ltf'}
student=collection.find_one(condition)
student['age']='25'
result=collection.update(condition,student)
print(result)

'''
#删除
result=collection.remove({'name':'bz'})
print(result)  #成功一个

result=collection.delete_one({'name':'zn'})
print(result)
print(result.deleted_count) #删除bn

result=collection.delete_many({'age':{'$gt':'20'}})
print(result.deleted_count) #删除bn
'''