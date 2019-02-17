import csv,time,datetime; from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

artists='Artists';albums='Albums';tracks='Tracks'
name='USERNAME'



def f(number,subject,days):
    totaltime1=time.time()
    timedata=[];data=[]
    fulldata=[];names=[];nums=[]
 
    n=0;secs=days*86400
    
    with open(f"{name}.csv",'r',encoding='utf-8') as file:
        
        csv_reader=csv.reader(file)
        next(csv_reader)
        t=int(time.time())
        t1=time.time()
        print(f"Scanning {subject}...")
        
        if subject=='Artists': column=0
        if subject=='Albums': column=1
        if subject=='Tracks': column=2

        for line in csv_reader:
            unixtime=int(time.mktime(datetime.strptime(line[3],"%d %b %Y %H:%M").timetuple()))
            if (t-unixtime)>secs and secs!=0:
                break
            
            n+=1
            if line[column]=='': next(csv_reader);print(line)# will show albumless tracks
            elif line[column] not in names:
                names.append(line[column])
                nums.append(1)
         
            else:
                nums[names.index(line[column])]+=1
                
        t2=time.time()
        print(f"{subject} scanned in {t2-t1} seconds")

        
        for i in range(len(nums)):
            data.append((nums[i],names[i]))
        data.sort(reverse=True)
        
        
        plottime=time.time()
        
        for j in range(number):
            x=[];y=[];p=0
            file.seek(0)
            for line2 in csv_reader:
                unixtime=int(time.mktime(datetime.strptime(line2[3],"%d %b %Y %H:%M").timetuple()))
        
                
                if data[j][1]==line2[column]:
                    
                    if (t-unixtime)>secs and secs!=0:
                        break
                    p+=1
                    x.insert(0,unixtime)
                    
                    y.append(p)
                
            
            
            x.append(int(time.time()))
            y.append(p)
            x=[datetime.fromtimestamp(val) for val in x]
            plt.plot(x,y,label=data[j],linewidth=1.0) #line thickness
            #plt.scatter(x,y,s=1.8)       #size of scatter points (works best with top tracks)
            print(data[j])
        

    if days>90 or days==0: timetype='%Y-%m'
    else: timetype='%Y-%m-%d'

    #matplotlib.rc('font', family='TakaoPGothic')
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(DateFormatter(timetype))
    plt.legend(fontsize=5,loc=2)    #size of legend font
    plt.grid(0,linestyle='--',alpha=0.5)
    plt.xlabel('Date')
    plt.ylabel('Plays')
    startdate=datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d')
    plt.title(f"{name}'s Top {number} {subject} Since {startdate}",fontsize=10)
    plt.savefig(f"{name}'s Top {number} {subject} Since {startdate}.png",dpi=800,bbox_inches='tight')
    totaltime2=time.time()
    print(f"{totaltime2-plottime} seconds to plot data")
    print(f"{totaltime2-totaltime1} seconds overall")
    plt.clf()
      

 
