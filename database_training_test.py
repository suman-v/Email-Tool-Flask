# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:31:56 2021

@author: User
"""
from email_creator import create_email, extract_email_format
import pickle, glob
from database_train import database_training
from read_Excel_file import read_excel_file, read_excel_folder
# from read_excel_folder import read_excel_sheets
from database_training import database_training
import time
import pandas as pd
import ntpath
start = time.time()
database_path = r'E:\Email_tool\Data Files'
pickle_file_path = r'E:\Email_tool\company_database'
def read_excel_folder(folder_path_for_excelfiles,pickle_file_path):
    print ("reading folder")
    path =  folder_path_for_excelfiles# use your folder path to read excel 
    print (path)
    all_files = glob.glob(path + "/*.xlsx") # reading only excel files using extension
    data=pd.DataFrame()
    for filename in all_files: #reading excel files in loop from given folder
       start = time.time()
       print (filename)
       data =  read_excel_file(filename)
      
       try:
           file_name = filename.split("\\")
           file_name = file_name[-1].split(".")
       except:
            file_name = "name"
       database_training(data,file_name[0],pickle_file_path)
       # data=pd.concat([data, df], axis=0)
       print (f"file__{filename}___")
       print ("Size of data:",data.shape)
       end = time.time()
       print(f"Runtime of the program is {end - start}")

       
    return data #return excel data in dataframe

# data = read_excel_folder(database_path, pickle_file_path)
# end = time.time()
# print(f"Final Runtime of the program is {end - start}")
