from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
import pandas as pd

product = ""

def reset_variables():
    global unit, price
    unit = 0
    price = 0

def request_url(product_name): 
    product_name = unidecode(product_name.lower().replace(" " , "-"))
    url = ("https://www.cimri.com/"+ product_name + "?sort=unit_price%2Casc")
    #print(url)
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content , features="lxml")
        return(soup)
    except:
        print("Can not get data! From : " + url)
        return(None)

def find_product(main_html, product_name):    
    product_html = main_html.find(attrs={"data-productorder" : "1"})
    return(product_html)

def find_price(product):
    
    top_offer = product.find(class_="top-offers")
    for i in top_offer.children:
        price = str(i.contents[1])
        price = price.replace(".", "")
        price = price.replace("," , ".")
        try:
            price = float(price.replace(" TL", ""))
            break
        except:
            pass
    return(price)

def find_unit(product, product_name):
    global unit, i 
    head = product.find("h3")
    head = head.contents[0]
    p_head = head
    head_split = head.split()
    i = 0
    for x in head_split:
        check = 0
        if x in ["ml", "cc"]:
            unit = int(head_split[i-1])
            check = 1
        if x.lower() in ["kg","l"]:
            unit = head_split[i-1]
            unit = int(unit+"000")
            check = 1
        i += 1
        if check == 1:
            break
    if unit == 0:
        #print("There was no given 'UNIT' value for " + head)
        unit = 1
    return(int(unit), p_head)

def get_data(product_name):
    reset_variables()
    html_main = request_url(product_name)
    if html_main == None:
        return(0, 0)
    product_html = find_product(html_main, product_name)
    price = find_price(product_html)
    unit, head = find_unit(product_html, product_name)
    print(f"For {product_name} Price : {price} - Unit : {unit}")
    return(pd.Series([head, price, unit]))
