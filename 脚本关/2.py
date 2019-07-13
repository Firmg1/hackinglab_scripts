import requests
import re
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
s=requests.session()
request = s.get(url)
ret = re.findall('\d+', request.text)
r1 = int(ret[2])
r2 = int(ret[3])
r3 = int(ret[4])
ree = r1 * r2 + r3 * (r1 + r2)
data = {
    'v': str(ree)
}
res = s.post(url, data=data).content
print(res.decode('utf-8'))
