import requests
import smtplib
from bs4 import BeautifulSoup
import wishList as data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def check_price(item: object):
    page = requests.get(item['url'], headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    item_title = soup.find(id='title').get_text()
    item_price = soup.find(id='priceblock_ourprice').get_text()
    item_details = f'Title: {item_title.strip()}  Price: {item_price}'

    if float(item_price[1:].replace(',', '')) >= item['target_price']:
        send_email(item_details)


def send_email(print_details: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('zarcher90@gmail.com', 'lyizpmsmznxzrqis')
    
    subject = 'Price Drop!!!'
    body = print_details

    msg = f'Subject: {subject}\n\n {body}'

    server.sendmail('PRICE CHECKER', 'zarcher90@gmail.com', msg)
    print('email sent')
    server.quit()


for wish_item in data.WISHLIST:
    check_price(wish_item)