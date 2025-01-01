from urllib.request import urlopen
import requests
import webbrowser
from bs4 import BeautifulSoup
import os
import requests

choose = int(input("1: เข้าโปรแกรม\n2: ออกโปรแกรม\n "))


def chooseInput():
    if choose == 1:
        saveContent()
    elif choose == 2:
        exit
        print('ออกจากโปรแกรม')


def saveContent():
    inputUrl = input('Job: ')

    if inputUrl == "":
        exit
        print('ออกจากโปรแกรม')
    else:
        URL = 'https://happyfranchise.co.th/store/product/view/'
        URL1 = URL + inputUrl

        path = inputUrl

        getURL = requests.get(URL1, headers={"User-Agent": "Mozilla/5.0"})

        soup = BeautifulSoup(getURL.text, 'html.parser')

        images = soup.find_all('img')
        resolvedUrls = []

        textTags = soup.find_all('p')

        for textTag in soup.select('p'):
            txt = textTag.get_text(strip=True, separator='\n')
            # print(txt)

            # Download from URL and decode as UTF-8 text.
            # with urlopen(URL) as webpage:
            #     content = webpage.read().decode()

            if not os.path.exists(path):
                urlContent = os.mkdir(path)
            urlCon = "{urlP}".format(urlP=path)

            # Save to file.
            # with open('./{{urlContent}}/{{URL1}}.txt', 'a') as output:
            with open('./' + path + '/' + urlCon + '.txt', 'a') as output:
                output.write(txt)

        for image in images:
            src = image.get('src')
            resolvedUrls.append(requests.compat.urljoin(URL, src))
            # print(src)

        for image in resolvedUrls:
            webs = requests.get(image)
            # open('images/' + image.split('/')[-1], 'wb').write(webs.content)
            open(urlCon + '/' + image.split('/')[-1], 'wb').write(webs.content)

        print('Save Content in website Success!!')

        chooseInput()


chooseInput()
