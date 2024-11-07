from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
#-------------------------------------------------------------------------------------
browser = webdriver.Firefox()
browser.get('https://finviz.com/forex_performance.ashx')
currency_pairs = []

def get_currency_pairs():
    k = 1
    try:
        while True:
            findelement = browser.find_element(By.XPATH, f'//*[@id="futures"]/div/div[2]/div/div/div/div[{k}]')
            k+=1
    except NoSuchElementException:
        if k==1 :
            print("Element 2 not found")
        else:    
            print(k)
    try:
        for i in range (k-8,k):
            currency_name = str(browser.find_element(By.XPATH, f'//*[@id="futures"]/div/div[2]/div/div/div/div[{i}]/div[2]').text)
            currency_value = str(browser.find_element(By.XPATH, f'//*[@id="futures"]/div/div[2]/div/div/div/div[{i}]/div[1]').text)
            currency_pair = [currency_name, currency_value]
            currency_pairs.append(currency_pair)
        return (1)
    except NoSuchElementException:
        print("Element 3 not found")
while True:
    try:
        element = browser.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')
        element.click()
        if get_currency_pairs() == 1:
            break
        else:
            time.sleep(5)
    except NoSuchElementException:
        print("Element 1 not found")
        if get_currency_pairs() == 1:
            break
        else:
            time.sleep(5)
browser.quit()
print("*"*20)
res = ""
res+= "The strength of currencies based on current sentiment, in order from strong to weak:" +"\n\n"
sorted_list = sorted(currency_pairs, key=lambda x: float(x[1].strip('%')), reverse=True)
result = [item[0] for item in sorted_list]
for i in result:
    res+= str(i)+'\n'   
risk_on_currencies  = ['AUD','NZD','CAD','GBP']
risk_off_currencies = ['USD','CHF','JPY']
if result[0] in risk_on_currencies:
    if result[1] in risk_on_currencies:
        res+= '\n'+'The market is in risk on conditions'
    else:
        res+= '\n'+'The sentiment of the market is Mix to risk on'
elif result[0] in risk_off_currencies:
    if result[1] in risk_off_currencies:
        res+= '\n'+'The market is in risk off conditions'
    else:
        res+= '\n'+'The sentiment of market is Mix to risk off'
else:
    res+= '\n'+'The sentiment of the market is completely mixed'




res+= '\n\n'+'#current_sentiment'

print(res)