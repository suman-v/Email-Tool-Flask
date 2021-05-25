# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:32:16 2021

@author: User
"""
from email_creator import create_email, extract_email_format
from load_excel_file import read_excel_sheets
import pickle
from database_train import database_training
from read_Excel_file import read_excel_file
from generate_Email import generate_email



# folder_path_for_excelfiles = r"E:\Data Files\test"  #r'F:\test'
# output = 'F:\test'


# database_training(folder_path_for_excelfiles)

excel_file_path = r"F:\test\Tulsa, OK Seggrigation  2018.xlsx"
# data = read_excel_sheets(folder_path_for_excelfiles)

input_data= read_excel_file(excel_file_path)


output =  generate_email(input_data )
