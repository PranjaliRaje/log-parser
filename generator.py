import sys,os,random, time
from datetime import datetime  
from datetime import timedelta 

print("Generator has started")
datapath = sys.argv[1] 

if ( not os.path.exists(datapath)):
    os.makedirs(datapath)
    
    
ip_prefix = "192.168."


def get_usage():
    return str(random.randint(0,100))

def get_ip():
    for i in range (0,4):
        if i == 0:
            for j in range (1, 256): 
                yield (ip_prefix+str(i)+"."+str(j))       
        if i== 1 or i==2:
            for j in range (0, 256):
                yield (ip_prefix+str(i)+"."+str(j))      
        else:
            for j in range (0, 233):
                yield(ip_prefix+str(i)+"."+str(j))    

dt = datetime(2014, 10, 31, 0, 0)
end_dt= datetime(2014, 10, 31, 23, 59)

while (dt <= end_dt):
    
    unixtime = int(time.mktime(dt.timetuple()))
    
    for ip in get_ip():

        filename= ip+'.log'
        with open(os.path.join(datapath,filename), 'a+') as file: 

            for cpu in range(2):
                file.write(str(unixtime)+"     "+ ip+"     "+str(cpu)+"     "+get_usage()+"\n") 
    
    dt = dt+ timedelta(minutes=1)
    



