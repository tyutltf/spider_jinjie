import pymongo

#连接 MongoDB
client=pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db=client.test
#指定集合
collection=db.students

#查询数据
result=collection.find_one({'name':'ltf'})
print(type(result))
print(result)

#查询多条数据
results=collection.find({'age':'20'})
print(results)
for result in results:
    print(result)

print('===='*20)
#查询年龄大于20
resultss=collection.find({'age':{'$gt':'20'}})
for result1 in resultss:
    print(result1)

print('===='*20)
#正则匹配查询
results=collection.find({'name':{'$regex':'^ltf.*'}})
for result in results:
    print(result)
#属性是否存在
results=collection.find({'name':{'$exists':True}})
for result in results:
    print(result)

#文本查询
results=collection.find({'$text':{'$search':'ltf'}})
print(results)

