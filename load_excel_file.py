# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:09:21 2021

@author: User
"""
from datetime import datetime
import pandas as pd
import glob
from read_Excel_file import read_excel_file

  
def read_excel_sheets(folder_path_for_excelfiles):
    path =  folder_path_for_excelfiles# use your folder path to read excel files
    all_files = glob.glob(path + "/*.xlsx") # reading only excel files using extension
    data=pd.DataFrame()
    for filename in all_files: #reading excel files in loop from given folder
    
       df =  read_excel_file(filename)
       data=pd.concat([data, df], axis=0)
       print (f"file__{filename}___")
       print ("Size of data:",data.shape)
       
    return data #return excel data in dataframe



def read_excel_sheets2(folder_path_for_excelfiles):
    path =  folder_path_for_excelfiles# use your folder path to read excel files
    all_files = glob.glob(path + "/*.xlsx") # reading only excel files using extension
    
    li = []
    
    for filename in all_files: #reading excel files in loop from given folder
        
        print (filename)
        try:
            
                for i in range(0,5): # reading multiple sheets from one excel file
                    print (filename)
                    try:
                        
                        print (filename)
                        df = pd.read_excel(filename, index_col=None, header=0, sheet_name=i) #read excel file
                        
                        print (df.columns)
                        df = df[['Company', 'Contact Name',  'Email','Designation']]
                        
                        print ("Reading data")
                        last = df['Contact Name'].str.split(" ")
        
                        first_name= [i[0] for i in last]
                        last_name= [i[-1] for i in last]
                            
                        df['First Name'] = first_name
                        df['Last Name'] = last_name
                        print("created last namd and first name columns")
                        df= df.dropna() #dropping Nan values
                      

                        print ("Excel file name:",filename) 
                        print ("Sheet No:",i)
                        print ("Size of data:",df.shape)
                      
                        li.append(df) #append data from first sheet in list
              
                        print (len(li))
                        print ("*"*80)
                    except:
                        
                        print ("No sheet")
                
        except:
            
            print ("ERROR IN", filename)
            
    data = pd.DataFrame()
    try:
        #concat all files data in one dataframe
        data = pd.concat(li, axis=0, ignore_index=True)
        
        #creating last and first name column using contac_name
        last = data['Contact Name'].str.split(" ")
        
        first_name= [i[0] for i in last]
        last_name= [i[-1] for i in last]
        
        data['First Name'] = first_name
        data['Last Name'] = last_name
            
        data = data[['Company', 'First Name', 'Contact Name', 'Last Name', 'Email', 'Designation']] 

    except:
        data = pd.DataFrame()
        print ("data issue")
   
        
   
    
        
    # make upper case to  lower case
    data['First Name'] = data['First Name'].str.lower()
   
    data['Last Name']= data['Last Name'].str.lower()
   
    data['Company']= data['Company'].str.lower()
 
    data['Email']= data['Email'].str.lower()
 
    data['Designation'] = data['Designation'].str.lower()
                                              
    print ("converted upper case to lower case")   
    return data #return excel data in dataframe



