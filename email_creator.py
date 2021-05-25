
'''
File name: email_generator

function 1
extract_email_format :  Function will match email format for each predefined formats
    input : first_name, last_name, company_name, designation
    output : email_format, domain, designation
    
function 2
create_email :

    
'''

import pandas as pd

def extract_email_format(first,last,org_email): 
    # print ("ennter")
    # get fisrt name,last name and company name and designation as inputs            
    email = org_email.split("@")         #split email to get prefix and domain name
    domain = email[1]
    email_prefix = ''

    last_name_check_dot = "." in last
    last_name_check_hyphen = "-" in last
    
    if last_name_check_hyphen == True:
        email_prefix = "fil"
    dot_email = "." in email[0]   #check if email consist dot 
    
    if dot_email == True:    
        
       
        prefix = email[0].split(".")
        
        if prefix[0] == first and prefix[1] == last:        # first.last
            email_prefix = "f.l"   #1
           
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial].last  
         
            email_prefix = "fi.l"   #2
           
            
        if prefix[0] == last and prefix[1] == first[:1]:        # last.first[initial]
          
            email_prefix = "l.fi" #3
           

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial].last[initial] 
         
            email_prefix = "fi.li"  #4
           
        
        if prefix[0] == first and prefix[1] == last[:1]:        # first.last[initial] 
         
            email_prefix = "f.li"  #5
            
        if prefix[1] == first and prefix[0] == last:        # last.first
         
            email_prefix = "l.f"  #6
            
    underscore_email = "_" in email[0]  #check if email consist underscore
    
    if underscore_email == True:
        prefix = email[0].split("_")
           
        if prefix[0] == first and prefix[1] == last:        # first_last  
            email_prefix = "f_l"  #7
           
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial]_last
         
            email_prefix = "fi_l"   #8
           
            
        if prefix[0] == last and prefix[1] == first[:1]:        # last_first[initial]
            
            email_prefix = "l_fi"  #9
           

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial]_last[initial] 
         
            email_prefix = "fi_li"   #10
            
        
        if prefix[1] == first and prefix[0] == last:        # last_first  
            email_prefix = "l_f"  #11
            
    
 
    hyphen_email = "-" in email[0]  #check if email consist underscore
    
    if hyphen_email == True:
       
        prefix = email[0].split("-")
          
        if prefix[0] == first and prefix[1] == last:        # first_last 
            
            email_prefix = "f-l"  #7
           
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial]_last
         
            email_prefix = "fi-l"   #8
           
            
        if prefix[0] == last and prefix[1] == first[:1]:        # last_first[initial]
            
            email_prefix = "l-fi"  #9
       

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial]_last[initial] 
         
            email_prefix = "fi-li"   #10
          
        
        if prefix[1] == first and prefix[0] == last:        # last_first  
            email_prefix = "l-f"  #11
           

        check_list = [".", "-", "_"]
        
        status_for_email = []
        # for i in  check_list:   
            
        #     status_for_email.append(i in email[0] )
            
        # status_for_single= True in status_for_email
        
        # print (status_for_single)
    else:
                
                    # print (email)
                    if email[0] == first+last[:1]:
                      
                        email_prefix = "fli"   #12
                      
                
                    if email[0] == first[:1]+last:
                       
                        email_prefix = "fil"  #13
                        
                   
                    if email[0] == first+last:
                      
                        email_prefix = "fl"  #14               
                
                    if email[0] == last+first[:1]:
                      
                        email_prefix = "lfi"  #14
                   
                        
                
                    if email[0] == last[:1]+first:
                       
                        email_prefix = 'lif'   #15
                    
                        
              
                    if email[0] == first:
                        email_prefix = "f"  #16
                       
                    
                    if email[0] == last:
               
                        email_prefix = "l"  #17
                      
                        
                    if email[0] == first[:1]:
                     
                        email_prefix = "fi"  #18
                      
                        
                    if email[0] == last[:1]:
                      
                        email_prefix = "li"  #19
        
    # print (email_prefix, domain)
    return email_prefix, domain



#email_database = email_format("suman", "verma", "s@math.com")

def create_email(f,l,company,email_format):
#    email_format = email_database[company]
    try:
        formt = email_format.split("@")     
        
         
        if formt[0] == "f.l":
            pre  = f+"."+l
            
        if formt[0] == "l.f":
            pre  = l+"."+f
            
        if formt[0] == "l.fi":
            pre  = l+"."+f[:1]
            
        if formt[0] == "fi.l":
            pre  = f[:1]+"."+l
            
        if formt[0] == "fi.li":
            pre  = f[:1]+"."+l[:1]
            

        if formt[0] == "f.li":
            pre  = f+"."+l[:1]
            
            
        if formt[0] == "f_l":
            pre  = f+"_"+l
            
        if formt[0] == "l_f":
            pre  = l+"_"+f          
            
        if formt[0] == "l_fi":
            pre  = l+"_"+f[:1]
            
            
            
        if formt[0] == "fi_l":
            pre  = f[:1]+"_"+l
            
            
            
        if formt[0] == "fi_li":
            pre  = f[:1]+"_"+l[:1]
            
                       
            
        if formt[0] == "fli": 
            pre  = f+l[:1]
            
        if formt[0] == "fil":
            pre  = f[:1]+l
            
        if formt[0] == "fl":
            pre  = f+l

        if formt[0] == "lif":
            pre  = l[:1]+f
            
        if formt[0] == "lfi":
            pre  = l+f[:1]
            
        if formt[0] == "f":
            pre  = f  
            
        if formt[0] == "l":
            pre  = l
            
        if formt[0] == "fi":
            pre  = f[:1]
            
        if formt[0] == "li":
            pre  = l[:1] 
            
            
        if formt[0] == "f-l":
            pre  = f+"-"+l
            
        if formt[0] == "l-f":
            pre  = l+"-"+f          
            
        if formt[0] == "l-fi":
            pre  = l+"_"+f[:1]
            
            
            
        if formt[0] == "fi-l":
            pre  = f[:1]+"_"+l
            
            
            
        if formt[0] == "fi-li":
            pre  = f[:1]+"_"+l[:1]  
      
        # print (pre+"@"+formt[1])
        return pre+"@"+formt[1]
        
    except:
        
        return "NA"
    
    
# data = pd.read_excel(r"F:\test_file.xlsx")
# data = data[:100]

#    
    
    
