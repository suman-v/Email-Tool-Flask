# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:41:09 2021

@author: User
"""
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:30:07 2021

@author: User
"""


from email_creator import create_email, extract_email_format
import pickle

  
def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
    
    
def generate_email(input_data ):
    
   

          
    email_database = load_obj("database" )  
   
    
    input_data= input_data.reset_index()
    
   
    
    input_data['email'] = ''
    #                    input_data['email_status'] = ''
    for i in range (input_data.shape[0]):
        f= input_data['First Name'][i]
        l= input_data['Last Name'][i]
        c= input_data['Company'][i]  
        d = input_data['Designation'][i]
        key= str(c)+str(d)
        try :
            formatemail = email_database[key]
           
            domain = formatemail.split("@")
            
        except:
            
            
            formatemail = "NA"
           
            domain = "NA"
        print (formatemail)
        input_data['email'][i] = create_email(f,l,c,formatemail)
        
    return input_data
        
        
        

