# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:09:59 2019

@author: user
"""
import pandas as pd
import os
import time
from datetime import datetime
path = "E:\intraQuarter" #data downloaded from this link 
def key_stats(gather ="Total Debt/Equity(mrq)"):
    statspath= path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns =['Date','Unix','Ticker','DE Ratio','Price','SP500'])
    sp500_df=pd.read_csv("./MULTPL-SP500_DIV_MONTH.csv")
    row=pd.DataFrame(columns =['Date','Value'])

   #sp_500=pd.DataFrame.from_csv("./MULTPL-SP500_DIV_MONTH")
    for each_dir in stock_list [1:5] :
        each_file =os.listdir (each_dir)
        ticker=each_dir.split("\\")[1]
        if len (each_file)>0:
            for file in each_file :
                date_stamp = datetime.strptime(file , "%Y%m%d%H%M%S.html")
                
                unix_time = time.mktime (date_stamp.timetuple())
                
                
                full_file_path= each_dir +'/'+file
                
                source= open(full_file_path,'r').read()
                
                 #we are going to split by gather
                try:
                    #if something is not float we wouldn t deal with it it just passes
                    value=float(source.split('Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                   
                        #259200 : the number of seconds in 3 days
                    sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                    for i in range (len(sp500_df['Date'])):
                  
                        if (sp500_df['Date'][i] == sp500_date):
                            print('l')
                            row=row.append({'Date':sp500_date,'Price':sp500_df['Value'][i]},ignore_index = True)
                            print('m')
                        else:
                            break;
                            
                            
                    sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                    for j in range (len(sp500_df['Date'])):
                        if (sp500_df['Date'][j] == sp500_date):
                            print('q')
                            row=row.append({'Date':sp500_date,'Price':sp500_df['Value'][j]},ignore_index = True)
                            print('y')

                        
                         
                    stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    
                    #print("Stock_price:",stock_price , "Ticker:" ,ticker)
                    df=df.append({'Date': date_stamp ,
                                  'Unix': unix_time,
                                  'Ticker':ticker,
                                  'DE Ratio':value,
                                  'Price': stock_price,
                                  'SP500':row['Price']},ignore_index = True)
                    print("yasmine")

                except Exception as e:
                    #because some companies don t have any values of these columns.
                    pass
                #save all this to CSV file
    save= gather.replace(' ','').replace('(','').replace(')','').replace('/','')+('.csv')
    
    print(save)

    df.to_csv(save)

                
                
                
                #it shows the file name and the Debt/Equity value
                #print(ticker + "hi yas:",value)

key_stats()

