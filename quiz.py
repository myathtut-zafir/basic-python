s = 'hello'
list3 = [1,2,[3,4,'hello']]
list3[2][2]="goodbye"
list4 = [5,3,4,6,1]
list4.sort()
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
value=d['k1'][0]['nest_key'][1]
string = ','.join(str(x) for x in value)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
string2=d['k1'][2]['k2'][1]['tough'][2]
print(','.join(str(x) for x in string2))

list5 = [1,2,2,33,4,4,11,22,3,5,3,2]
myset=set(list5)
print(myset)