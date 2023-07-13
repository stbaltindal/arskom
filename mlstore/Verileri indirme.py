import requests
from bs4 import BeautifulSoup

url = "https://lore.kernel.org/linux-renesas-soc/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", text="mirror")

    if links:
        mirror_link = links[0]["href"]
        print("Mirror bağlantısı:", mirror_link)
    else:
        print("Mirror bağlantısı bulunamadı.")
else:
    print("Sayfa çekilemedi. Hata kodu:", response.status_code)