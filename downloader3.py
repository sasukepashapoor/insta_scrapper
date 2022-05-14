import requests
from time import  sleep,perf_counter
from threading import Thread
import re

with open('source.txt','r') as f:
    Urls=f.readlines()


counter=[]
can_not_download=[] 

def get_content(url,Time=10):
    result=requests.get(url,timeout=Time,)
    if result.ok==False:
        sleep(0.5)
        result=requests.get(url,timeout=Time,) 
        if result.ok==False:
            return False  
                                    #if return = False means that can not download file         
    return result.content 



def file_name(url):
    res=re.compile('jpg')
    img=res.findall(url)
    if len(img)>=1:
        File_Extensions='.jpg'
        return  (url.split('=')[-3])+File_Extensions
    elif len(img)==0:
        File_Extensions='.mp4'
        # counter.append(2)
        return  (url.split('=')[-3])+File_Extensions
   

def write_file(name,content):
    with open('./img/'+name,'wb') as wb:
        wb.write(content)


def download(url):
    counter.append(1)
    name=file_name(url)
    result=get_content(url)
    if result==False:
        return None
    write_file(name,result)


Start_time=float(perf_counter())
for x in range(9,len(Urls),10):
    
    num1=Urls[x-9]
    num2=Urls[x-8]
    num3=Urls[x-7]
    num4=Urls[x-6]
    num5=Urls[x-5]
    num6=Urls[x-4]
    num7=Urls[x-3]
    num8=Urls[x-2]
    num9=Urls[x-1]
    num10=Urls[x]
    
    d1=Thread(target=download,args=(num1,))
    d2=Thread(target=download,args=(num2,))
    d3=Thread(target=download,args=(num3,))
    d4=Thread(target=download,args=(num4,))
    d5=Thread(target=download,args=(num5,))
    d6=Thread(target=download,args=(num6,))
    d7=Thread(target=download,args=(num7,))
    d8=Thread(target=download,args=(num8,))
    d9=Thread(target=download,args=(num9,))
    d10=Thread(target=download,args=(num10,))
    
    d1.start()
    d2.start()
    d3.start()
    d4.start()
    d5.start()
    d6.start()
    d7.start()
    d8.start()
    d9.start()
    d10.start()
    
    d1.join()
    d2.join()
    d3.join()
    d4.join()
    d5.join()
    d6.join()
    d7.join()
    d8.join()
    d9.join()
    d10.join()
    
    print(len(counter),'done')
End_time=float(perf_counter())    
Process_time=End_time-Start_time
# print('process_time:',type(Process_time),Process_time)
# print('len(counter):',len(counter),type(len(counter)))
speed=((len(counter)-len(can_not_download))/Process_time)
print('speed:',speed)



# print('videos:',count_video=counter.count(2))
if len(can_not_download)==0:
    print('All files downloaded !')
else:
    print('can not download :',can_not_download)






    



   
    














