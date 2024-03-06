# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
import requests
import pandas as pd
import re
import openpyxl
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
< naver 뉴스 검색시 리스트 크롤링하는 프로그램 > _select사용
- 크롤링 해오는 것 : 링크,제목,신문사,날짜,내용요약본
- 날짜,내용요약본  -> 정제 작업 필요
- 리스트 -> 딕셔너리 -> df -> 엑셀로 저장 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''



#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/Python/workspaces/ors_news/crawling_result/'  #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기

today_str = datetime.today().strftime("%Y%m%d")
today_num = int(today_str)

#날짜 정제화 함수
def date_cleansing(test):
    try:
        #지난 뉴스
        #머니투데이  10면1단  2018.11.05.  네이버뉴스   보내기
        pattern = '\d+.(\d+).(\d+).'  #정규표현식

        r = re.compile(pattern)
        match = r.search(test).group(0)  # 2018.11.05.
        return match

    except AttributeError:
        #최근 뉴스
        #이데일리  1시간 전  네이버뉴스   보내기
        pattern = '\w* (\d\w*)'     #정규표현식

        r = re.compile(pattern)
        match = r.search(test).group(1)
        #print(match)
        return match


#내용 정제화 함수
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
                                      str(contents)).strip()  #앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
                                       first_cleansing_contents).strip()#뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    return third_cleansing_contents



def crawler(maxpage,query,sort,s_date,e_date):

    s_from = re.sub(r'[^0-9]', '', s_date)
    e_to   = re.sub(r'[^0-9]', '', e_date)

    page = 1
    maxpage_t =(int(maxpage)-1)*10+1   # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지

    while page <= maxpage_t:
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)

        response = requests.get(url)
        html = response.text

        #뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        # 각 크롤링 결과 저장하기 위한 리스트 선언
        News_dates = []
        Press_name = []
        Title      = []
        Link       = []
        Contents   = []
        result     = {}

        for news_result in soup.select(".list_news > li"):

            news_dates = news_result.select('span.info')
            press_name = news_result.select_one(".info.press").text
            title      = news_result.select_one(".news_tit").text
            link       = news_result.select_one(".news_tit")["href"]
            contents   = news_result.select_one(".news_dsc").text

            # (A면1단, 날짜) 형태로 되어 있는 경우 처리
            if len(news_dates) > 1:
                news_date = news_dates[1].get_text().replace('.', '')
            else:
                news_date = news_dates[0].get_text().replace('.', '')

            if "분" in news_date or "시간 전" in news_date:
                news_date = str(today_num)
                news_date = datetime.strptime(news_date, '%Y%m%d').strftime('%Y-%m-%d')

            elif "일 전" in news_date:
                news_date_num = int(re.sub('[\D]', '', news_date))
                news_date = str(datetime.today() - timedelta(days=news_date_num))
                news_date = news_date[:10]
            # news_date = datetime.strptime(news_date, '%Y%m%d').strftime('%Y-%m-%d')

            else:
                news_date = str(news_date)
                news_date = datetime.strptime(news_date, '%Y%m%d').strftime('%Y-%m-%d')

            News_dates.append(news_date)
            Press_name.append(press_name)
            Title.append(title)
            Link.append(link)
            Contents.append(contents_cleansing(contents))

            #모든 리스트 딕셔너리형태로 저장
            result= {
                     "기사일자"  : News_dates ,
                     "언론사"    : Press_name ,
                     "기사제목"  : Title ,
                     "기사링크"  : Link ,
                     "본문요약"  : Contents
                     }


        print(page)
        df = pd.DataFrame(result)  #df로 변환
        page += 10

    # 새로 만들 파일이름 지정
    outputFileName = 'RESULT_%04d%02d%02d_%02d%02d%02d_%s.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second,query)
    df.to_excel(
                 RESULT_PATH + outputFileName
               , sheet_name=query
               , index=False
               )




def main():
    #info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)

    maxpage = "5"  #input("최대 크롤링할 페이지 수 입력하시오: ")
    query = "BNK" #input("검색어 입력: ")
    sort = "1"   # input("뉴스 검색 방식 입력(관련도순=0  최신순=1  오래된순=2): ")    #관련도순=0  최신순=1  오래된순=2
    s_date = "2024/03/01" # input("시작날짜 입력(2019.01.04):")  #2019.01.04
    e_date = "2024/03/07" # input("끝날짜 입력(2019.01.05):")   #2019.01.05

    crawler(maxpage,query,sort,s_date,e_date)

main()













