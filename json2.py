import json
path="C:\\Users\\gopi\\Desktop\\gopi.py\\input1.json"
f=open(path,"r")
data=f.read()
f.close()
print(data)
d=json.loads(data)
print(d.keys())
print(d.values())
