from bs4 import BeautifulSoup
import requests
url = "http://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

print(" Назви всіх книг ")
books = soup.find_all("article", class_="product_pod")
for i, book in enumerate(books, 1):
  title = book.h3.a["title"]
  print(f"{i}. {title}")

print(" Ціна кожної книги ")
for i, book in enumerate(books, 1):
  price = book.find("p", class_="price_color").text
  print(f"{i}. {price}")

print(" Інформація про всі книги ")
for i, book in enumerate(books, 1):
  title = book.h3.a["title"]
  price = book.find("p", class_="price_color").text
  print(f"Книга {i}: «{title}» — Ціна: {price}")