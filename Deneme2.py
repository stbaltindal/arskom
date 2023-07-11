from bs4 import BeautifulSoup
import requests

# Web sayfasını indirin
url = "https://lore.kernel.org"
response = requests.get(url)

# İçeriği analiz etmek için BeautifulSoup kullanın
soup = BeautifulSoup(response.content, "html.parser")

# <a> etiketlerini bulun ve bağlantıları ve metin içeriklerini sözlükte eşleştirin
links = soup.find_all("a")
link_dict = {}
while True:
    for link in links:
        link_text = link.text.strip()
        link_href = link.get("href")
        link_dict[link_text] = link_href
    if 'next (older)' in link_dict:
        response = requests.get(url+f"{link_dict['next (older)']}")
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    if not 'next (older)' in link_dict:
        break
    del link_dict['next (older)']
for i in link_dict.keys():
    print(i)
# Kullanıcıdan istenilen konu arşivine erişme

while True:
    print()
    istenilen_konu = input("Sahip olmak istediğiniz arşivi seçiniz:")
    if istenilen_konu in link_dict:
        print(f"***{istenilen_konu}*** arşivi size gönderiliyor...")
        break
    else:
        print("Olmayan bir konu seçtiniz tekrar deneyiniz.")








"""
# Sözlüğü yazdırın
for text, href in link_dict.items():
    print("Metin: {}, Link: {}".format(text, href))
print(link_dict)
"""