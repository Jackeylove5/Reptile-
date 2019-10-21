import json

# 1.json-->字典
json_str='{"username":"ll","age":"21"}'
# 获取到字典
dic= json.loads(json_str)
print(dic)   # {'username': 'll', 'age': '21'}
print(type(dic))       # <class 'dict'>

# 2.字典-->json
jso=json.dumps(dic,ensure_ascii=False,indent=2)
print(jso)   # {"username": "ll","age": "21"}
print(type(jso))      # <class 'str'>

# 3.json-->文件
with open('demo.json','w',encoding='utf-8') as f:
    json.dump(jso,f,ensure_ascii=False)

# 4.读取json文件
with open('demo.json','r',encoding='utf-8') as f:
    print(json.load(f))    # {"username": "ll","age": "21"}