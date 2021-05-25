
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
    # get fisrt name,last name and company name and designation as inputs            
    email = org_email.split("@")         #split email to get prefix and domain name
    domain = email[1]
    email_prefix = ''

   
    dot_email = "." in email[0]   #check if email consist dot    
    if dot_email == True:     
        prefix = email[0].split(".")
        
        if prefix[0] == first and prefix[1] == last:        # first.last
            email_prefix = "f.l"   #1
            print (f"company:{email}  format{email_prefix}")
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial].last  
         
            email_prefix = "fi.l"   #2
            print (f"company:{email}  format{email_prefix}")
            
        if prefix[0] == last and prefix[1] == first[:1]:        # last.first[initial]
          
            email_prefix = "l.fi" #3
            print (f"company:{email}  format{email_prefix}")

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial].last[initial] 
         
            email_prefix = "fi.li"  #4
            print (f"company:{email}  format{email_prefix}")
        
        if prefix[0] == first and prefix[1] == last[:1]:        # first.last[initial] 
         
            email_prefix = "f.li"  #5
            print (f"company:{email}  format{email_prefix}")
            
        if prefix[1] == first and prefix[0] == last:        # last.first
         
            email_prefix = "l.f"  #6
            print (f"company:{email}  format{email_prefix}")
            
    underscore_email = "_" in email[0]  #check if email consist underscore
    
    if underscore_email == True:
        prefix = email[0].split("_")
           
        if prefix[0] == first and prefix[1] == last:        # first_last  
            email_prefix = "f_l"  #7
            print (f"company:{email}  format{email_prefix}")
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial]_last
         
            email_prefix = "fi_l"   #8
            print (f"company:{email}  format{email_prefix}")
            
        if prefix[0] == last and prefix[1] == first[:1]:        # last_first[initial]
            
            email_prefix = "l_fi"  #9
            print (f"company:{email}  format{email_prefix}")

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial]_last[initial] 
         
            email_prefix = "fi_li"   #10
            print (f"company:{email}  format{email_prefix}")
        
        if prefix[1] == first and prefix[0] == last:        # last_first  
            email_prefix = "l_f"  #11
            print (f"company:{email}  format{email_prefix}")
    
 
    # if dot_email == False:
       
    #     prefix = email[0]
    #     if prefix == first:
    #         email_prefix = "f"
    #         print (f"company:{email}  format{email_prefix}")
        
    #     if prefix == last:
   
    #         email_prefix = "l"
    #         print (f"company:{email}  format{email_prefix}")
            
    #     if prefix == first[:1]:
         
    #         email_prefix = "fi"
    #         print (f"company:{email}  format{email_prefix}")
            
    #     if prefix == last[:1]:
          
    #         email_prefix = "li"
    #         print (f"company:{email}  format{email_prefix}")
            
    status3 = "." and "_" in email[0]
    if status3 == False:
    
        if email[0] == first+last[:1]:
            print ("f+li")
            email_prefix = "fli"   #12
            print (f"company:{email}  format{email_prefix}")
    
        if email[0] == first[:1]+last:
            print ("fi+l")
            email_prefix = "fil"  #13
            print (f"company:{email}  format{email_prefix}")
    
    
        if email[0] == last+first[:1]:
            print ("l+fi")
            email_prefix = "lfi"  #14
            print (f"company:{email}  format{email_prefix}")
            
    
        if email[0] == last[:1]+first:
            print ("li+f")
            email_prefix = 'lif'   #15
            print (f"company:{email}  format{email_prefix}")
            
  
        if email[0] == first:
            email_prefix = "f"  #16
            print (f"company:{email}  format{email_prefix}")
        
        if email[0] == last:
   
            email_prefix = "l"  #17
            print (f"company:{email}  format{email_prefix}")
            
        if email[0] == first[:1]:
         
            email_prefix = "fi"  #18
            print (f"company:{email}  format{email_prefix}")
            
        if email[0] == last[:1]:
          
            email_prefix = "li"  #19
            print (f"company:{email}  format{email_prefix}")
            
            
            
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
            
            
        return pre+"@"+formt[1]
        
    except:
        
        return "NA"
    
    
# data = pd.read_excel(r"F:\test_file.xlsx")
# data = data[:100]

#    
    
    
