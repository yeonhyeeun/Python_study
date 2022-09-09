#request와 beautifulsoup4 터미널을 통해 설치하기 
import os

#get은 웹사이트를 받아오는 형식이다
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

search_term = "python"

#f덕분에 문자열 안에 변수를 넣을수있는것!
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    #.text는 해당 웹사이트를 구성하고있는 html을 받아온다
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")