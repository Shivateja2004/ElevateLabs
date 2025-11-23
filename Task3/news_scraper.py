import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"  # You can choose any public news site

def fetch_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("Error fetching page:", e)
        return None

def scrape_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    titles = []

    # Scraping <a> tags inside title links (Hacker News)
    for tag in soup.find_all("a", class_="storylink"):
        titles.append(tag.text.strip())

    return titles

def save_to_file(headlines):
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")

def main():
    html = fetch_html(URL)
    if not html:
        return

    headlines = scrape_headlines(html)

    if headlines:
        save_to_file(headlines)
        print(f"Saved {len(headlines)} headlines to headlines.txt")
    else:
        print("No headlines found.")

main()
