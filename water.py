import requests


def water(cookie):
    headers = {
        'Host': 'api.m.jd.com',
        'x-rp-client': 'h5_1.0.0',
        'user-agent': 'jdapp;android;11.1.2;;;Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36',
        'x-referer-page': 'https://carry.m.jd.com/babelDiy/Zeus/3KSjXqQabiTuD1cJ28QskrpWoBKT/index.html',
        'accept': '*/*',
        'origin': 'https://carry.m.jd.com',
        'x-requested-with': 'com.jingdong.app.mall',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://carry.m.jd.com/',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookie
    }

    response = requests.get(
        'https://api.m.jd.com/client.action?functionId=waterGoodForFarm&appid=wh5',
        headers=headers,
    )
    print(response.text)
    return response.text


if __name__ == "__main__":
    water("ck")
