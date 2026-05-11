import requests
#
def sec(text):
    print("---"*5, text, "---"*5)
#
# # # sendMessage
sec('sendMessage')
token = "8237583362:AAEV73uiXJ7nqrbKng8-i1RxbH7anrq9Mno"
chat_id=8551788907
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendMessage',
    data={
        'chat_id': chat_id,
        'text': "salom"
    }
).json()
print(response)

# sendDice
sec("sendDice")
method = 'sendDice'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': chat_id, 'emoji': '🎳'}
).json()
print(response)

# # getUpdates
sec('getUpdates')
response = requests.get(
    url=f'https://api.telegram.org/bot{token}/getUpdates'
).json()
print(response)

sec("send_photo_url  orqali")

response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendDocument',
    data={
        "chat_id": chat_id,
        "document": "https://store-images.s-microsoft.com/image/apps.55245.13537716651231321.3067a421-6c2f-48a9-b77c-1e38e19146e6.10e2aa49-52ca-4e79-9a61-b6422978afb9",
        "caption": "Telegramning rasmi"
    }
).json()
print(response)
sec("send_Location")

response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendLocation',
    data={
        "chat_id": chat_id,
        'latitude':41.5634243994903,
        "longitude": 60.58831276487031
    }
).json()
print(response)

sec("sendAudio")
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendAudio',
    data={
        "chat_id": chat_id},
     files={"audio": open('CHIVAS.mp3', 'rb')}
).json()
print(response)

sec("sendVideo")
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendVideo',
    data={"chat_id": chat_id},
    files={"video": open("video.mp4", "rb")}
).json()
print(response)

sec("sendContact")
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendContact',
    data={
        "chat_id": chat_id,
        "phone_number": "+998878416662",
        "first_name": "Azamat",
        "last_name": "Sobirov"
    }
).json()
print(response)
sec("sendPoll")
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendPoll',
    data={
        "chat_id": chat_id,
        "question": "Qaysi til yaxshi?",
        "options": '["Python", "Java", "JavaScript"]',
        "is_anonymous": False
    }
).json()
print(response)

sec("editMessageText")
text = requests.post(
    url=f'https://api.telegram.org/bot{token}/sendMessage',
    data={
        "chat_id": chat_id,
        "text": "Eski matn"
    }
).json()
# 2-qism
message_id = text['result']['message_id']

response = requests.post(
    url=f'https://api.telegram.org/bot{token}/editMessageText',
    data={
        "chat_id": chat_id,
        "message_id": message_id,
        "text": "Yangilangan matn! ✅"
    }
).json()
print(response)






