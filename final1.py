import json
with open('Data/final.json') as f:
    allcoms = json.load(f)
n1 =[]
for coms in allcoms:
    for com in coms:
        n1.append(com)
print(n1)
with open('Data/final.json','w') as f:
    json.dump(n1,f,ensure_ascii=False)