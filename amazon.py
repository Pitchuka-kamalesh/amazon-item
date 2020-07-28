import time 
import smtplib
import requests 
from bs4 import BeautifulSoup as bs
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
link = 'https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK' 
# item you want to moniter for rate
def mailg(rate):
    gmail_user = ''  #gmail id 
    gmail_password = '' #gmail password

    sent_from = gmail_user
    to = [""] #sender mail
    subject ='Amazon Fire Stick Price'
    body = '\n\nAmazon fire stick rate is %s \n\n %s' %(rate,link)
    message = 'Subject: {}\n\n{}'.format(subject,body)

   

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(gmail_user,gmail_password)
        s.sendmail(sent_from,to,message)
        s.quit()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


def amaz ():
    page = requests.get(link,headers = headers)

    soup = bs(page.text,'html.parser')

    price = (soup.find(class_ = 'a-size-medium a-color-price priceBlockBuyingPriceString').text)

    rate = float((price.replace("₹\xa0","")).replace(',',''))

    if rate <= 3200:
        mailg(rate)
    
    else:
        print(rate)
        time.sleep(43200)
        amaz()

amaz() 



