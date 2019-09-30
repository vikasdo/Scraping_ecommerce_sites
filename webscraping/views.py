
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request as requested

import requests



from difflib import get_close_matches
import webbrowser



from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
class product:
    def __init__(self, name=None, price=None,image=None,cat=None):
        self.name = name
        self.price = price
        self.image=image
        self.cat=cat

def index(request):
    prod=product()
    prod.name='sony tv'
    prod.img='news_1.jpg'
    prod.price=39200
    prod1 = product()
    prod1.name = 'sony tv'
    prod1.img = 'news_2.jpg'
    prod1.price = 39200
    prod2 = product()
    prod2.name = 'sony tv'
    prod2.img = 'news_3.jpg'
    prod2.price = 39200
    prod3 = product()
    prod3.name = 'sony tv'
    prod3.img = 'news1.jpg'
    prod3.price = 39200
    prods=[prod1,prod2,prod3]
    return render(request, 'index.html',{'prods':prods})
def search(request):
    key=request.GET['key']

#snapdeal **)))))))_++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url_flip = 'https://www.snapdeal.com/search?clickSrc=top_searches&keyword=' +str(key)+''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    keys = []
    source_code = requests.get(url_flip, headers=headers)
    plain_text = source_code.text
    soup_flip = BeautifulSoup(plain_text, "html.parser")
    snapdeal=[]
    count = 0
    try:
        for title in soup_flip.find_all("p", {"class": "product-title"}):
            count += 1

            keys.append(title.text)

            if count == 2:
                break
    except:
        print()
    values=[]
    try:
        k = 0
        for div in soup_flip.find_all('div', {'class': 'product-price-row clearfix'}):
            for each in div.find_all('span', {'class': 'lfloat product-price'}):
                if k < 2:
                    values.append(each.text.replace("shipping", " "))
                    k += 1
    except:
        print()
    response = requested.urlopen(url_flip)
    soup = BeautifulSoup(response, 'html.parser')
    s = soup.find_all('picture', {'class': 'picture-elem'})
    c=0
    imag=[]
    for s1 in s:
        try:
            if c<2:
             imag.append(s1.img['data-src'])
             c+=1
        except:
            print("not found", s1.img['src'])
    for i in range(len(keys)):
        snapdeal.append(product(keys[i],values[i],imag[i],'Snapdeal'))

    #    flipkart ********************************************************************************
    url = 'https://www.flipkart.com/search?q=' + str(key) + ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    flipkart=[]
    titlear=[]
    prices = []
    c=0
    for title in soup.find_all('div', {'class': '_3wU53n'}):
        if c<2:
         titlear.append(title.text)
         c+=1
    try:

        product_source_code = requests.get(url, headers=headers)
        product_plain_text = product_source_code.text
        product_soup = BeautifulSoup(product_plain_text, "html.parser")
        c = 0

        for price in product_soup.find_all('div', {'class': '_1vC4OE'}):
            if c<2:
             prices.append(price.text)
             c+=1
    except:
        print("erre")
    for i in range(len(titlear)):
        flipkart.append(product(titlear[i],prices[i],cat='Flipkart'))



    #ebay**************************************************************************************************************************


    url_flip = 'https://www.ebay.com/sch/i.html?_nkw=' + str(key) + ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    title_arr = []
    source_code = requests.get(url_flip, headers=headers)
    plain_text = source_code.text
    soup_flip = BeautifulSoup(plain_text, "html.parser")
    count = 0
    tty=[]
    try:

        for title in soup_flip.find_all("h3", {"class": "s-item__title"}):

            count += 1

            tty.append(title.text)
            if count == 2:
                break
    except:
        print()
    pr=[]
    pr2=[]
    try:
        k = 0
        for div in soup_flip.find_all('div', {'class': 's-item__wrapper clearfix'}):
            for each in div.find_all('div', {'class': 's-item__detail s-item__detail--primary'}):
                if k < 2 and each.text not in('or Best Offer','Watch','Buy It Now'):
                    pr.append(each.text)
            k += 1


    except:
        print()
    url = 'https://www.ebay.com/sch/i.html?_nkw='+str(key)+''
    response = requested.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    img=[]
    s = soup.find_all('div', {'class': 's-item__image-wrapper'})
    for s1 in s:
        try:
            img.append(s1.img['src'])
        except:
            print("not found")

    ebay=[]
    for i in range(len(tty)):
     ebay.append(product(tty[i], pr[i],img[i], cat='Ebay'))

#amazon;**************************************************************************************************************************

    url_flip = 'https://www.amazon.in/s?k=' + str(key) + ''
    print(url_flip)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    source_code = requests.get(url_flip, headers=headers)
    plain_text = source_code.text
    soup_flip = BeautifulSoup(plain_text, "html.parser")
    titles=[]
    k=0
    for title in soup_flip.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"}):
        if k<2:
         titles.append(title.text)
         k+=1
         print(title.text)
    pricea=[]
    c=0
    for div in soup_flip.find_all('div', {'class': 'a-row'}):
        for each in div.find_all('span', {'class': 'a-offscreen'}):
            if c<2:
             c+=1
             pricea.append(each.text)
    amazon = []
    for i in range(len(titles)):
        amazon.append(product(titles[i], pricea[i], img[i], cat='Amazon'))

    return render(request, "home.html", {'snapdeal': snapdeal,'flipkart':flipkart,'ebay':ebay,'amazon':amazon})
