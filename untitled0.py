# Python code to demonstrate
# to split strings
# on uppercase letter
 
import re

# Initialising string
fc = 'AdityaAdVenkatesh'
sc= 'AdityaADVenkatesh'
tc= 'SumanVerma'
dc= 'Komal'
name= [dc,fc,sc,tc]



def split_name(name):
    res_list = []
    res = re.findall('[A-Z][^A-Z]*', name)
    f=''
    l=''
    len_res= len(res)
    if len_res == 1:
        print (len_res,"Result: ",res)
        f= name
        l= name
        
    if len_res == 2:
        print (len_res,"Result: ",res)  
        f= res[0]
        l= res[-1]

    if len_res > 2:
        if len(res[-2]) > 1:
            f= res[0]
            l = res[-2]+res[-1]
        if len(res[-2]) < 2:
            f= res[0]
            l = res[-1]        
    fr = [f,l]
    print( "Final Result: ", fr)
    return fr

contact_name = [split_name(i) for i in name]





# from concurrent.futures import ThreadPoolExecutor
# import requests
# from requests.exceptions import ConnectionError

# def validate_existence(domain):
#     try:
#         response = requests.get(f'http://{domain}', timeout=10)
#     except ConnectionError:
#         print(f'Domain {domain} [---]')
#     else:
#         print(f'Domain {domain} [+++]')


# list_domain = ['a-1freeman.com', 'atime.org', 'eloanline.com']

# with ThreadPoolExecutor() as executor:
#     executor.map(validate_existence, list_domain)