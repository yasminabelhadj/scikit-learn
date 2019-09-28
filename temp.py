# -*- coding: utf-8 -*-
import pandas as pd
import os
import time
from datetime import datetime
path = "E:\intraQuarter" #data downloaded from this link 
def key_stats(gather ="Total Debts/Equity(mrq)"):
    statspath= path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns =['Date','Unix','Ticker','DE Ratio'])
    
    sp_500=pd.DataFrame.from_csv("./MULTPL-SP500_DIV_MONTH")
    for each_dir in stock_list [1:] :
        each_file =os.listdir (each_dir)
        ticker=each_dir.split("\\")[1]
       
        
        if len (each_file)>0:
            for file in each_file :
                date_stamp = datetime.strptime(file , "%Y%m%d%H%M%S.html")
                
                unix_time = time.mktime (date_stamp.timetuple())
                print(unix_time)
                
                full_file_path= each_dir +'/'+file
                
                source= open(full_file_path,'r',encoding='utf-8').read()
                
                
                #we are going to split by gather
                try:
                    value=float(source.split('Total Debts/Equity(mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    print(value)
                    try:
                        sp_500_date= datetimefromtimestamp(unix_time).strftime('%Y-%m-%y')
                        row=
    
                    df=df.append({'Date': date_stamp ,'Unix': unix_time,'Ticker':ticker,'DE Ratio':value,},ignore_index = True)
                    print("yasmine")

                except Exception as e:
                    pass
                #save all this to CSV file
    save= gather.replace(' ','').replace('(','').replace(')','').replace('/','')+('.csv')
    print("yas")
    print(save)

    df.to_csv(save)

                
                
                
                #it shows the file name and the Debt/Equity value
                #print(ticker + "hi yas:",value)
             
                
key_stats()
