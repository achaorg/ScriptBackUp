#Copy from hostloc Jialian4213
import requests,time

h={
        'Host':'pt.btschool.net',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept-Language': 'zh-CN',
        'Referer':'https://pt.btschool.net/details.php?id=3703&hit=1',
} #header

c={
        'c_secure_login':'bmdfgdfgwZQ=555=',
        'c_secure_pass':'338ae1555a1ed6dfgdfgdb1b3ae78808bcec44305',
        'c_secure_ssl':'eWVhadfgdfgA55==',
        'c_secure_tracker_ssl':'bm9dfgdfgw2525252ZQ==',
        'c_secure_uid':'MjEyMdfgdfgzA='
} #cookie 改成自己的cookie

url="https://pt.btschool.net/thanks.php" #改成相应网站地址

s=requests.Session()

s.headers.update(h)
s.cookies.update(c)

for d in range(1, 5000) :
        req=s.post(url,data={'id':d})
        print('种子编号：',d,'状态码:',req.status_code)
        time.sleep(0.01) #加个延迟 避免影响服务器稳定....  怕ban号的 这里改成60
