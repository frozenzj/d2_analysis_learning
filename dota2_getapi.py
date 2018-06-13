import requests
import time
import json
#EZ output random match_id
def get_ran_match_id(limi=1):
#    def ransql(limi=1):
    i=0
    rec=[]
    sql='''select matches.match_id
    from matches
    order by random()
    limit %s'''%(limi)
#        return sql
    r=requests.get('https://api.opendota.com/api/explorer?sql={}'.format(sql),timeout=3)
    r_json=r.json()
    rMi=r_json['rows']
#        return rMi
    for i in range(len(rMi)):
        rec.append(rMi[i]['match_id'])
    return rec
#output match_info by match_id
def get_api_json(match_id):
    r=requests.get('https://api.opendota.com/api/matches/{}'.format(match_id))
    r_json=r.json()
    return r_json
#TEAM_GOLD
#match_info = apimatch.json()    slot_s = start slot num.   slot_e = end slot num.
def get_totalgold(match_info,slot_s=0,slot_e=5,matchtype=1):
    i=0
    j1=0
    k1=0
    j2=0
    k2=0
    r_w=bool
    if matchtype==1:
        for i in range(slot_s,slot_e):
            k1=match_info['players'][i]['total_gold']
            j1=j1+k1
        return j1
    elif matchtype==2:
        for i in range(0,10):
            if match_info['players'][i]['player_slot']<10:
                k1=match_info['players'][i]['total_gold']
                j1=j1+k1
            else:
                k2=match_info['players'][i]['total_gold']
                j2=j2+k2
        if match_info['radiant_win']==True:
            r_w=True
        else:
            r_w=False
        return j1,j2,r_w
def get_sleep_api(id,sleepT=1):
    #define i,minfo200
    i=0
    minfo200=[]
    #sleep module to get match_info
    for i in range(len(id)):
        minfo200.append(get_api_json(id[i]))
        time.sleep(int(sleepT))
    #define i,k,matchid_from_minfo200
    i=0
    k=[]
    mid_from_minfo200=[]
    #judge 'error' information & miss match_info -->return minfo200
    for i in range(len(minfo200)):
        if 'error' in minfo200[i]:
            k.append(i)
    if len(k)!=0:
        print("Rate limit exceeded!!!")
        return minfo200
    else:
        if len(id)==len(minfo200):
            print("All done!")
            return minfo200
        else:
            i=0
            for i in range(len(minfo200)):
                mid_from_minfo200.append(minfo200[i]['match_id'])
            i=0
            for i in range(len(id)):
                if id[i] not in mid_from_minfo200:
                    k.append(id[i])
                    minfo200=minfo200+k
            print("Match_id:"+k+" is missing,Already fixed it!")
            return minfo200
