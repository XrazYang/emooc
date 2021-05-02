# -*- coding: utf-8 -*-
# @Time       :   2021-05-02 13:42
# @Author     :   XrazYang
# @File       :   vonage.py
# @Project    :   emooc


import vonage

client = vonage.Client(key="52c5e8ce", secret="d1MuDjwDB5fNr8AO")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "8619898819744",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

print(responseData)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
