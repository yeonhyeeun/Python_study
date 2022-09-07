#for loops practice

websites = (
    "goggle.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

for website in websites:
    # if website.startswith("https://"):
    #   print("good to go")
    # else:
    #   print("we have to fix it")
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)

    #startswith는 True / False 를 반환하는 메소드
    #f포맷을 사용하여 변수 재설정 (튜플이니까 수정불가능하다는 생각에서 벗어나기)

#request practice
#import requests 

from requests import get
#import requests
#standard lib에 없음. 인터넷을 통해 다운 받음

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    #get함수는 웹사이트의 응답 그대로를 받아온다.
    #print(response.status_code)
    #http 상세코드 검색해보면 프로토콜마다의 의미를 알수있음
    if response.status_code == 200:
        results[website] = "ok"
    else:
        results[website] = "failed"

print(results)

