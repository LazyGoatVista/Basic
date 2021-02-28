import urllib.request
import ssl
import re


def generate_vmess():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://my.ishadowx.biz'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    pattern = re.compile(r'vmess:.*?\n')
    res = pattern.findall(html)
    #return res[2]
    return ''.join(res)


if __name__ == '__main__':
    output = generate_vmess()
    print(output)
