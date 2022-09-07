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

