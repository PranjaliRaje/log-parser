import sys,os,random, time
from datetime import datetime  
from datetime import timedelta 
datapath = sys.argv[1] 

if ( not os.path.exists(datapath)):
    print("Invalid Path")
    exit()
    
while True:
    l = input("Enter Command\n").split(" ")

    if l[0] == "EXIT":
        exit()

    if l[0] != "QUERY" or len(l)!=7:
        print ("Invalid command")
        exit()
    try:
        ip = l[1]
        cpu = l[2]

        start_date = l[3].split('-')
        start_time = l[4].split(':')

        end_date = l[5].split('-')
        end_time = l[6].split(':')


        st = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]), int(start_time[0]), int(start_time[1]))
        et = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), int(end_time[0]), int(end_time[1]))

        print("CPU"+cpu+" usage on "+ip+":")

        filename = ip+".log"
        with open(os.path.join(datapath,filename), 'r') as file:
            for line in file:
                if (st<et):
                    ut = str(int(time.mktime(st.timetuple())))
                    if ut in line:
                        logline = line.split("     ")
                        if logline[2] == cpu:  
                            print("("+str(st.year)+"-"+str(st.month).zfill(2)+"-"+str(st.day).zfill(2)+" "+str(st.hour).zfill(2)+":"+str(st.minute).zfill(2)+", "+ str(logline[3][:-1])+"%)" , end= " ")                   
                            st = st+ timedelta(minutes=1)
    except:
        print("Invalid Command")
    print("\n")     
        