#Code by Harry Crexx.

import requests, re
from time import sleep as wait

def cookie_convert(cookie):
    try:
        head={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie}
        tkkn=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', tkkn.text)
        token=reqq.group(1)
        print("\n✓ your token: %s\n\n"%(token))
    except AttributeError:
        print("! don't be empty");wait(3)
    except UnboundLocalError:
        print("! cookie invalid");wait(3)

cookie = input("Enter Your Cookie : ")
cookie_convert(cookie)
