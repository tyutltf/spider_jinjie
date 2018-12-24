import pymongo

#连接 MongoDB
client=pymongo.MongoClient(host='localhost',port=27017)

#第二种连接方式
#client=pymongo.MongoClient('mongodb://localhost:27017/')

#指定数据库
db=client.test
#第二种指定方式
#db=client['test']

#指定集合
collection=db.students

#collection=db['students']


#插入数据
student={
    'id':'201812121',
    'name':'ltf',
    'age':'21',
    'gender':'male'
}
result=collection.insert(student)
print(result)

student1={
    'id':'201812122',
    'name':'lsq',
    'age':'21',
    'gender':'female'
}
student2={
    'id':'201812123',
    'name':'lhw',
    'age':'20',
    'gender':'male'
}
result1=collection.insert([student1,student2])
print(result1)


student3={
    'id':'201812124',
    'name':'bz',
    'age':'21',
    'gender':'female'
}
student4={
    'id':'201812125',
    'name':'zn',
    'age':'20',
    'gender':'male'
}
result2=collection.insert_many([student3,student4])
print(result2)
print(result2.inserted_ids)


#查询数据
result3=collection.find_one({'name':'ltf'})
print(type(result3))
print(result3)