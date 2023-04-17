# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import random

client_id = "yBeCYOpJm4z0LP2glWvo"
client_secret = "1GxLsJ05tP"

print('블로그 검색기 입니다.')
keyword = input('검색어를 입력하세요 :')

encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    data = json.loads(response_body.decode('utf-8'))
    print(type(data))
    print(type(data['items'])) # 얘는 리스트

    # 리스트를 풀어서 각각 딕셔너리에 있는 데이터 중에 내가 원하는 값들만 출력
    for item in data['items']: # 리스트 중에서 딕셔너리 하나를 가지고 와서
        print('블로그 제목 :', item['title']) # 딕셔너리 중에서 타이틀로 되어있는 데이터를 출력
        print('블로그 링크 :', item['link']) #이건 링크 

    input('이중에 하나를 추천 받고 싶으면 아무 키나 입력하세요.')
    recom = random.choice(data['items'])
    print(recom['title'])
    print(recom['link'])


else:
    print("Error Code:" + rescode)