import requests
from bs4 import BeautifulSoup

URL = "https://timesofindia.indiatimes.com"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h2')
    
    titles = []
    for h in headlines:
        text = h.get_text(strip=True)
        if text and text not in titles: 
            titles.append(text)

    with open("headlines.txt", "w", encoding="utf-8") as f:
        for title in titles:
            f.write(title + "\n")

    print(f"✅ {len(titles)} headlines saved to 'headlines.txt'")

else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")
