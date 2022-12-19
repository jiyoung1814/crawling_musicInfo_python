from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

import time



def crawling(browser,name):
    # browser = webdriver.Chrome(ChromeDriverManager().install()) # 현재파일과 동일한 경로일 경우 생략 가능


    ##-------------------네이버 검색-----------------------
    # browser.get('https://naver.com')  # 네이버 사이트로 이동한다.
    # time.sleep(0.5)
    #
    # elem = browser.find_element(By.ID, "query") # 검색어 입력창을 가져온다.
    # elem.send_keys(name)# 검색어 입력창에 'name'라고 입력한다.
    #
    # elem = browser.find_element(By.CLASS_NAME, "btn_submit")  # 검색 버튼을 가져온다.
    # elem.click()  # 검색 버튼을 클릭한다.
    ##-------------------네이버 검색-----------------------


    browser.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+name)
    # time.sleep(1.5)

    # try:
    #     elem = browser.find_element(By.LINK_TEXT, "곡정보")
    #     elem.click()
    #     # time.sleep(0.5)
    #
    #     # 0. 아티스트, 1. 앨범, 2. 발매  3. 장르 4. 작곡 5. 작사 6. 편곡
    #     # for title in elem:
    #     #     # if title.text == "곡정보":
    #     #     print(title.text)
    #     artist.append(elem[0].text.split("\n")[1])
    #     artist.append(elem[2].text.split("\n")[1])
    #     genre.append(elem[3].text.split("\n")[1])
    # except:
    #     print("NO 곡정보")

    elem = browser.find_element(By.CLASS_NAME, "_text")
    song_title = elem.text
    # print(song_title == "Attention")

    if song_title != 'Attention':
        if song_title != "Yet To Come":

            try:
                elem = browser.find_element(By.CLASS_NAME, "link_box")
                elem.click()

                elem = browser.find_element(By.LINK_TEXT, "곡정보")
                elem.click()
                # time.sleep(0.5)

                # 0. 아티스트, 1. 앨범, 2. 발매  3. 장르 4. 작곡 5. 작사 6. 편곡
                for t in elem:
                    if t.text.split("\n")[0] == "아티스트":
                        artist.append(t.text.split("\n")[1])
                    else:
                        artist.append("");

                    if t.text.split("\n")[0] == "발매":
                        date.append(t.text.split("\n")[1])
                    else:
                        date.append("");

                    if t.text.split("\n")[0] == "장르":
                        genre.append(t.text.split("\n")[1])
                    else:
                        genre.append("");
                    title.append(song_title)
                # time.sleep(0.5)
            except:
                print("NO link_box")



    elem = browser.find_element(By.LINK_TEXT, "곡정보")
    elem.click()
    # time.sleep(1.5)

    elem = browser.find_elements(By.CLASS_NAME, "info_group")

    str =""
    str_a ="";
    str_d = "";
    str_g = "";

    #0. 아티스트, 1. 앨범, 2. 발매  3. 장르 4. 작곡 5. 작사 6. 편곡
    # title.append(song_title)
    str += song_title;
    for t in elem:
        # if t.text.split("\n")[0] == "아티스트":
        #     artist.append(t.text.split("\n")[1])
        # else:
        #     artist.append("");
        #
        # if t.text.split("\n")[0] == "발매":
        #     date.append(t.text.split("\n")[1])
        # else:
        #     date.append("");
        #
        # if t.text.split("\n")[0] == "장르":
        #     genre.append(t.text.split("\n")[1])
        # else:
        #     genre.append("");
        # title.append(song_title)

        if t.text.split("\n")[0] == "아티스트":
            str_a +=(t.text.split("\n")[1])
        else:
            str_a +=("");

        if t.text.split("\n")[0] == "발매":
            str_d +=(t.text.split("\n")[1])
        else:
            str_d +=("");

        if t.text.split("\n")[0] == "장르":
            str_g +=(t.text.split("\n")[1])
        else:
            str_g +=("");

    str += "|"+str_a+"|"+str_d+"|"+str_g
    info.append(str);
    print(str)







def print_title(address, query):

    for i in range(2,10):
        startvalue = 15* i -29
        addr= address + str(i) +'&query='+query+'&research_url=&sm=tab_pge&start='+str(startvalue)+'&where=web'

        res = requests.get(addr)
        soup = BeautifulSoup(res.content, 'html.parser')


        items = soup.select('.link_tit')
        for item in items:

            print(item.text)

if __name__ == '__main__':
    s_title = ['After LIKE', '새삥 (Prod. ZICO) (Feat. 호미들)', 'Shut Down', 'Pink Venom', 'Attention', 'Hype Boy', 'LOVE DIVE', 'FOREVER 1', '그때 그 순간 그대로 (그그그)', 'Cookie', '사랑은 늘 도망가', '우리들의 블루스', '보고싶었어', 'LAW (Prod. Czaer)', '그라데이션', '다시 만날 수 있을까', 'SNEAKERS', 'TOMBOY', '사랑인가 봐', '무지개', '정이라고 하자 (Feat. 10CM)', '이제 나만 믿어요', '나의 X에게', '아버지', '내가 아니라도', 'POP!', 'A bientot', 'That That', '도깨비불 (Illusion)', '손이 참 곱던 그대', '사랑해 진짜', '인생찬가', 'ELEVEN', '사랑역', 'Talk that Talk', '보금자리', 'FEARLESS', '사랑해요 그대를', '질주 (2 Baddies)', 'Love story', 'That\'s Hilarious', 'Monologue', '취중고백', 'LOVE me', '사랑한다고 말해줘', '너의 모든 순간', '통화연결음', 'Girls', '다정히 내 이름을 부르면', '봄여름가을겨울 (Still Life)', 'Ready For Love', 'strawberry moon', 'Yeah Yeah Yeah', 'Stay', '모든 날, 모든 순간 (Every day, Every Moment)', 'Dynamite', '스티커 사진', 'Left and Right (Feat. Jung Kook of BTS)', 'Feel My Rhythm', 'I Don\'t Think That I Like Her', 'I Ain\'t Worried', 'INVU', '열이올라요 (Heart Burn)', '드라마', 'Butter', '윤슬 (Gold Dust)', '밤하늘의 별을(2020)', '아무래도 난', '잠수이별 (Prod. 코드 쿤스트)', 'GANADARA (Feat. 아이유)', 'Yet To Come', 'MY BAG', '늦은 밤 헤어지긴 너무 아쉬워', 'Next Level', 'Off My Face ', '듣고 싶을까', 'Permission to Dance', 'SMILEY', 'Weekend 태연', '너를 생각해', '고백하는 취한밤에 (Prod. 2soo)', '언제나 사랑해 ', 'I LOVE U', '팡파레', 'Braindead', 'Celebrity', '어떻게 이별까지 사랑하겠어, 널 사랑하는 거지', '인생은 뷰티풀', '바라만 본다', '미친 것처럼', '라일락 아이유', 'BEAUTIFUL MONSTER', 'My Universe 방탄소년단', 'Clink Clink (클링 클링)', 'HOT']
    baseaddress = 'https://search.naver.com/search.naver?display=15&f=&filetype=0&page='
    query = '테스트'

    # for i in range(1, 35):
    # print_title(baseaddress, query)



    browser = webdriver.Chrome(ChromeDriverManager().install())

    global title
    global artist
    global genre
    global date
    global info

    title = []
    artist = []
    genre = []
    date = []
    info = []


    # crawling(browser, 'Clink Clink')
    # crawling(browser, 'HOT')

    for name in s_title:
        crawling(browser, name)

    # print(title)
    # print(artist)
    # print(genre)
    # print(date)
    print(info)
    for name in info:
        print(name+"\n")



