"""""""""""""""""""""""""""
#Code by Firmg1           #
#Time：2019/6/1           #
"""""""""""""""""""""""""""



import requests
#设置头
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36 '
}
#设置目标url
url="http://lab1.xseclab.com/xss1_30ac8668cd453e7e387c76b132b140bb/search_key.php"
#获得响应
res = requests.get(url,headers=headers)
#打印出key
print(res.text)
