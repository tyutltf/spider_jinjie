import json

str='''
[{
"name":"ltf",
"gender":"male",
"birthday":"1997-04-04"
},{
"name":"lsq",
"gender":"female",
"birthday":"1998-05-18"
}]
'''
print(type(str))
data=json.loads(str)
print(data)
print(type(data))
print(data[0])
print(data[0].get('name'))
print(data[1].get('age'))  #不会报错 只会输出None
print(data[1].get('age',25))  #可以传参数

#输出JSON
data1=[{
"name":"ltf",
"gender":"male",
"birthday":"1997-04-04"
}]
with open('data1.json','w') as file:
    file.write(json.dumps(data1,indent=2))

#中文JSON保存文件
data2=[{
"name":"梁腾飞",
"gender":"男性",
"birthday":"1997-04-04"
}]
with open('data2.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data2,indent=2,ensure_ascii=False))

