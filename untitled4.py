# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:51:42 2021

@author: User
"""
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:09:54 2021

@author: Admin
"""

from split_contact_name import split_name
from datetime import datetime
import pandas as pd
import glob
from termcolor import colored, cprint
import csv 

def last_name(i):
    try:
        return i[-1]
    except:
        return i[0]



excel_file_path = r'F:\test\Tulsa, OK Seggrigation  2018.xlsx'

input_file_column = ['Company', 'Contact Name','Designation']

database_file_column = ['Company', 'Contact Name',  'Email','Designation']

def read_excel_file(excel_file_path, column_name):
    
    data=pd.DataFrame()
    for i in range(0,6): # reading multiple sheets from one excel file
       
        try:
                
            df = pd.read_excel(excel_file_path, index_col=None, header=0, sheet_name=i) #read excel file
            df = df[column_name]
            data=pd.concat([data, df], axis=0)
    
            data= data.dropna(subset = ['Company','Contact Name']) #dropping Nan values
            contact_name = [split_name(i) for i in data['Contact Name']]
            print ("Sheet No:",i)
            print ("Size of data:",data.shape)
          
        except Exception as err:
            
                   
            print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
            print_red_on_cyan(err)
    try:      
        data['temp'] = data['Contact Name'].str.split(" ")
        data= data.dropna(subset = ['Company','Contact Name', 'temp'])
        data['Last Name'] = [last_name(i) for i in data['temp']]
        data['First Name'] = [i[0] for i in data['temp']]
    
        data['First Name'] = data['First Name'].str.lower()
       
        data['Last Name']= data['Last Name'].str.lower()
       
        data['Company']= data['Company'].str.lower()
     
        data['Designation'] = data['Designation'].str.lower()
                                                  
        print ("converted upper case to lower case") 
        data['Email']= data['Email'].str.lower()
        
    except:
        print ("no data")
 
    
    return data

