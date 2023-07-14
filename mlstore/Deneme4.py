import subprocess

from bs4 import BeautifulSoup
import requests
def find_git_clone_code(url,link_text):
    # Web sayfasını indirin
    response = requests.get(url)

    # İçeriği analiz etmek için BeautifulSoup kullanın
    soup = BeautifulSoup(response.content, "html.parser")

    # Verilen anahtar kelimeye sahip olan linkleri seçin ve döndürün
    for link in soup.find_all("a"):
        link_split = link.text.split("/")
        if link_text in link.text and len(link_split) == 5 and link_split[0:3] == ['http:', '', 'lore.kernel.org'] and link_split[-2] == link_text and link_split[-1].isdigit():
            yield link.get("href")
def find_mirror(url):
    target_text = "mirror"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        link = soup.find("a", string=target_text)
        if link:
            link_url = link.get("href")
            return url+link_url
        else:
            print("Hedef metin için bağlantı bulunamadı.")
    else:
        print("Sayfa çekilemedi. Hata kodu:", response.status_code)

print(find_mirror("https://lore.kernel.org/oe-kbuild-all/"))