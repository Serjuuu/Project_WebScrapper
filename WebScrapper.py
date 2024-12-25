import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://sandbox.oxylabs.io/products')
results = []
prices = []
categories = []
content = driver.page_source
soup = BeautifulSoup(content ,'html.parser')
for element in soup.findAll(attrs={'class': 'product-card'}):
    name = element.find('p')    
    price = element.find('div', class_='price-wrapper')
    title = element.find('h4')
    if title:
        product_title = title.text.strip()
        if name:
            product_name = name.text.strip()      
            if price:
                product_price = price.text.strip()
            else:
                product_price = "Price Not Available"      
    results.append((product_title, product_name, product_price))

df = pd.DataFrame(results, columns=['Product', 'Category', 'Price'])
df.to_csv('HackedData.csv', index=False, encoding='utf-8')

for title, name, price in results:
    print("Product: " + title + ", Category: " + name + ", Price: " + price)