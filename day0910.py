
import re
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

search_term = "python"

#f덕분에 문자열 안에 변수를 넣을수있는것!
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")

    #len - 리스트나 튜플의 길이를 줄여줌  -> 개수로 
    #섹션 안에 들어간 li들을 각각 그룹화로 나눠줄거임 
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1] #두번째 링크를 얻기 위해 [1] 작성 
        #print(anchor['href']) #우리가 필요한 정보가 담긴 링크 
        #파이썬에서는 따로 변수 뒤에 [] 안 붙여도 리스트인거 담을때 잘 알아 듣는다. 
        link = anchor['href']
        # 링크 받았으니 이제 회사이름, 구인 제목, 원격, 시간제, 위치 받기 
        # 사이트 기준 company 동일 이름 변수 순서대로 회사이름/시간제/지역 으로 분류된다 
        company, kind, region = anchor.find_all('span', class_="company")
        #print(company, kind, region)
        title = anchor.find('span', class_="title") 
        #find_all은 리스트 형식으로 반환하기 때문에 하나의 항목만 필요한 시점에선 find를 사용한다. 
        print(title,company,kind,region)
        print("////////////")
        print("////////////")