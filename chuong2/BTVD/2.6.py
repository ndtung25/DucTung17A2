import json 
 
with open('2.6.json', 'r', encoding='utf-8') as f: 
    content = f.read()
infor = json.loads(content) 
print(infor)