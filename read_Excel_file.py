# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:09:54 2021

@author: Admin
"""


from datetime import datetime
import pandas as pd
import glob
from termcolor import colored, cprint
  

def last_name(i):
    try:
        return i[-1]
    except:
        return i[0]

def read_excel_file(excel_file_path):

    print ("reading excel file")
    data=pd.DataFrame()
    for i in range(0,6): # reading multiple sheets from one excel file
        print (excel_file_path)
        try:
                
            df = pd.read_excel(excel_file_path, index_col=None, header=0, sheet_name=i) #read excel file
            df = df[['Company', 'Contact Name',  'Email','Designation']]
            data=pd.concat([data, df], axis=0)
    
            data= data.dropna(subset = ['Company','Contact Name']) #dropping Nan values
           
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

def read_excel_folder(folder_path_for_excelfiles):
    print ("reading folder")
    path =  folder_path_for_excelfiles# use your folder path to read excel 
    print (path)
    all_files = glob.glob(path + "/*.xlsx") # reading only excel files using extension
    data=pd.DataFrame()
    for filename in all_files: #reading excel files in loop from given folder
    
       print (filename)
       df =  read_excel_file(filename)
       data=pd.concat([data, df], axis=0)
       print (f"file__{filename}___")
       print ("Size of data:",data.shape)
       
    return data #return excel data in dataframe

def read_excel_file_input_file(excel_file_path):

    
    data=pd.DataFrame()
    for i in range(0,5): # reading multiple sheets from one excel file
        print (excel_file_path)
        try:
                
            df = pd.read_excel(excel_file_path, index_col=None, header=0, sheet_name=i) #read excel file
            # df = df[['Company', 'Contact Name', 'Designation']]
            data=pd.concat([data, df], axis=0)
    
            data= data.dropna(subset = ['Company','Contact Name']) #dropping Nan values
           
            print ("Sheet No:",i)
            print ("Size of data:",data.shape)
          
     
        except Exception as err:
            
                   
            print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
            print_red_on_cyan(err)
            
    data['temp'] = data['Contact Name'].str.split(" ")
    data= data.dropna(subset = ['Company','Contact Name', 'temp'])
    data['Last Name'] = [last_name(i) for i in data['temp']]
    data['First Name'] = [i[0] for i in data['temp']]

    data['First Name'] = data['First Name'].str.lower()
   
    data['Last Name']= data['Last Name'].str.lower()
   
    data['Company']= data['Company'].str.lower()
 

    data['Designation'] = data['Designation'].str.lower()
                                              
    print ("converted upper case to lower case") 
    
    return data