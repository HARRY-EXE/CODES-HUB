#Code By Harry Akumaa.

import requests
import random
import re

def pass_to_cuki():
    i = input(f'Enter uid : ')
    p = input(f'Enter password : ')
    ses=requests.Session()
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    fb = ses.get('https://mbasic.facebook.com').text
    data = {
        "lsd":re.search('name="lsd" value="(.*?)"', str(fb)).group(1),
        "jazoest":re.search('name="jazoest" value="(.*?)"', str(fb)).group(1),
        "m_ts":re.search('name="m_ts" value="(.*?)"', str(fb)).group(1),
        "li":re.search('name="li" value="(.*?)"', str(fb)).group(1),
        "try_number":"0",
        "unrecognized_tries":"0",
        "email":i,
        "pass":p,
        "login":"Log In"}
    headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '2',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2006C3MG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',}
    params = {
    'refsrc': 'deprecated',
    'lwv': '100',
    'ref': 'dbl',}
    response = ses.post(
    'https://mbasic.facebook.com/login/device-based/regular/login/',
    params=params,
    headers=headers,
    data=data)
    cookies=ses.cookies.get_dict()
    if 'c_user' in cookies:
        cuki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
        print(cuki)
    elif 'checkpoint' in cookies:
        print(f'Account On Checkpoint')
    else:
        print(f'Uid / Psw Wrong')

pass_to_cuki()
