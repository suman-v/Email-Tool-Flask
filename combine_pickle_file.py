# -*- coding: utf-8 -*-
"""
Created on Mon May 17 00:15:04 2021

@author: Admin
"""




import pickle, glob

my_dict_final = {}  # Create an empty dictionary


path = r"E:\Email_tool\company_database"
 

all_files = glob.glob(path + "/*.pkl") # reading onl

    
for file in all_files:
    print (file)
    
    with open(file, 'rb') as f:
        print (len(my_dict_final))
        my_dict_final.update(pickle.load(f))   # Update contents of file1 to the dictionary
        
def save_obj(obj):
    with open(r'E:\Email_tool\eemail-flask-app\database.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    
save_obj(my_dict_final )  