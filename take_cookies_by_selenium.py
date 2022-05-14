from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#for wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

# login:

Username=input('username: ')
Password=input('password: ')
Chrome_Driver_path='D:\\chromedriver.exe'    
d=webdriver.Chrome(Chrome_Driver_path)    
d.get('https://www.instagram.com')

user_name=WebDriverWait(d,10).until(ec.element_to_be_clickable((By.NAME , 'username')))
user_name.send_keys(Username)

pass_word=WebDriverWait(d,5).until(ec.element_to_be_clickable((By.NAME , 'password')))
pass_word.send_keys(Password)

b_path='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button'
button_login=WebDriverWait(d,3).until(ec.element_to_be_clickable((By.XPATH , b_path)))
button_login.click()



Login_alert=WebDriverWait(d,20).until(ec.element_to_be_clickable((By.XPATH , '//*[@id="react-root"]/section/main/div/div/div/section/div/button')))
Login_alert.click() 

sleep(5)

#login_ cookies:

csrftoken=d.get_cookie('csrftoken')
datr=d.get_cookie('datr')
dpr=d.get_cookie('dpr')
ds_user_id=d.get_cookie('ds_user_id')
ig_did=d.get_cookie('ig_did')
ig_nrcb=d.get_cookie('ig_nrcb')
mid=d.get_cookie('mid')
rur=d.get_cookie('rur')
sessionid=d.get_cookie('sessionid')
shbid=d.get_cookie('shbid')
shbts=d.get_cookie('shbts')

All_get_cookies=[csrftoken,datr,dpr,ds_user_id,ig_did,ig_nrcb,mid,rur,sessionid,shbid,shbts]

cookie_list=[(x['name'],x['value'])  for x in All_get_cookies]


  
#login_headers:

#headers = d.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
#headers = headers.splitlines()




#write All get cookies in a cookies.txt

cookie_string=f'ig_did={cookie_list[4][1]}; ig_nrcb={cookie_list[5][1]}; mid={cookie_list[6][1]}; csrftoken={cookie_list[0][1]}; sessionid={cookie_list[8][1]}; shbid={cookie_list[9][1]}'

with open('cookies.txt','w') as f:
    f.write(cookie_string)


print('All cookies were taken!')

# c=f'cookie: ig_did={}; ig_nrcb={}; mid={}; csrftoken={}; sessionid={}; ds_user_id=5923342284; shbid={}'






    
