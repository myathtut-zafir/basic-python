names=["a","a","c","b","d"]

nameMap={}
for name in names:
    if name not in nameMap:
        nameMap[name]=1
    else:
        nameMap[name]+=1

print(nameMap)
        