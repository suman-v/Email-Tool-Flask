# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:11:55 2021

@author: User
"""
def email_verifier_api(email_address):
    import requests     
    api_key = "e3af5dd0-cf4f-43b4-96ce-bfc7cd20ade2"
    
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address},
        headers = {'Authorization': "Bearer " + api_key })
    
    status = response.json()['status']
    status_label= ''
    if status == "valid":
      
        status_label = "valid"
    elif status == "invalid":
        status_label = "invalid"
        
    else:
        status_label = "unknown"
   
        
    return status_label
  
import csv
with open(r"F:\test\Output_csv.csv") as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         status_label = email_verifier_api(row['email'])
         print(row['email'], "::", status_label)

# {'email': 'foo@bar.com', 'status': 'valid'}