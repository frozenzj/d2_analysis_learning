import timeit
idn=get_ran_match_id(10)
%time get_ran_match_id(5)
%time minfo=list(map(get_api_json,idn))
idx=get_ran_match_id(10)
minfox=list(map(get_api_json,idx))
res=[]
for i in range(len(minfox)):
    res.append(get_totalgold(minfox[i],matchtype=2))
res

#json文件读写方法
import json
#导出json内容（minfo）到“dota_j1.json”文件
with open("dota_j1.json","w") as f:
    json.dump(minfo,f)
#导入json“dota_j1.json”文件到rj1变量
with open("dota_j1.json","r") as f:
    rj1=json.load(f)
