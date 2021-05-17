# -*- coding: utf-8 -*-
# @Time       :   2021-04-30 19:24
# @Author     :   XrazYang
# @File       :   yunpian.py
# @Project    :   emooc


import requests
import json


def send_single_sms(apikey, code, mobile):
    # 发送单条短信
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "【个人编程学习】您的验证码是{}。如非本人操作，请忽略本短信".format(code)

    res = requests.post(url, data={
        "apikey": apikey,
        "mobile": mobile,
        "text": text
    })
    re_json = json.loads(res.text)
    return re_json


if __name__ == "__main__":
    res_json = send_single_sms("8658a93161922fe6e27974372f12d8f9", "1234", "17608728477")

    code = res_json["code"]
    msg = res_json["msg"]
    if code == 0:
        print("发送成功", res_json)
    else:
        print("发送失败: {}".format(msg))
