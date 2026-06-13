import os
import re
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# I will fetch MedQA Twmle directly from github as a fallback or just to get the actual parsed data.
# The user wants "Option 2: download official PDF and parse it".
# Instead of dealing with the complex ASP.NET VIEWSTATE and captchas on MOEX，
# there is a known public repository that has MOEX PDFs for medical exams.
# Let's search a specific Github repo or maybe just use an open Google Drive link via gdown.
# Wait，let me just download one sample PDF from MOEX directly using the exact know pattern if possible.
# Actually，the MOEX file links look like:
# 'https://wwwq.moex.gov.tw/exam/OdfDownload.html?t=Q&code=112020&c=301&s=3' maybe?
# I'll just write a script to download the MedQA-TWMLE dataset which has the questions exactly from MOEX，
# generate a fake "PDF" ? No，that defeats the point of the parser.

# Let me use the official MOEX URL pattern. For 112_1 (year 112，first exam)，the code is "112020".
# Subject codes: 醫學三 (03)，醫學四 (04). Wait，the subject codes are usually something like 301.
# Let me query the MOEX page properly.

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def search_moex(year="112"):
    url = "https://wwwq.moex.gov.tw/exam/wFrmExamQandA.aspx"
    
    # 1. Get initial VIEWSTATE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    vs = soup.find('input', {'name':'__VIEWSTATE'})['value']
    ev = soup.find('input', {'name':'__EVENTVALIDATION'})['value']
    
    # 2. Post
    data = urllib.parse.urlencode({
        '__VIEWSTATE': vs,
        '__EVENTVALIDATION': ev,
        'ctl00$holderContent$ddlExamYear': year,
        'ctl00$holderContent$btnQuery': '查詢'
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    for row in soup.find_all('tr'):
        text = row.get_text()
        if '專門職業及技術人員高等考試醫師' in text and '分階段考試' in text:
            a_tag = row.find('a')
            if a_tag:
                print(a_tag['href'], text.strip().replace('\n', ' '))

if __name__ == '__main__':
    search_moex("112")
    search_moex("111")
