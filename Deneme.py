import requests
from bs4 import BeautifulSoup

url = "https://em.gsu.edu.tr"
keyword = "Chief"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


print(soup.title.string)
print(soup.p)
print(soup.find_all('a'))
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.find_all(string=lambda text: text and keyword in text)

    if rows:
        for row in rows:
            # Satırı kopyalayın veya işleyin
            print(row)
    else:
        print("Anahtar kelime bulunamadı.")
else:
    print("Sayfa çekilemedi. Hata kodu:", response.status_code)
