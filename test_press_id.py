import urllib.request

from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
from pip._internal.utils.direct_url_helpers import direct_url_from_link

url_company = 'https://news.naver.com/main/officeList.naver'
html_company = urllib.request.urlopen(url_company).read()
soup_company = BeautifulSoup(html_company,'html.parser')
print(soup_company)

title_company = soup_company.find_all(class_='list_press nclicks(\'rig.renws2pname\')')
print(title_company)


for i in title_company :
    parts = urlparse(i.attrs['href'])

    PRESS_NAME = i.get_text().strip()
    PRESS_ID   = parse_qs(parts.query)['officeId'][0]

    print(PRESS_NAME + ' : ' + PRESS_ID)
