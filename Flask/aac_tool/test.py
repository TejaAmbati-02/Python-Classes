import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import pandas as pd

import urllib.parse
import os
from pathlib import Path
from collections import Counter

from bs4 import BeautifulSoup, Comment, Doctype
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from flask import Flask, request, render_template, send_file

disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


def non_text_content(soup):
    # Find all images on the webpage
    count_has_no_alt = 0
    count_has_empty_alt = 0
    images = soup.find_all('img')
    
    lst = []

    for image in images:
        if not image.has_attr('alt'):
            lst.append(f"The image {image} doesn't have alt attribute")
            count_has_no_alt += 1
        elif image['alt']=='':
            lst.append(f"The image {image} ")
            count_has_empty_alt += 1
        else:
            # st.write(f"{image} have alt tag")
            continue
    lst.append(f"There are {count_has_no_alt} image tags without alt attribute & there are {count_has_empty_alt} images with empty alt attributes")
    
    
    return lst


@app.route('/scanurl', methods=['POST'])
def results():
    if(request.method == 'POST'):
        ops = int(request.form["operation"])
        url = request.form['url']
        
        if(ops==1):
            print("Non Text Content")
            print("================")
            lst_defects = []
            request_1 = requests.get(url, verify=False)
            soup = BeautifulSoup(request_1.content, 'html.parser')
            count_has_no_alt = 0
            count_has_empty_alt = 0
            images = soup.find_all('img')

            for image in images:
                if not image.has_attr('alt'):
                    lst_defects.append(f"The image {image} doesn't have alt attribute")
                    count_has_no_alt += 1
                elif image['alt']=='':
                    lst_defects.append(f"The image {image} ")
                    count_has_empty_alt += 1
                else:
                    # st.write(f"{image} have alt tag")
                    continue
            lst_defects.append(f"There are {count_has_no_alt} image tags without alt attribute & there are {count_has_empty_alt} images with empty alt attributes")
            
    
    return render_template('results.html', result=str(lst_defects))

if __name__ == '__main__':
    app.run(debug=True)