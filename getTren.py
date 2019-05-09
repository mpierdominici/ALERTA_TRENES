import requests
import json
#fuente
#https://github.com/Fermoto5HD/proximo-tren/blob/master/js/tracker.js
clientId='8a1267e3bc2a4b3594d0bdcb2d6354c4'
clientSecret='45C42645a4bb4535AAf3dE8f26050Ec4'
uurl='https://apitransporte.buenosaires.gob.ar/trenes/tripUpdates'

pparam={'client_id':clientId,'client_secret':clientSecret,'json':'1'} #mitre tigre

r=requests.get(url=uurl,params=pparam)
parsed=r.json()
trenesMitre=[]


for x in parsed['entity']:
    if((x['trip_update']['trip']['route_id'])=='5'):
        trenesMitre.append(x)

#0: SCHEDULED
#1: ADDED
#2: UNSCHEDULED
#3: CANCELED
#5: REPLACEMENT
for x in trenesMitre:
    if((x['trip_update']['trip']['schedule_relationship'])!=0):
        print('Cuidado')


print('hola')