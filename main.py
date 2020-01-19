from bs4 import BeautifulSoup
import requests
import time 

url = "https://www.paycalculator.com.au/#5800|1|2020|9.5|5,250,8,40,50|100000"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
delay = 3


base = requests.get(url, headers=headers)
soup = BeautifulSoup(base.text,"lxml")

mydivs = soup.find_all('tr',{'class':'foot'})

print(mydivs)