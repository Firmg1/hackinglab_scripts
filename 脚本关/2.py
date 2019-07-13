import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
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
res = s.post(url, data=data)
soup = BeautifulSoup(res.content, 'lxml')
print(soup)
