import json

result=open('test_ANSI.txt','r').read()
print(result)

re=open('test_utf8.txt','r',encoding='UTF-8').read()
print(re)

title='我们'
with open('title.txt','a+',encoding='UTF-8') as f:
    f.write(title)
    f.close()

t='我们love你们'
with open('t.json','w',encoding='UTF-8') as f:
    json.dump([t],f,ensure_ascii=False)