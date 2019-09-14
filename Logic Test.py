import json
from datetime import datetime, timedelta

config = json.loads(open('U1ZQR43RB.json').read())

dicts={}

for line in range(len(config)):
    start = config[line]['ts']
    
    if not dicts.__contains__(config[line]['user']):
        dicts.update({config[line]['user']:{}})
        dicts[config[line]['user']].update({start:[]})

    find=False
    for user_time in dicts[config[line]['user']].keys():
        end_time = datetime.timestamp(datetime.fromtimestamp(float(user_time)) + timedelta(minutes=2))    
        if float(start) <= float(end_time): 
            dicts[config[line]['user']][user_time].append(config[line])
            find=True
        
    if not find: 
        dicts[config[line]['user']].update({start: [config[line]]})
    

for user in dicts.keys():
    with open(user+'.json', 'w') as file:
        json.dump(dicts[user],file)