import requests
from bs4 import BeautifulSoup
import smtplib


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aviralaarav@gmail.com', 'aviralvns')

    subject = 'Price fell down!'
    body = 'Check amazon link: https://www.amazon.in/gp/product/B07HGJJ559/ref=s9_acss_bw_cg_Budget_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=8XHV91KMRJTF59PBRX6J&pf_rd_t=101&pf_rd_p=ddc11549-2c67-4b5e-ac5a-1ec8f1107dca&pf_rd_i=1389401031'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('aviralaarav@gmail.com', 'aviralsingh@protonmail.com', msg)
    print('Email has been sent')

    server.quit()


URL = 'https://www.amazon.in/gp/product/B07HGJJ559/ref=s9_acss_bw_cg_Budget_2\
    a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=8XHV91\
    KMRJTF59PBRX6J&pf_rd_t=101&pf_rd_p=ddc11549-2c67-4b5e-ac5a-1ec8f1107dca&p\
    f_rd_i=1389401031'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100\
           101 Firefox/79.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
deal_price = soup.find(id='priceblock_dealprice')
price = soup.find(id='priceblock_ourprice')
processed_price = ''

if deal_price:
    for character in deal_price.get_text():
        if character == ',' or character == ' ' or character == '₹':
            c = ''
            processed_price += c

        else:
            processed_price += character
    converted_price = float(processed_price)

elif price:
    for character in price.get_text():
        if character == ',' or character == ' ' or character == '₹':
            c = ''
            processed_price += c

        else:
            processed_price += character
    converted_price = float(processed_price)

if converted_price < 14499:
    send_mail()

print(title.strip())
