import requests
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
    r=requests.get('https://api.opendota.com/api/matches/{}'.format(match_id),timeout=3)
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
        return j1,j2
