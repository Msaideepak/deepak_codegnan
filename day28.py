import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re
#step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()
except requests.exceptions.RequestException as e:
      print("❌ Error fetching data:", e)
      exit()
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
names =[]
prices=[]

for book in books:
    name=book.h3.a["title"]

    price_text=book.find("p",class_="price_color").text
    price=float(re.findall(r'\d+\.+',price_text)[0])

    names.append(name)
    prices.append(price)

df=pd.DataFrame({
    "book name": names,
    "price":prices
})

print("\n📊 table data:\n")
print(df.head())

df.to_csv("books_data.cvs", index=false)
print("\n✅ csv file 'books_data.csv' created successfully!")


plt.figure()
pli.bar(names[:10], prices[:10])
plt.xticks(rotation=90)
plt.xlabel("books names")
plt.ylabel("price")
plt.title("books prices (top 10)")
plt.tight_layout()
plt.show()
