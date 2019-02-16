import csv,time,datetime; from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

artists='Artists';albums='Albums';tracks='Tracks'
name='hedphylem'



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
        if subject=='Artists':
            column=2
        if subject=='Albums':
            column=4
        if subject=='Tracks':
            column=6
    
        for line in csv_reader:
            if (t-int(line[0]))>secs and secs!=0:
                break
            
            n+=1

            if line[column] not in names:
                names.append(line[column])
                nums.append(1)
               #if subject=='Tracks':
                    
            else:
                nums[names.index(line[column])]+=1
                
        t2=time.time()
        print(t2-t1)

        
        for i in range(len(nums)):
            data.append((nums[i],names[i]))
        data.sort(reverse=True)
        
        
        plottime=time.time()
        
        for j in range(number):
            x=[];y=[];p=0
            file.seek(0)
            for line2 in csv_reader:

                #print(data);print(line)
                if data[j][1] in line2[column]:
                    if (t-int(line2[0]))>secs and secs!=0:
                        break
                    p+=1
                    x.insert(0,int(line2[0]))
                    #print(x)
                    y.append(p)
                #print(line2)
            
            #print(x)
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
    startdate=datetime.utcfromtimestamp(int(line[0])).strftime('%Y-%m-%d')
    plt.title(f"{name}'s Top {number} {subject} Since {startdate}",fontsize=10)
    plt.savefig(f"{name}'s Top {number} {subject} Since {startdate}.png",dpi=800,bbox_inches='tight')
    totaltime2=time.time()
    print(f"{totaltime2-plottime} seconds to plot data")
    print(f"{totaltime2-totaltime1} seconds overall")
    plt.clf()
      

 
