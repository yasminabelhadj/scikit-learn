# -*- coding: utf-8 -*-
import pandas as pd
import os
import time
from datetime import datetime
path = "E:\intraQuarter"
def key_stats(gather ="Total Debts/Equity(mrq)"):
    statspath= path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns =['Date','Unix','Ticker','DE Ratio'])
    data = []
    for each_dir in stock_list [1:5] :
        each_file =os.listdir (each_dir)
        ticker=each_dir.split("\\")[1]
        print(ticker)
        
        
        if len (each_file)>0:
            for file in each_file :
                date_stamp = datetime.strptime(file , "%Y%m%d%H%M%S.html")
                
                unix_time = time.mktime (date_stamp.timetuple())
                
                full_file_path= each_dir +'/'+file
                
                source= open(full_file_path,'r',encoding='utf-8').read()
                
                print(source)
                #we are going to split by gather
                try:
                    value=float(source.split('Total Debts/Equity(mrq):</td><td class="yfnc_tabledata1">')[0].split('</td>')[0])
                    print(value)
                
                    data=data.append({'Date': date_stamp ,'Unix': unix_time,'Ticker':ticker,'DE Ratio':value,},ignore_index = True)
                    print("yasmine")
                    print(data)
                except Exception as e:
                    pass
                
                #save all this to CSV file
                df = pd.DataFrame.from_dict(data)
                save= gather.replace(' ','').replace('(','').replace(')','').replace('/','')+('.csv')
                print("yas")
                print(save)
                print(data)
                df.to_csv(save)
                
                
                #it shows the file name and the Debt/Equity value
                #print(ticker + "hi yas:",value)
             
                
key_stats()
