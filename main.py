import requests
from bs4 import BeautifulSoup

URL = "https://www.lenovo.com/ca/en/laptops/thinkbook-series/ThinkBook-16p-G2-ACH/p/XXTBXPEA600"
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("li", {"class": "tabbedBrowse-productListing-container only-allow-small-pricingSummary"})

for result in results:
    if result.attrs['data-code'] == '20YM001DUS' or result.attrs['data-code'] == '20YM001EUS':
        status = result.find("div", {"class": "merch-tagLabel-ribbon modelCust__ribbon taglabel-font-sm"}).get_text()
        if status != "Temporarily Unavailable":
            print("Here!")
        else:
            print("Not here")