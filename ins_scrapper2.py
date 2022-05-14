from time import perf_counter
import re
import json
import requests 

with open('cookies.txt','r') as r:
    cook=r.read()

Url='https://www.instagram.com/graphql/query/'
head={'cookie':str(cook)}

user_id='54052706'
taylor='11830955'

def get_text(after): 
           
    payload={
    'query_hash':'69cba40317214236af40e7efa697781d',
    'variables': "{\"id\":\"1381895679\",\"first\":50,\"after\":\""+after+"\"}"}
    response=requests.get(Url,headers=head,params=payload).text
    result=str(json.loads(response))
    return result


def find_end_cursor(content):
    try:
        res=re.compile('end_cursor.{20,150}=')
        text=(res.findall(content))[0]
        result=text.replace("end_cursor': '",'')
    except:
        result=''  

    return result 

def find_img (content,Quality='s480x480')  : 
    result_img=re.compile('https://.{1,200}jpg?.{1,200}480x480&.{1,400}nc_sid=86f79a')
    img_source=result_img.findall(content)
    return img_source

def find_video (content,Quality='480x480') : 
    result_film=re.compile('https://.{1,200}mp4?.{1,300}480x480&.{1,300}nc_sid=86f79a')
    video_source=result_film.findall(content)
    return video_source    

def file(source):
        if len(source)>0:
            with open('source.txt','a') as f:
                for x in source:
                    f.write(x+'\n')

start_time=perf_counter()
Base_end_cursor=''

num=0
while True:
    num+=1
    content=get_text(Base_end_cursor)
    secound_end_cursor=find_end_cursor(content)

    if secound_end_cursor!=Base_end_cursor:
        Base_end_cursor=secound_end_cursor   
    else :
        print('done!')
        break  

    Videos=find_video(content)
    Imgs=find_img(content)

    file(Videos)
    file(Imgs)

    print(num)


end_time=perf_counter()
print('speed:',(num/(end_time-start_time))*50)
    















    


