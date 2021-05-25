
# read excel files
# pre processing (NA, lower case)
# create first name and last name column
# match email format from email_database
# store formats in pickle file



from email_creator import extract_email_format, create_email
import pandas as pd
import pickle
from termcolor import colored, cprint


def database_training(data,name,path):
        
    #read excel sheets
    
    company = data.to_dict() # convert dataframe into dictionary
    print ("database training........", name)
       
    range_company = company['First Name'] # get length of data
    
    email_database = {} #empty dictionary
    for num in range_company:
        
        #get first name,last name, company name and email
        f,l,com,des,email = company['First Name'][num], company['Last Name'][num],company['Company'][num],  company['Designation'][num], company['Email'][num]
        
        key = str(com)+str(des)
        # print (key)
        
        try:
            
            #find format of given email from existing email patterns
            email_prefix,domain = extract_email_format(f,l,email)
            # print ("email_prefix",email_prefix)
            
            #split email patter and domain
            format_of_email = email_prefix+"@"+domain
            
             
        except Exception as err:
            
                   
            print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
            print_red_on_cyan(err)
            
            #if email pattern doesnt exist, assign NA
            format_of_email = "NA"
            
        email_database.update({key:format_of_email})
    
    df = pd.DataFrame({"Company":list(email_database.keys()), "format":list(email_database.values())})
    df.to_csv(path+"\\"+f"db_{name}.csv")
    print ("saving into csv")    
    print (path+"\\"+f"db_{name}.csv")
    def save_obj(obj, name ):
        with open(  path+"\\"+f'{name}.pkl', 'wb') as f:
            
            print ("pickle file path", path+"\\"+f'{name}.pkl')
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
    save_obj(email_database, name )  
