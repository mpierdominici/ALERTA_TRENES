import requests
import telebot
import time
import threading
#0: SCHEDULED
#1: ADDED
#2: UNSCHEDULED
#3: CANCELED
#5: REPLACEMENT
def getTigreMitreStatus():
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

    status=[]
    for x in trenesMitre:
        status.append((x['trip_update']['trip']['schedule_relationship']))
    return status

def suscrivirse(chatid):
    path='list2send.txt'
    file=open(path,'a')
    file.write(str(chatid)+'\n')
    file.close()

def getSuscriptors():
    path = 'list2send.txt'
    file = open(path, 'r')
    data=file.readlines()
    file.close()
    temp=set(data)
    toReturn=[]
    for x in temp:
        toReturn.append(x.replace('\n',''))
    return toReturn

def mythread(bot):
    while True :
        sus = getSuscriptors()
        sus = list(sus)
        estado = getTigreMitreStatus()
        temp = 0

        for x in estado:
            temp = temp + x
        if temp!=0:
            for x in sus:
                if x!='':
                    bot.send_message(int(x),'Falla en el servicio')

        time.sleep(35)

token='801847099:AAEp9NqLjCzJkJbpRCuAiN5sDg39b1C0Yz0' #token del bot
bot=telebot.TeleBot(token)

sus=getSuscriptors()
sus=list(sus)

#for x in sus:
#    if x!='':
#        bot.send_message(int(x),'Prueba de difudion')

estado=getTigreMitreStatus()



#bot.send_message(768347055,'hola gil')

@bot.message_handler(commands='suscribirse')
def command_suscribirse(message):
    try:
        suscrivirse(message.chat.id)
        bot.reply_to(message, "Gracias por suscrivirse")
    except:
        bot.reply_to(message, "Suscricion fallida")


@bot.message_handler(commands='estado')
def command_estado(message):
    estado = getTigreMitreStatus()
    temp=0
    data2send='Servicio funciona normal'
    for x in estado:
        temp=temp+x

    if temp!=0:
        data2send='Hay problemas en el servicio'

    bot.reply_to(message, data2send)


x = threading.Thread(target=mythread, args=(bot,))
x.start()

bot.polling(none_stop=False)




