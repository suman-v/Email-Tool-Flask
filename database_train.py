
# read excel files
# pre processing (NA, lower case)
# create first name and last name column
# match email format from email_database
# store formats in pickle file



from email_creator import extract_email_format, create_email
import pandas as pd
from load_excel_file import read_excel_sheets
import pickle

  
def database_training(database_path):
    
    
    #read excel sheets
    data = read_excel_sheets(database_path)  # function to read excel files from folder and multiple sheets from excel file, returning dataframe
    
    company = data.to_dict() # convert dataframe into dictionary
       
    range_company = company['First Name'] # get length of data
    
    email_database = {} #empty dictionary
    for num in range_company:
        
        #get first name,last name, company name and email
        f,l,com,des,email = company['First Name'][num], company['Last Name'][num],company['Company'][num],  company['Designation'][num], company['Email'][num]
        
        key = str(com)+str(des)
        
        
        try:
            
            #find format of given email from existing email patterns
            email_prefix,domain = extract_email_format(f,l,email)
            # print ("email_prefix",email_prefix)
            
            #split email patter and domain
            format_of_email = email_prefix+"@"+domain
            
        except:
            
            #if email pattern doesnt exist, assign NA
            format_of_email = "NA"
            
        
        email_database.update({key:format_of_email})
        
    
    def save_obj(obj, name ):
        with open( name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
    save_obj(email_database, "database" )  
  
def load_obj(name ):
  with open( name + '.pkl', 'rb') as f:
      return pickle.load(f)
  
# ddd= load_obj("database" )