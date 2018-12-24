import csv


with open('data.csv','w')as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001', 'ltf', '21'])
    writer.writerow(['10002', 'lsq', '22'])
    writer.writerow(['10003', 'lhw', '20'])
    writer.writerow(['10004', 'fjf', '21'])
    writer.writerows([['10005','lgb','20'],['10005','lgb','20'],['10005','lgb','20']])

#字典化数据
with open('data1.csv','w')as csvfile1:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile1,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'ltf','age':'20'})
    writer.writerows([{'id': '10002', 'name': 'lsq', 'age': '20'},{'id': '10003', 'name': 'lhw', 'age': '20'},])

#中文追加写入
with open('data1.csv','a',encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10004','name':'梁腾飞','age':'十八岁'})



#读取csv文件
with open('data1.csv','r',encoding='utf-8')as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)

#pandas库的read_csv 方法
import pandas as pd
df=pd.read_csv('data1.csv')
print(df)
